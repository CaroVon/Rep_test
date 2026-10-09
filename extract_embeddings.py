"""
Stage 1 - extract everything the steering comparison needs, then free the GPU.

Saves to --out_dir:
  G.npy            (V, d)  output-embedding (unembedding) matrix; float32 if V*d<1e8 else float16
  pairs.npy        (n, 2)  token ids (base verb, 3rd-person verb), single-token, disjoint
  E_base.npy       (N, d)  last-layer inputs to the output head (lambda) for contexts predicting base verbs
  E_target.npy     (N, d)  same for contexts predicting 3rd-person verbs
  contexts.json    {"base": [...texts], "target": [...texts]}
  meta.json        model, dtype, quantization, V, d, n_pairs, logits_rel_err, library versions, date

lambda is captured with a forward-pre-hook on the output head, so it is EXACTLY the vector the model
multiplies with the unembedding matrix (works for any final norm / tied weights).

Examples (RTX 4060, 8 GB):
  python extract_embeddings.py --model gpt2 --dtype float32 --out_dir data/gpt2
  python extract_embeddings.py --model google/gemma-3-1b-pt --dtype bfloat16 --out_dir data/gemma1b
  python extract_embeddings.py --model google/gemma-3-4b-pt --dtype bfloat16 --load_in_4bit --out_dir data/gemma4b
Gemma models are gated: accept the license on the Hugging Face model page and run `huggingface-cli login`.
All output paths are rebuilt from whitelist path components by safe_run_dir(), so traversal is impossible.
"""
import argparse, json, os, datetime
import re as _re
from pathlib import Path
import numpy as np


def safe_run_dir(raw):
    """Rebuild a user-supplied output directory from whitelist tokens only ('..' and separators cannot appear)."""
    parts = [p for p in str(raw).replace("\\", "/").split("/") if _re.fullmatch(r"[A-Za-z0-9._-]+", p) and p not in (".", "..")]
    if not parts:
        raise SystemExit(f"unsafe output directory (only [A-Za-z0-9._-] path components allowed): {raw!r}")
    return os.path.join(*parts)

VERBS = ("accept add agree allow answer appear ask believe belong break build buy call carry catch change check choose "
         "clean close come consider continue cook cost count cover create cut decide depend describe develop die do drink "
         "drive eat enjoy enter expect explain fall feel fight fill find finish fix follow forget give go grow happen hate "
         "have hear help hit hold hope hurt include keep kill know last laugh learn leave let like listen live look lose "
         "love make mean meet move need offer open pay play point produce provide pull push put reach read receive "
         "remember remove report require return run save say see seem sell send set show sing sit sleep speak spend stand "
         "start stay stop study suggest support take talk teach tell think throw touch travel try turn understand use "
         "visit wait walk want watch wear win wish work write").split()


def third(v):
    irr = {"have": "has", "do": "does", "go": "goes"}
    if v in irr: return irr[v]
    if v.endswith(("s", "x", "z", "ch", "sh")): return v + "es"
    if v.endswith("y") and v[-2] not in "aeiou": return v[:-1] + "ies"
    return v + "s"


def ing(v):
    """Gerund: die->dying, see->seeing, make->making, run/stop->running/stopping (CVC doubling,
    single-syllable only - visit/open/travel do not double)."""
    if v.endswith("ie"): return v[:-2] + "ying"
    if v.endswith("ee"): return v + "ing"
    if v.endswith("e") and len(v) > 2 and v != "be": return v[:-1] + "ing"
    dbl = {"stop", "plan", "snap", "spin", "swim", "trip", "shop"}
    if (len(v) == 3 and v[-1] not in "aeiouwxy" and v[-2] in "aeiou" and v[-3] not in "aeiou") or v in dbl:
        return v + v[-1] + "ing"
    return v + "ing"


def tid(vocab, w):
    for p in ("\u0120", "\u2581"):          # GPT-2/Qwen style, SentencePiece/Gemma style
        if p + w in vocab: return vocab[p + w]
    return None


def make_pairs(tok, concept="third"):
    vocab = tok.get_vocab(); pairs, used = [], set()
    for v in VERBS:
        w = third(v) if concept == "third" else ing(v)
        a, b = tid(vocab, v), tid(vocab, w)
        if a is None or b is None or a == b or a in used or b in used: continue
        pairs.append((a, b)); used |= {a, b}
    return np.array(pairs, dtype=np.int64)


_BE = {"I": "am"}      # subject -> be-form for the -ing concept; singular default "is", plural "are"
_PLURAL = {"You", "We", "They", "People", "Students", "Many people", "The workers", "Our customers",
           "These kids", "Most doctors", "The engineers", "Both of them", "Parents", "Farmers", "Voters"}


