# Rep_test - Steering geometry comparison

Comparison of three steering direction rules for causal language models,
executed per `RUNBOOK.md` on an RTX 4060 8GB:

- **euclid**: v = beta (probe mean-difference direction)
- **causal_fixed**: v = (S0 + a*I)^-1 beta, S0 = uniform covariance of
  unembedding rows (Park 2024-style causal metric, frozen)
- **dual**: v = (S_t + a*I)^-1 beta, S_t = softmax-weighted top-K covariance
  at the current point (Park 2026-style adaptive dual steering)

All methods share the probe, step norm, and stopping rule; only the direction
differs. Metrics: reach_rate of target probability levels, counterfactual
(pair) mass, and off-target KL divergence, with 2000-resample bootstrap CIs
over contexts.

## Results

See **`runs/AGGREGATE.md`** for the aggregate tables, guardrail checks,
findings, and caveats. Summary: Euclidean steering dominates on gpt2,
gemma-3-1b (bf16), and gemma-3-4b (4-bit) across alpha_rel in {1e-3, 1e-2,
1e-1}; causal_fixed reaches on gemma but with consistently higher off-target
KL; the adaptive dual method fails to reach on real models in this pipeline
(mechanism diagnosed in `runs/AGGREGATE.md`).

## Repository layout

```
RUNBOOK.md               experiment protocol (steps, guardrails, output spec)
extract_embeddings.py    stage 1: save G, verb pairs, context lambdas from an HF model
steer_compare.py         stage 2: 3-method comparison, selftest, synthetic mode
run_all.sh               extract + alpha sweep wrapper
runs/<tag>/<run>/        per-run outputs (summary/paired/per_context CSVs,
                         checks/config JSONs, curves.png, report.md)
runs/AGGREGATE.md        cross-run aggregate report
data/                    NOT committed (G.npy up to 1.3 GB; regenerate locally)
```

## Reproduce

```bash
python steer_compare.py --selftest
python steer_compare.py --synthetic --out runs/syn
bash run_all.sh gpt2 gpt2 "--dtype float32" "--topk 5000"
bash run_all.sh google/gemma-3-1b-pt gemma1b "--dtype bfloat16" "--topk 20000 --backend torch"
bash run_all.sh google/gemma-3-4b-pt gemma4b "--dtype bfloat16 --load_in_4bit" "--topk 20000 --backend torch"
```

Gemma models are gated: accept the license on the model page and authenticate
(`hf auth login`). Embeddings are extracted once into `data/<tag>/` and reused
by all steering runs.

## Environment used

Python 3.12.3, torch 2.6.0+cu124, transformers 5.19.0, accelerate 1.15.0,
bitsandbytes 0.50.2, numpy 2.5.x, matplotlib 3.11.x; CUDA driver 13.1.

## Status

Steps 0-4 of RUNBOOK.md executed 2026-10-08/09; the gemma-3-4b alpha=0.1 run
was still finishing when this snapshot was pushed (see `runs/AGGREGATE.md`
run inventory).
