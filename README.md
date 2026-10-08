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

See **`runs/AGGREGATE.md`** for the v1 aggregate tables, guardrail checks,
and scope-limited findings, and **`runs/AGGREGATE_V2.md`** for the follow-up
experiments prescribed by `EXPERIMENT_REVIEW_AND_FIXES.md` (absolute-alpha
sweep, Park 2024 recipe, Sigma_t spectrum diagnostics, cluster bootstrap,
entropy diagnostics). Summary of the corrected picture:

- v1 (relative alpha = alpha_rel * tr(S0)/d): euclid looks best, dual never
  reaches - but the absolute alphas were 2-4 orders of magnitude below Park
  2026's 5e-3, so v1 could not test the published methods (see the review).
- v2 (absolute alpha): dual reaches reliably for alpha_abs >= 5e-3; Park
  2024's recipe (causal_unemb: Cov^-1 applied to the mean unembedding
  difference) is the strongest direction on BOTH gpt2 (KL 0.73 vs euclid
  0.95 at level 0.9) and gemma-3-1b (KL 0.96 vs 1.12), with full reach, ~2x
  fewer steps than euclid, and it lowers distribution entropy while
  steering; the improvement over the raw unembedding direction is
  significant under cluster bootstrap (+0.082 [+0.047, +0.115]).

## Repository layout

```
RUNBOOK.md               experiment protocol (steps, guardrails, output spec)
EXPERIMENT_REVIEW_AND_FIXES.md  design review of the v1 runs (in Chinese)
extract_embeddings.py    stage 1: save G, verb pairs, context lambdas from an HF model
steer_compare.py         stage 2: 3-method comparison, selftest, synthetic mode
steer_compare_v2.py      stage 2 v2: absolute alpha, Park 2024 recipe, diagnostics
run_all.sh               extract + alpha sweep wrapper
runs/<tag>/<run>/        per-run outputs (summary/paired/per_context/final CSVs,
                         checks/config JSONs, curves.png, report.md)
runs/AGGREGATE.md        v1 cross-run aggregate report
runs/AGGREGATE_V2.md     v2 follow-up report (absolute alpha, Park 2024 recipe)
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
