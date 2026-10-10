# WP1: step-by-step comparison against KihoPark/dual-steering

Date: 2026-10-09. Reference repo cloned from git@github.com:KihoPark/dual-steering.git
(commit recorded in commands.log; examined files: `03_llm_steering.py`,
`information_geometry/core/metric.py`, `information_geometry/core/geometry.py`,
`information_geometry/steering/method.py`).

Setup for the numerical comparison: gemma-3-1b data (data/gemma1b, G fp16 ->
fp32 on cuda), first held-out test context lambda_0 (||lambda_0|| = 107.8),
Dual MD probe beta^Phi = mean(phi(lambda_target,train)) - mean(phi(lambda_base,train))
computed identically for both sides, alpha = 5e-3, top-K = 20000, 20 CG
iterations, torch fp32 throughout.

## 1. First-step direction

| comparison | cosine |
|---|---|
| ours `TorchOps.dual_dir` (raw probe, as in production) vs author's `cg_solve` | 1.000000 |
| ours `dual_dir` (normalized probe) vs author's `cg_solve` | 1.000000 |

Pass criterion (cosine >= 0.99): **PASS**.

## 2. 20-step trajectory (same step size 2.0 = author's `m_steering` default)

| step | author P1 | ours P1 | author H | ours H |
|---|---|---|---|---|
| 0 | 0.0015 | 0.0015 | 4.1561 | 4.1561 |
| 5 | 0.1317 | 0.1317 | 4.5465 | 4.5465 |
| 10 | 0.7869 | 0.7869 | 4.7999 | 4.7999 |
| 15 | 0.9834 | 0.9834 | 4.5894 | 4.5894 |
| 20 | 0.9981 | 0.9981 | 4.4787 | 4.4787 |

Max relative difference of P(W=1) over 20 steps: 4.8e-06. Max abs entropy
difference: 1.4e-05. Pass criterion (relative diff <= 5%): **PASS**.

Raw data: `repro_check_data.json`, `repro_check_traj.json`.

## 3. Algorithm-level findings

Identical by construction (verified line by line AND numerically):

- metric operator: `G_top^T (p * (G_top x)) - mu (mu.x) + alpha x` with
  top-K = `torch.topk(logits, 20000)`, `softmax` over the top-K values,
  `mu = p @ G_top` - same in both.
- CG solver structure, 20 iterations, tol 1e-5 (author: absolute on ||r||,
  ours: relative to ||b||; coincides here because the author normalizes the
  probe before solving, and we verified both raw and normalized probes give
  cosine 1.000000).
- Dual MD probe: author's `primals_to_duals` = softmax(G lambda) @ G = our
  `ops.phi`; the dmd probe in `steer_compare_v3.py` matches their
  `get_MD(train_duals0, train_duals1)`.

Differences (configuration, NOT implementation):

| item | author | ours | impact |
|---|---|---|---|
| m_steering step size | absolute 2.0 | eta = step_frac * ||lambda_0|| = 0.01 * 107.8 = 1.08 | ours takes ~2x more steps; per-step dynamics identical (verified above at matched step size) |
| stop rule | P1 > 0.9999 | P1 >= 0.99 (levels[-1]) | ours stops earlier; paired comparisons are per-level so this only truncates paths |
| KL metric | q*(log(q+5e-3) - log(p+5e-3)), offset 5e-3 | KL over (pair mass + neutral) with 1e-12 floor | different tail weighting; do not compare our absolute KL numbers to theirs |
| rank metric | union of top-0.999 sets across 20 sampled steps | simplified: top-0.99 set at the start only (documented in AGGREGATE as a deviation) | our `rd` is a lower-bound variant |
| e_steering step | absolute 0.5 | same eta as all methods | - |

Bugs found in the author's shipped code (reported, not fixed on our side):

- `information_geometry/steering/method.py` uses `F.softmax` in
  `m_steering` but never imports `torch.nn.functional as F` -
  NameError on call. Worked around in this check by injecting the module
  (`igm.F = F`). Upstream fix is a one-line import.

## 4. Verdict

The implementations are numerically equivalent (cosine 1.000000; trajectory
agreement to ~5e-6). The V2 observation "dual at alpha=5e-3 has ~3x the
off-target KL of euclid on the ctx probe" is therefore a property of the
setting (probe, step size, contexts, KL definition), not of our
implementation. G0's WP1 criterion is met.

## Addendum (V4, 2026-10-10)

- Region-C re-verification (task-doc decision-tree requirement for the
  C1-reversal branch): first-step direction cosine vs the author's cg_solve on
  a natural-text (C4, Park-filtered) context = **1.000000**
  (repro_check_c4.json / repro_check_c4.txt). Implementation equivalence
  extends beyond template contexts.
- Author notification about the missing `import torch.nn.functional as F` in
  `information_geometry/steering/method.py`: **not yet sent**. Recommended
  channel: GitHub issue on KihoPark/dual-steering with the one-line fix and
  the cosine-1.000000 equivalence table above as evidence. No e-mail or
  account channel is available from this execution environment.
