# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=80, alpha_rel=0.1, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.912

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.344 [0.296,0.388] | 0.679 [0.569,0.805] |
| 0.3 | causal_fixed | 1.00 | 0.378 [0.335,0.421] | 0.854 [0.726,0.993] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.343 [0.298,0.389] | 0.816 [0.695,0.945] |
| 0.5 | causal_fixed | 1.00 | 0.372 [0.328,0.418] | 1.054 [0.918,1.207] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.365 [0.316,0.412] | 0.942 [0.817,1.086] |
| 0.7 | causal_fixed | 1.00 | 0.387 [0.341,0.431] | 1.258 [1.109,1.414] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.432 [0.384,0.481] | 1.142 [1.019,1.297] |
| 0.9 | causal_fixed | 1.00 | 0.443 [0.401,0.486] | 1.628 [1.460,1.802] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.566 [0.523,0.610] | 1.660 [1.521,1.820] |
| 0.99 | causal_fixed | 1.00 | 0.559 [0.520,0.595] | 2.537 [2.335,2.745] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | causal_fixed | 80 | -0.175 [-0.209,-0.142] | 0.06 |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | causal_fixed | 80 | -0.238 [-0.282,-0.196] | 0.05 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 80 | -0.316 [-0.370,-0.266] | 0.04 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 80 | -0.486 [-0.556,-0.417] | 0.03 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 80 | -0.877 [-0.987,-0.766] | 0.03 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
