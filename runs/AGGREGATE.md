# Aggregate results: Euclidean vs fixed causal metric vs adaptive dual steering

Generated 2026-10-08/09 by executing RUNBOOK.md steps 0-4 on an RTX 4060 8GB
(lrg_env: torch 2.6.0+cu124, transformers 5.19.0; backend=torch).
See EXPERIMENT_REVIEW_AND_FIXES.md for a design review of these runs and
steer_compare_v2.py + runs/*_v2/ for the follow-up experiments it prescribes.

Selftest: numpy and torch backends both PASS (CG vs exact solve cos = 1.0000,
identical steering paths across backends).

## Guardrail checks (RUNBOOK section 6 - all passed)

| run | logits_rel_err (max 5e-2) | probe AUC (min 0.8) | n_steered |
|---|---|---|---|
| synthetic | 0.0 | 1.000 | 19 |
| gpt2 (all alphas) | 6.4e-07 | 0.931 | 80 |
| gemma1b (all alphas) | 2.9e-03 | 1.000 | 80 |
| gemma4b (all alphas) | 3.5e-03 | 1.000 | 80 |

Data: gpt2 V=50257 d=768; gemma-3-1b V=262144 d=1152; gemma-3-4b (4-bit)
V=262208 d=2560. All models: 143-144 single-token verb pairs (base vs 3rd
person), 300+300 template contexts, 80 steered contexts, max_steps=600,
seed=0, topk=5000 (gpt2) / 20000 (gemma).

## Headline table: reach_rate and off-target KL at level P1 = 0.9

alpha = alpha_rel * tr(S0)/d (RELATIVE calibration; see Finding 3 - this
turns out to be far below Park 2026's absolute alpha=5e-3).

| model | alpha_rel | euclid KL | causal_fixed KL | dual reach | paired euclid-causal KL diff (n=80) |
|---|---|---|---|---|---|
| gpt2 | 1e-3 | 0.967 | reach 0.00 | 0.00 | no overlap |
| gpt2 | 1e-2 | 0.967 | reach 0.00 | 0.00 | no overlap |
| gpt2 | 1e-1 | 0.967 | 8.108 | 0.02 | -7.14 [-7.68, -6.59], frac causal lower = 0.00 |
| gemma1b | 1e-3 | 1.142 | 2.383 | 0.00 | -1.24 (run paired.csv) |
| gemma1b | 1e-2 | 1.142 | 2.210 | 0.00 | -1.07 [-1.27, -0.88], frac causal lower = 0.012 |
| gemma1b | 1e-1 | 1.142 | 1.628 | 0.00 | -0.49 [-0.56, -0.42], frac causal lower = 0.025 |
| gemma4b | 1e-3 | 0.995 | 3.927 | 0.00 | run paired.csv |
| gemma4b | 1e-2 | 0.995 | 3.820 | 0.00 | run paired.csv |
| gemma4b | 1e-1 | 0.995 | 3.069 | 0.00 | -2.07 [-2.28, -1.87], frac causal lower = 0.00 |

Note: the "frac X lower" column is the fraction of paired contexts where the
second method has lower KL (a win rate), NOT a p-value. Counterfactual mass
at level 0.9 shows the same ordering (e.g. gpt2 a=0.1: euclid 0.304 vs
causal_fixed 0.016; gemma4b a=0.1: 0.449 vs 0.461).

## Findings (v1 runs, scope-limited)

1. **Within this configuration** (template contexts, alpha_rel in [1e-3,
   1e-1] under the tr(S0)/d calibration, context-mean-difference probe), the
   Euclidean direction has reach_rate 1.0 on all models with the lowest
   off-target KL.
2. Strong alpha dependence on gpt2: with alpha_rel <= 1e-2 the fixed-causal
   direction (S0 + alpha*I)^-1 beta reaches nothing (S0 min eigenvalue
   1.65e-7 vs alpha 1.5e-4). At alpha_rel=0.1 it recovers full reach with
   ~8x worse KL. causal_fixed also needs 2-4x more steps than euclid to
   reach 0.9 on the gemma models (gemma-1b ~70 vs 38 steps; gemma-4b ~180
   vs 49).
3. **The adaptive dual method reaches no level on the real models under the
   alphas swept here.** Our absolute alphas (about 1e-7 .. 1e-4) are 2-4
   orders of magnitude below Park 2026's reported 5e-3, so this result does
   NOT constitute a test of their method. The near-null-eigendirection
   amplification / entropy-rise account is a working hypothesis verified on
   single contexts only (see v2 sigma_t_diag and final.csv for the
   multi-context check).
4. On the synthetic generator all three methods steer; euclid and
   causal_fixed are statistically tied, dual slightly worse.
5. **These runs did not test Park 2024's original recipe** (Cov^-1 applied
   to the mean unembedding difference - see v2 methods euclid_unemb /
   causal_unemb) and did not align Park 2026's alpha magnitude or context
   filtering. No conclusion can be drawn about the relative merit of either
   published method from the v1 runs alone.

## v2 follow-up (per EXPERIMENT_REVIEW_AND_FIXES.md)

- Backend parity: numpy vs torch on synthetic - reach identical, KL means
  agree to 1e-5 (runs/syn_np, runs/syn_torch).
- Probe agreement: cos(beta, gbar) ~ 0.48 on gemma-1b - the context probe and
  the unembedding-difference probe are substantially different directions;
  compare them separately, do not pool.
- Absolute-alpha sweep on gemma-1b (runs/gemma1b_v2/abs*) and gpt2 ridge
  sensitivity (runs/gpt2_v2/ridge*): see runs/AGGREGATE_V2.md.

## Caveats (from per-run report.md)

- Paired rows use only contexts reached by BOTH methods; read reach_rate
  first (selection bias).
- Template contexts cluster by subject; v1 CIs treat them as independent and
  are therefore too narrow (v2 adds cluster bootstrap by subject).
- Report all three alpha_rel values (tables above / per-run summary.csv).
- gemma-4b: 4-bit quantization shifts hidden states slightly; all analysis
  uses the saved lambda and G, so it is self-consistent, but it is not
  strictly the same model as Park's bf16.
- Probe is trained on templates; AUC is held-out within the same templates.

## Run inventory

- runs/syn - synthetic sanity run (v1)
- runs/gpt2/alpha{0.001,0.01,0.1}_seed0 - complete (v1)
- runs/gemma1b/alpha{0.001,0.01,0.1}_seed0 - complete (v1)
- runs/gemma4b/alpha{0.001,0.01,0.1}_seed0 - complete (v1)
- runs/syn_np, runs/syn_torch - v2 backend-parity checks
- runs/gemma1b_v2/abs* - v2 absolute-alpha sweep on gemma-1b
- runs/gpt2_v2/ridge* - v2 ridge sensitivity for causal_unemb on gpt2

Each run dir: config.json, checks.json, summary.csv, paired.csv,
per_context.csv (+ final.csv in v2), curves.png, report.md.