def make_contexts(rng, n, concept="third"):
    # symmetric templates: same prefixes/adverbs for both groups, only the subject (+be) differs
    # (expanded per EXPERIMENT_REVIEW_AND_FIXES.md section 2.3; keep _SUBJ in steer_compare_v3/v4 in sync)
    prefixes = ["", "Every day, ", "At work, ", "Honestly, ", "Today, ", "In this case, ",
                "Lately, ", "At home, ", "Over time, ", "Usually, "]
    adv = ["usually", "often", "always", "never", "sometimes", "rarely", "really", "also", "just",
           "still", "typically", "generally", "now", ""]
    base_s = ["I", "You", "We", "They", "People", "Students", "Many people", "The workers",
              "Our customers", "These kids", "Most doctors", "The engineers", "Both of them",
              "Parents", "Farmers", "Voters"]
    targ_s = ["He", "She", "It", "The man", "My sister", "The teacher", "This company", "My brother",
              "Our customer", "That kid", "The doctor", "The engineer", "Her mother",
              "The farmer", "The voter", "Everyone"]
    if concept == "ing":
        # target adds an agreeing auxiliary: frame differs from base - ctx/dmd probes are confounded
        # (documented in NEXT_EXPERIMENT_V4_AND_REVIEW.md WP-E); unemb probe is unaffected.
        targ_s = targ_s  # same subjects; the be-form is inserted below
        def sample(subs, with_be):
            allc = [f"{p}{s} {_BE.get(s, 'are' if s in _PLURAL else 'is')} {a}".strip() if with_be
                    else f"{p}{s} {a}".strip() for p in prefixes for s in subs for a in adv]
            rng.shuffle(allc); return allc[:n]
        return sample(base_s, False), sample(targ_s, True)
    def sample(subs):
        allc = [f"{p}{s} {a}".strip() for p in prefixes for s in subs for a in adv]
        rng.shuffle(allc); return allc[:n]
    return sample(base_s), sample(targ_s)


