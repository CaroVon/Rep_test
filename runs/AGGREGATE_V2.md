# V2 aggregate: absolute-alpha sweep, Park 2024 recipe, diagnostics (per EXPERIMENT_REVIEW_AND_FIXES.md)

All runs on the same extracted data as v1 (gemma-3-1b bf16, gpt2 fp32; see
runs/AGGREGATE.md). Script: steer_compare_v2.py. CIs: cluster bootstrap by
template subject (8-9 clusters on gemma-1b; intervals are correspondingly
coarse and should be read as order-of-magnitude, not precise).

## 1. Backend parity (review step 1)

selftest PASS on both backends; synthetic np vs torch: reach identical, KL
means agree to 1e-5 (runs/syn_np, runs/syn_torch). The three previously
untested torch operators (pair_diff_mean, entropy, sigma_spec) are correct.

## 2. Absolute-alpha sweep on gemma-3-1b (review section 2.1; 20 contexts, level 0.9)

| alpha_abs | alpha/mean_eig(S0) | frac eig(Sigma_t)>alpha | dual reach | dual KL | euclid KL | euclid_unemb KL | causal_unemb KL |
|---|---|---|---|---|---|---|---|
| 1e-4 | 0.11 | 0.234 | 0.0 | - | 1.120 | 1.042 | **0.960** |
| 1e-3 | 1.1 | 0.075 | 0.3 | 5.95 | 1.120 | 1.042 | **0.960** |
| 5e-3 (Park) | 5.6 | 0.029 | 1.0 | 3.31 | 1.120 | 1.042 | **0.960** |
| 2e-2 | 22 | 0.009 | 1.0 | 1.32 | 1.120 | 1.042 | **0.960** |
| 1e-1 | 112 | 0.001 | 1.0 | 1.02 | 1.120 | 1.042 | **0.960** |

Findings:

- **dual's failure in v1 was an alpha-magnitude artifact.** Reach goes
  0 -> 0.3 -> 1.0 as alpha_abs passes ~5e-3 - i.e. exactly at Park 2026's
  reported value. The v1 relative calibration (alpha = alpha_rel * tr(S0)/d)
  put us 2-4 orders of magnitude below it.
- **causal_unemb (Park 2024 recipe) is the best direction at every alpha**
  on gemma-1b: KL 0.960 < euclid_unemb 1.042 < euclid 1.120, with ~19 steps
  to 0.9 (euclid needs ~38). The three fixed directions are alpha-independent
  by construction (only dual uses alpha), which is why their columns repeat.
- dual improves monotonically with alpha (KL 5.9 -> 1.0) but does not beat
  causal_unemb anywhere in the sweep; at 1e-1 it roughly matches euclid.
- Steps-to-0.9 for dual: 511 (alpha 1e-3, when it reaches at all) -> 166
  (5e-3) -> 71 (2e-2) -> 45 (1e-1).

Paired comparisons (cluster bootstrap, 20 contexts, alpha-independent):

- euclid vs causal_unemb at 0.9: KL diff +0.159 [-0.022, +0.351],
  frac contexts where causal_unemb lower = 0.75. Direction favours
  causal_unemb; with only 8-9 subject clusters the CI still touches zero.
- euclid_unemb vs causal_unemb at 0.9: +0.082 [+0.047, +0.115], frac = 0.90
  - the Cov^-1 pre-multiplication significantly improves on the raw
  unembedding-difference direction.

## 3. Mechanism check via final.csv (review sections 2.1/2.5)

Mean over 20 starting contexts (gemma-1b):

| method (alpha) | P1_end | H_start | H_end |
|---|---|---|---|
| dual (1e-4, stuck) | 0.096 | 4.054 | 4.009 |
| dual (1e-3, partial) | 0.820 | 4.054 | 4.276 |
| euclid (1e-4) | 0.991 | 4.054 | 4.320 |
| euclid_unemb (1e-4) | 0.992 | 4.054 | 3.714 |
| causal_unemb (1e-4) | 0.992 | 4.054 | 3.694 |

The v1 working hypothesis (near-null directions amplified, entropy rises
while the target barely moves) is supported in aggregate at alpha 1e-3
(entropy +0.22 while P1 only 0.82 after ~580 steps). The unembedding-space
directions do the opposite: they RE-CONCENTRATE the distribution
(entropy 4.05 -> 3.69/3.71) while reaching the target, which is why their
off-target KL is lower.

## 4. gpt2 ridge sensitivity for causal_unemb (review section 2.2; 20 contexts, level 0.9)

| ridge_rel | causal_unemb KL | steps | (euclid KL = 0.946 for reference) |
|---|---|---|---|
| 1e-8 | 0.725 | 49.1 | |
| 1e-6 | 0.728 | 45.4 | |
| 1e-4 | 0.786 | 8.0 | |

**causal_unemb beats euclid on gpt2 as well** (0.725-0.786 vs 0.946) with
full reach at every level and every ridge value; the conclusion is not an
artifact of the ridge (smaller ridge = more steps but slightly lower KL).
euclid_unemb on gpt2: KL 1.270, fastest (~2 steps), worst leakage of the
three.

## 5. Step/budget control (review section 2.7)

gemma-1b, alpha_abs 5e-3, step_frac 0.02, max_steps 1200 vs defaults:
reach 1.0 everywhere; KL essentially unchanged (dual 3.29 vs 3.31, others
within 0.08); steps halve. The ranking is robust to the budget choice.

## 6. Probe agreement

cos(beta, gbar) = 0.476 on gemma-1b: the context-mean-difference probe and
the unembedding-difference probe are substantially different directions
(~61 degrees). Comparisons across the two probe families are reported
separately and should not be pooled.

## 7. Conclusions relative to the review

- v1's "dual never reaches" is explained and quantified: absolute alpha was
  2-4 orders of magnitude below Park 2026's 5e-3. At >= 5e-3 dual reaches
  reliably (review section 2.1 acceptance criterion met: reach clearly > 0
  in a wide interval around 5e-3).
- Park 2024's recipe (causal_unemb) is the strongest fixed direction tested
  on both gpt2 and gemma-1b: lowest off-target KL, full reach, few steps,
  and it lowers distribution entropy while steering.
- Because dual now reaches, the review's section 2.8 (line-by-line
  comparison against KihoPark/dual-steering) is not triggered by its own
  criterion ("if dual still reaches 0 near 5e-3"). It remains the right next
  step if a faithful replication of Park 2026's full setting is attempted,
  together with the review's section 2.3 context changes (C4-like natural
  text, tighter filtering, expanded symmetric subject lists) which were NOT
  applied here.
- Remaining caveats: template contexts (one concept), 8-9 subject clusters
  (coarse CIs), gemma-4b v1 runs only (4-bit), no multi-seed replication.
