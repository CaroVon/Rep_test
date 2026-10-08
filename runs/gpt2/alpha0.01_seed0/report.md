# Steering comparison: gpt2

backend=torch, V=50257, d=768, pairs=143, steered contexts=80, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=6.392812679223425e-07, probe held-out AUC=0.931, cos(euclid,causal)=0.943

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.193 [0.169,0.219] | 0.671 [0.628,0.716] |
| 0.3 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.198 [0.172,0.223] | 0.773 [0.726,0.820] |
| 0.5 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.224 [0.196,0.252] | 0.847 [0.800,0.893] |
| 0.7 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.304 [0.273,0.336] | 0.967 [0.923,1.016] |
| 0.9 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.497 [0.470,0.524] | 1.427 [1.350,1.506] |
| 0.99 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
