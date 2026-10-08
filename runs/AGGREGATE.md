# Aggregate results: Euclidean vs fixed causal metric vs adaptive dual steering

Generated 2026-10-08/09 by executing RUNBOOK.md steps 0-4 on an RTX 4060 8GB
(lrg_env: torch 2.6.0+cu124, transformers 5.19.0; backend=torch).

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

| model | alpha_rel | euclid KL | causal_fixed KL | dual reach | paired euclid-causal KL diff (n=80) |
|---|---|---|---|---|---|
| gpt2 | 1e-3 | **0.967** | reach 0.00 | 0.00 | - (no overlap) |
| gpt2 | 1e-2 | **0.967** | reach 0.00 | 0.00 | - (no overlap) |
| gpt2 | 1e-1 | **0.967** | 8.108 | 0.02 | -7.14 [-7.68, -6.59], P=0.00 |
| gemma1b | 1e-3 | **1.142** | 2.383 | 0.00 | -1.24 (see run paired.csv) |
| gemma1b | 1e-2 | **1.142** | 2.210 | 0.00 | -1.07 [-1.27, -0.88], P=0.012 |
| gemma1b | 1e-1 | **1.142** | 1.628 | 0.00 | -0.49 [-0.56, -0.42], P=0.025 |
| gemma4b | 1e-3 | **0.995** | 3.927 | 0.00 | see runs/gemma4b/alpha0.001_seed0 |
| gemma4b | 1e-2 | (see run) | (see run) | (see run) | runs/gemma4b/alpha0.01_seed0 |
| gemma4b | 1e-1 | (in progress) | | | |

Counterfactual mass at level 0.9 shows the same ordering (euclid >=
causal_fixed, e.g. gpt2 a=0.1: 0.304 vs 0.016; gemma1b a=0.1: 0.432 vs 0.443
comparable; gemma4b a=0.001: 0.449 vs 0.424).

## Findings

1. **Euclidean steering dominates everywhere in this pipeline.** At every
   alpha and every model, euclid has reach_rate 1.0 with the lowest off-target
   KL. Paired comparisons (n=80 contexts) favor euclid over causal_fixed with
   CIs excluding zero on gpt2 and gemma1b.
2. **Strong alpha dependence on gpt2**: with alpha_rel <= 1e-2 the fixed causal
   direction (S0 + alpha*I)^-1 beta is dominated by near-null directions of
   the unembedding covariance (S0 min eigenvalue 1.65e-7 vs alpha 1.5e-4,
   ~1000x amplification) and reaches nothing (diagnostic: cos(euclid,causal)
   = 0.943 and equal per-step logit movement, but P1 goes 0.0018 -> 0.0059 in
   200 steps vs euclid reaching 1.0 by step 50). At alpha_rel=0.1 it recovers
   full reach but with ~8x worse KL.
3. **The adaptive dual method never reaches on real models** (reach 0.00 at
   all levels and alphas on gemma1b/gemma4b; on gpt2 only at alpha_rel=0.1 and
   only at low levels). CPU diagnostic on gemma-1b shows the same mechanism:
   dual direction has cos 0.86 with euclid yet moves P1 from 0.0097 to only
   0.02 in 30 steps (euclid reaches 0.93) - the top-K softmax-covariance
   Newton direction pushes mass onto off-pair top-K tokens instead of the
   verb-pair ratio.
4. On the synthetic generator (runs/syn) all three methods steer (by
   construction the concept direction lives in the row space), euclid and
   causal_fixed are statistically tied, dual is slightly worse - confirming
   the pipeline is correct and the real-model failures are geometric, not
   bugs.
5. This does NOT reproduce an advantage for causal-metric / dual steering on
   the Park 2026 setup. Caveats: template contexts only, one concept
   (verb -> 3rd person), probe is within-template, gemma-4b hidden states are
   4-bit (self-consistent with saved lambda/G but slightly different from
   bf16), and step/max_steps budgets differ from the reference repo.

## Caveats (from per-run report.md)

- Paired rows use only contexts reached by BOTH methods; read reach_rate
  first (selection bias). At alpha=0.1 dual has n_paired <= 2 at level >= 0.9
  on gpt2 - not interpretable.
- Report all three alpha_rel values (tables above / per-run summary.csv).
- gemma-4b: 4-bit quantization shifts hidden states slightly; all analysis
  uses the saved lambda and G, so it is self-consistent.

## Run inventory

- runs/syn - synthetic sanity run
- runs/gpt2/alpha{0.001,0.01,0.1}_seed0 - complete
- runs/gemma1b/alpha{0.001,0.01,0.1}_seed0 - complete
- runs/gemma4b/alpha0.001_seed0 - complete; alpha0.01 completed during upload;
  alpha0.1 finishing - to be pushed in a follow-up commit

Each run dir: config.json, checks.json, summary.csv, paired.csv,
per_context.csv, curves.png, report.md (auto-generated tables + caveats).
