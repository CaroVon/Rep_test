# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=5, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.976

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.328 [0.107,0.575] | 0.530 [0.292,0.764] |
| 0.3 | euclid_unemb | 1.00 | 0.324 [0.111,0.565] | 0.408 [0.220,0.561] |
| 0.3 | causal_unemb | 1.00 | 0.311 [0.103,0.542] | 0.408 [0.238,0.575] |
| 0.3 | dual | 1.00 | 0.461 [0.329,0.598] | 1.818 [0.887,2.901] |
| 0.5 | euclid | 1.00 | 0.327 [0.104,0.579] | 0.657 [0.414,0.899] |
| 0.5 | euclid_unemb | 1.00 | 0.332 [0.116,0.576] | 0.531 [0.333,0.729] |
| 0.5 | causal_unemb | 1.00 | 0.321 [0.106,0.557] | 0.502 [0.321,0.684] |
| 0.5 | dual | 1.00 | 0.413 [0.282,0.519] | 3.435 [1.926,4.963] |
| 0.7 | euclid | 1.00 | 0.344 [0.117,0.576] | 0.773 [0.528,1.043] |
| 0.7 | euclid_unemb | 1.00 | 0.350 [0.128,0.575] | 0.632 [0.463,0.824] |
| 0.7 | causal_unemb | 1.00 | 0.341 [0.127,0.576] | 0.560 [0.390,0.743] |
| 0.7 | dual | 1.00 | 0.376 [0.287,0.464] | 4.723 [2.885,6.335] |
| 0.9 | euclid | 1.00 | 0.400 [0.173,0.635] | 0.965 [0.706,1.224] |
| 0.9 | euclid_unemb | 1.00 | 0.407 [0.192,0.630] | 0.853 [0.727,1.042] |
| 0.9 | causal_unemb | 1.00 | 0.401 [0.179,0.628] | 0.747 [0.620,0.932] |
| 0.9 | dual | 0.40 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.538 [0.346,0.729] | 1.438 [1.129,1.730] |
| 0.99 | euclid_unemb | 1.00 | 0.528 [0.355,0.680] | 1.565 [1.318,1.846] |
| 0.99 | causal_unemb | 1.00 | 0.531 [0.366,0.702] | 1.343 [1.122,1.604] |
| 0.99 | dual | 0.20 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 5 | -1.288 [-2.385,-0.212] | 0.20 |
| 0.3 | euclid_unemb | causal_unemb | 5 | +0.001 [-0.050,+0.044] | 0.60 |
| 0.3 | euclid_unemb | dual | 5 | -1.409 [-2.632,-0.417] | 0.20 |
| 0.3 | causal_unemb | dual | 5 | -1.410 [-2.607,-0.369] | 0.20 |
| 0.3 | euclid | euclid_unemb | 5 | +0.122 [+0.032,+0.212] | 0.80 |
| 0.3 | euclid | causal_unemb | 5 | +0.122 [+0.060,+0.185] | 1.00 |
| 0.5 | euclid | dual | 5 | -2.777 [-4.435,-1.120] | 0.00 |
| 0.5 | euclid_unemb | causal_unemb | 5 | +0.029 [-0.038,+0.090] | 0.60 |
| 0.5 | euclid_unemb | dual | 5 | -2.904 [-4.527,-1.205] | 0.00 |
| 0.5 | causal_unemb | dual | 5 | -2.932 [-4.555,-1.235] | 0.00 |
| 0.5 | euclid | euclid_unemb | 5 | +0.126 [+0.038,+0.234] | 1.00 |
| 0.5 | euclid | causal_unemb | 5 | +0.155 [+0.073,+0.222] | 1.00 |
| 0.7 | euclid | dual | 5 | -3.950 [-5.704,-1.937] | 0.00 |
| 0.7 | euclid_unemb | causal_unemb | 5 | +0.072 [-0.007,+0.117] | 0.80 |
| 0.7 | euclid_unemb | dual | 5 | -4.091 [-5.772,-2.175] | 0.00 |
| 0.7 | causal_unemb | dual | 5 | -4.163 [-5.881,-2.248] | 0.00 |
| 0.7 | euclid | euclid_unemb | 5 | +0.141 [-0.004,+0.299] | 0.60 |
| 0.7 | euclid | causal_unemb | 5 | +0.213 [+0.110,+0.315] | 1.00 |
| 0.9 | euclid | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.9 | euclid_unemb | causal_unemb | 5 | +0.106 [+0.052,+0.166] | 1.00 |
| 0.9 | euclid_unemb | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.9 | causal_unemb | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.9 | euclid | euclid_unemb | 5 | +0.112 [-0.057,+0.343] | 0.60 |
| 0.9 | euclid | causal_unemb | 5 | +0.218 [+0.085,+0.390] | 1.00 |
| 0.99 | euclid | dual | 1 | +nan [+nan,+nan] | 0.00 |
| 0.99 | euclid_unemb | causal_unemb | 5 | +0.222 [+0.140,+0.292] | 1.00 |
| 0.99 | euclid_unemb | dual | 1 | +nan [+nan,+nan] | 0.00 |
| 0.99 | causal_unemb | dual | 1 | +nan [+nan,+nan] | 0.00 |
| 0.99 | euclid | euclid_unemb | 5 | -0.127 [-0.324,+0.209] | 0.20 |
| 0.99 | euclid | causal_unemb | 5 | +0.096 [-0.111,+0.436] | 0.40 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
