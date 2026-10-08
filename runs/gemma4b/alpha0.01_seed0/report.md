# Steering comparison: google/gemma-3-4b-pt

backend=torch, V=262208, d=2560, pairs=144, steered contexts=80, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.00348491407930851, probe held-out AUC=1.000, cos(euclid,causal)=0.839

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.358 [0.316,0.400] | 0.554 [0.473,0.636] |
| 0.3 | causal_fixed | 1.00 | 0.463 [0.421,0.505] | 1.348 [1.176,1.534] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.357 [0.317,0.399] | 0.679 [0.597,0.772] |
| 0.5 | causal_fixed | 1.00 | 0.446 [0.406,0.487] | 1.849 [1.643,2.080] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.379 [0.335,0.421] | 0.796 [0.712,0.887] |
| 0.7 | causal_fixed | 1.00 | 0.437 [0.395,0.476] | 2.502 [2.260,2.782] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.449 [0.405,0.494] | 0.995 [0.910,1.081] |
| 0.9 | causal_fixed | 1.00 | 0.429 [0.386,0.470] | 3.820 [3.498,4.153] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.582 [0.542,0.620] | 1.523 [1.424,1.637] |
| 0.99 | causal_fixed | 1.00 | 0.407 [0.361,0.455] | 6.609 [6.164,7.050] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | causal_fixed | 80 | -0.794 [-0.907,-0.679] | 0.00 |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | causal_fixed | 80 | -1.169 [-1.323,-1.023] | 0.00 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 80 | -1.706 [-1.908,-1.519] | 0.00 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 80 | -2.825 [-3.095,-2.563] | 0.00 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 80 | -5.086 [-5.479,-4.682] | 0.00 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
