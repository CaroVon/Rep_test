# Steering comparison: google/gemma-3-4b-pt

backend=torch, V=262208, d=2560, pairs=144, steered contexts=80, alpha_rel=0.001, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.00348491407930851, probe held-out AUC=1.000, cos(euclid,causal)=0.833

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.358 [0.316,0.400] | 0.554 [0.473,0.636] |
| 0.3 | causal_fixed | 1.00 | 0.463 [0.422,0.506] | 1.388 [1.211,1.582] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.357 [0.317,0.399] | 0.679 [0.597,0.772] |
| 0.5 | causal_fixed | 1.00 | 0.445 [0.405,0.486] | 1.906 [1.695,2.143] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.379 [0.335,0.421] | 0.796 [0.712,0.887] |
| 0.7 | causal_fixed | 1.00 | 0.435 [0.393,0.473] | 2.574 [2.324,2.860] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.449 [0.405,0.494] | 0.995 [0.910,1.081] |
| 0.9 | causal_fixed | 1.00 | 0.424 [0.380,0.465] | 3.927 [3.594,4.267] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.582 [0.542,0.620] | 1.523 [1.424,1.637] |
| 0.99 | causal_fixed | 1.00 | 0.400 [0.354,0.448] | 6.759 [6.308,7.209] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | causal_fixed | 80 | -0.834 [-0.951,-0.713] | 0.00 |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | causal_fixed | 80 | -1.226 [-1.387,-1.074] | 0.00 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 80 | -1.778 [-1.986,-1.583] | 0.00 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 80 | -2.932 [-3.209,-2.659] | 0.00 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 80 | -5.235 [-5.642,-4.823] | 0.00 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
