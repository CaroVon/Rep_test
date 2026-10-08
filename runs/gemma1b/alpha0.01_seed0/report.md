# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=80, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.886

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.344 [0.296,0.388] | 0.679 [0.569,0.805] |
| 0.3 | causal_fixed | 1.00 | 0.346 [0.302,0.392] | 1.029 [0.867,1.205] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.343 [0.298,0.389] | 0.816 [0.695,0.945] |
| 0.5 | causal_fixed | 1.00 | 0.323 [0.278,0.369] | 1.321 [1.130,1.527] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.365 [0.316,0.412] | 0.942 [0.817,1.086] |
| 0.7 | causal_fixed | 1.00 | 0.316 [0.271,0.363] | 1.641 [1.427,1.866] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.432 [0.384,0.481] | 1.142 [1.019,1.297] |
| 0.9 | causal_fixed | 1.00 | 0.328 [0.281,0.376] | 2.210 [1.954,2.481] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.566 [0.523,0.610] | 1.660 [1.521,1.820] |
| 0.99 | causal_fixed | 1.00 | 0.351 [0.298,0.403] | 3.465 [3.138,3.804] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | causal_fixed | 80 | -0.350 [-0.432,-0.276] | 0.01 |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | causal_fixed | 80 | -0.505 [-0.619,-0.404] | 0.01 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 80 | -0.700 [-0.844,-0.572] | 0.01 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 80 | -1.069 [-1.271,-0.883] | 0.01 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 80 | -1.804 [-2.072,-1.556] | 0.01 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