def c4_contexts(model, tok, head, G, y0, y1, rng, n_docs=600, max_pos=128, max_per_doc=5, park_k=3, park_mass=0.7):
    """Region-C extraction: stream C4 'en', one forward per document, keep positions whose
    top-k predicted tokens all lie in one concept group with cumulative mass >= park_mass.
    Returns (E_base, E_target, base_texts, target_texts, base_cluster, target_cluster, rel_err)."""
    import torch
    from datasets import load_dataset
    y0t = torch.as_tensor(np.asarray(y0), dtype=torch.long, device=model.device)
    y1t = torch.as_tensor(np.asarray(y1), dtype=torch.long, device=model.device)
    set0 = set(y0.tolist()); set1 = set(y1.tolist())
    ds = load_dataset("allenai/c4", "en", streaming=True, split="train").shuffle(seed=int(rng.integers(1 << 31)), buffer_size=10_000)
    Eb, Et, tb, tt, cb, ct = [], [], [], [], [], []
    doc_i, scanned = -1, 0
    store = []
    hook = head.register_forward_pre_hook(lambda m, args: store.append(args[0].detach()))
    errs = []
    for ex in ds:
        if rng.random() < 0.5: continue                      # seeded thinning of the stream
        doc_i += 1; scanned += 1
        if doc_i >= n_docs: break
        enc = tok(ex["text"], truncation=True, max_length=max_pos, return_tensors="pt").to(model.device)
        if enc.input_ids.shape[1] < 4: continue
        store.clear()
        with torch.no_grad():
            out = model(**enc)
        if not store: continue
        lam_all = store[-1][0].float()                       # (T, d) hidden states feeding the head
        probs = torch.softmax(out.logits[0].float(), dim=-1)  # (T, V); row i predicts token i+1
        kb = kt = 0
        toks = enc.input_ids[0].tolist()
        for i in range(min(lam_all.shape[0], probs.shape[0]) - 1):   # need a next token to exist
            top = torch.topk(probs[i], park_k)
            ids = top.indices.tolist()
            cum = float(top.values.sum().item())
            lam = lam_all[i].cpu().numpy()
            side = None
            if all(t in set0 for t in ids) and cum >= park_mass: side = 0
            elif all(t in set1 for t in ids) and cum >= park_mass: side = 1
            if side is None: continue
            if side == 0 and kb >= max_per_doc: continue
            if side == 1 and kt >= max_per_doc: continue
            if len(errs) < 5:
                lg = out.logits[0, i].float().cpu().numpy()
                errs.append(float(np.abs(lg - G @ lam).max() / (np.abs(lg).max() + 1e-9)))
            ctx_text = tok.decode(toks[max(0, i - 19): i + 1])      # ~20 trailing tokens
            if side == 0: Eb.append(lam); tb.append(ctx_text); cb.append(doc_i); kb += 1
            else: Et.append(lam); tt.append(ctx_text); ct.append(doc_i); kt += 1
    hook.remove()
    err = float(max(errs)) if errs else float("nan")
    print(f"[c4] scanned {scanned} docs -> base {len(Eb)}, target {len(Et)} candidates "
          f"from {len(set(cb)) + len(set(ct))} docs; logits check err {err:.2e}")
    if not Eb or not Et: raise SystemExit("C4 extraction found no candidates for both groups")
    return (np.stack(Eb), np.stack(Et), tb, tt, cb, ct, err)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--out_dir", required=True)
    ap.add_argument("--dtype", default="float32", choices=["float32", "bfloat16", "float16"])
    ap.add_argument("--load_in_4bit", action="store_true")
    ap.add_argument("--n_per_group", type=int, default=300); ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--concept", default="third", choices=["third", "ing"], help="second concept: verb -> gerund (WP-E)")
    ap.add_argument("--ctx_source", default="templates", choices=["templates", "c4"], help="c4 = region C natural text (WP-D)")
    ap.add_argument("--c4_docs", type=int, default=600); ap.add_argument("--c4_max_pos", type=int, default=128)
    ap.add_argument("--max_per_doc", type=int, default=5)
    a = ap.parse_args()
    outdir = safe_run_dir(a.out_dir)
    import torch, transformers
    from transformers import AutoModelForCausalLM, AutoTokenizer
    rng = np.random.default_rng(a.seed); os.makedirs(outdir, exist_ok=True)
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    dt = getattr(torch, a.dtype)
    tok = AutoTokenizer.from_pretrained(a.model)
    kw = dict(torch_dtype=dt, low_cpu_mem_usage=True)
    if a.load_in_4bit:
        from transformers import BitsAndBytesConfig
        kw["quantization_config"] = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                                       bnb_4bit_compute_dtype=torch.bfloat16)
        kw["device_map"] = {"": 0}
    try:
        model = AutoModelForCausalLM.from_pretrained(a.model, **kw)
    except Exception as e:                                     # Gemma-3 4B ships as a multimodal class
        print("AutoModelForCausalLM failed (", repr(e)[:120], ") -> trying Gemma3ForConditionalGeneration")
        from transformers import Gemma3ForConditionalGeneration
        model = Gemma3ForConditionalGeneration.from_pretrained(a.model, **kw)
    if not a.load_in_4bit: model = model.to(dev)
    model.eval()
    head = model.get_output_embeddings()
    G = head.weight.detach().float().cpu().numpy()
    V, d = G.shape
    pairs = make_pairs(tok, a.concept)
    if a.ctx_source == "c4":
        Eb, Et, tb, tt, cb, ct, err = c4_contexts(model, tok, head, G, pairs[:, 0], pairs[:, 1], rng,
                                                   a.c4_docs, a.c4_max_pos, a.max_per_doc)
        store = []
    else:
        tb, tt = make_contexts(rng, a.n_per_group, a.concept)
        print(f"V={V} d={d} pairs={len(pairs)} contexts={len(tb)}+{len(tt)}")

        store = []
        hook = head.register_forward_pre_hook(lambda m, args: store.append(args[0].detach()))
        errs = []

        def embed(texts, check=False):
            out = []
            with torch.no_grad():
                for i, t in enumerate(texts):
                    store.clear()
                    enc = tok(t, return_tensors="pt").to(model.device)
                    o = model(**enc)
                    lam = store[-1][0, -1].float().cpu().numpy(); out.append(lam)
                    if check and i < 5:
                        lg = o.logits[0, -1].float().cpu().numpy()
                        errs.append(float(np.abs(lg - G @ lam).max() / (np.abs(lg).max() + 1e-9)))
            return np.stack(out)
        Eb = embed(tb, check=True); Et = embed(tt)
        hook.remove()
        err = float(max(errs)) if errs else float("nan")
        cb, ct = None, None
    print(f"[check] logits vs G@lambda relative max error = {err:.2e}   (fp32 model: ~1e-5; bf16/4bit: <~2e-2 is fine)")
    if err > 5e-2: print("  WARNING: output layer has extra ops (softcap/scale/bias). softmax(G@lambda) != model distribution.")

    gdt = np.float32 if V * d < 1e8 else np.float16
    np.save(os.path.join(outdir, "G.npy"), G.astype(gdt)); np.save(os.path.join(outdir, "pairs.npy"), pairs)
    np.save(os.path.join(outdir, "E_base.npy"), Eb.astype(np.float32)); np.save(os.path.join(outdir, "E_target.npy"), Et.astype(np.float32))
    ctx_obj = {"base": tb, "target": tt}
    if cb is not None: ctx_obj["base_cluster"] = cb; ctx_obj["target_cluster"] = ct
    Path(outdir, "contexts.json").write_text(json.dumps(ctx_obj, ensure_ascii=False, indent=1), encoding="utf-8")
    meta = dict(model=a.model, dtype=a.dtype, load_in_4bit=a.load_in_4bit, V=int(V), d=int(d),
                n_pairs=int(len(pairs)), logits_rel_err=err, seed=a.seed, torch=torch.__version__,
                transformers=transformers.__version__, concept=a.concept, ctx_source=a.ctx_source,
                date=datetime.datetime.now().isoformat())
    Path(outdir, "meta.json").write_text(json.dumps(meta, indent=1), encoding="utf-8")
    print("saved to", a.out_dir)


if __name__ == "__main__":
    main()
