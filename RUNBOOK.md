# Runbook: Euclidean vs fixed causal metric vs adaptive dual steering (RTX 4060 8GB)

## 0. What is tested vs untested
- TESTED (synthetic data, CPU): numpy backend, all logic, all output files, selftest.
- NOT TESTED by the author: `extract_embeddings.py` (needs HF models), torch/GPU backend. Run `--selftest` first.

## 1. Repos
| repo | use |
|---|---|
| https://github.com/KihoPark/dual-steering | reference implementation of Park 2026 (Gemma-3-4B, MetaCLIP-2): cross-check, token-pair JSONs, their metrics |
| https://github.com/KihoPark/linear_rep_geometry | Park 2024 code (causal inner product); reference only |
| https://github.com/sambowyer/no_clt_paper | optional: small-n confidence intervals (Bowyer et al.) |
Your own scripts: extract_embeddings.py, steer_compare.py, run_all.sh (this folder).

## 2. Environment
python>=3.10; install torch (CUDA build from pytorch.org), then:
  pip install numpy matplotlib transformers accelerate bitsandbytes
Gemma models are gated: accept the license on the model page, then `huggingface-cli login`.

## 3. Steps (do in order; stop when you have enough for the meeting)
0. python steer_compare.py --selftest            # expect "SELFTEST PASS" for numpy (and torch if present)
   python steer_compare.py --synthetic --out runs/syn
1. python extract_embeddings.py --model gpt2 --dtype float32 --out_dir data/gpt2
   -> check printed "[check] logits vs G@lambda relative max error" (~1e-5)
   python steer_compare.py --data_dir data/gpt2 --alpha_rel 0.01 --seed 0 --out runs/gpt2/alpha0.01_seed0
2. bash run_all.sh gpt2 gpt2 "--dtype float32" "--topk 5000"      # alpha sweep 1e-3,1e-2,1e-1
3. bash run_all.sh google/gemma-3-1b-pt gemma1b "--dtype bfloat16" "--topk 20000 --backend torch"
4. (optional) bash run_all.sh google/gemma-3-4b-pt gemma4b "--dtype bfloat16 --load_in_4bit" "--topk 20000 --backend torch"
Time a run first: --n_ctx 10 --max_steps 100. Runtime scales with n_ctx x steps x (3 methods); V=262k models need the torch/GPU backend.

## 4. VRAM / RAM
- gpt2: <1GB. gemma-3-1b bf16 extraction ~2-3GB. gemma-3-4b 4-bit extraction ~3-4GB (bf16 does NOT fit 8GB).
- Stage 2 holds G on GPU in fp32: gemma-1b ~1.2GB, gemma-4b ~2.7GB (stage 1 process has already exited).
- Host RAM: 16GB recommended for gemma-4b.
- 4-bit model => hidden states differ slightly from bf16; all analysis uses the saved lambda and G, so it is self-consistent, but state this caveat.

## 5. Output format (runs/<tag>/<run>/)
config.json   args, backend, V, d, n_pairs, model meta, versions, runtime
checks.json   logits_rel_err, probe_heldout_auc, n_*_raw/kept, n_steered, cos_euclid_causal, alpha
summary.csv   model,method,level,n_start,n_reached,reach_rate,cf_mean,cf_lo,cf_hi,kl_mean,kl_lo,kl_hi,steps_mean
paired.csv    level,a,b,n_paired,kl_diff_mean,kl_diff_lo,kl_diff_hi,win_b_lower_kl,cf_diff_mean,cf_diff_lo,cf_diff_hi
              (diff = a - b; >0 means b has lower KL / mass leakage)
per_context.csv ctx_id,text,method,level,reached,step,P1,cf,kl
curves.png    counterfactual mass and off-target KL vs target prob, 95% bootstrap CI
report.md     auto-generated tables + caveats
data/<tag>/   G.npy (fp32 or fp16), pairs.npy, E_base.npy, E_target.npy, contexts.json, meta.json
CIs: percentile bootstrap over contexts (2000 resamples). cf = counterfactual mass; kl = KL(P^Z_0 || P^Z_t) over pair-level and neutral tokens.

## 6. Interpretation guardrails
- Always read reach_rate before paired.csv; paired rows use only contexts reached by BOTH methods.
- If checks.json logits_rel_err > 5e-2 or probe AUC < 0.8: stop, the comparison is not meaningful.
- Report all three alpha_rel values.

## 7. Aggregate several runs
python - <<'PY'
import pandas as pd, glob
df = pd.concat([pd.read_csv(f).assign(run=f.split('/')[-2]) for f in glob.glob('runs/gpt2/*/summary.csv')])
print(df[df.level==0.9].pivot(index='run', columns='method', values=['reach_rate','kl_mean']))
PY
