# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=20, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.915

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.364 [0.297,0.455] | 0.660 [0.524,0.796] |
| 0.3 | euclid_unemb | 1.00 | 0.353 [0.288,0.437] | 0.540 [0.433,0.637] |
| 0.3 | causal_unemb | 1.00 | 0.329 [0.271,0.405] | 0.590 [0.458,0.715] |
| 0.3 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.5 | euclid | 1.00 | 0.362 [0.295,0.453] | 0.799 [0.645,0.942] |
| 0.5 | euclid_unemb | 1.00 | 0.359 [0.297,0.444] | 0.658 [0.540,0.777] |
| 0.5 | causal_unemb | 1.00 | 0.337 [0.276,0.414] | 0.678 [0.538,0.804] |
| 0.5 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid | 1.00 | 0.384 [0.313,0.475] | 0.922 [0.740,1.093] |
| 0.7 | euclid_unemb | 1.00 | 0.386 [0.328,0.473] | 0.776 [0.674,0.904] |
| 0.7 | causal_unemb | 1.00 | 0.365 [0.305,0.441] | 0.767 [0.622,0.929] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid | 1.00 | 0.454 [0.386,0.547] | 1.120 [0.921,1.317] |
| 0.9 | euclid_unemb | 1.00 | 0.454 [0.402,0.524] | 1.042 [0.901,1.247] |
| 0.9 | causal_unemb | 1.00 | 0.439 [0.383,0.512] | 0.960 [0.806,1.175] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.593 [0.534,0.664] | 1.630 [1.387,1.883] |
| 0.99 | euclid_unemb | 1.00 | 0.568 [0.539,0.610] | 1.720 [1.514,2.011] |
| 0.99 | causal_unemb | 1.00 | 0.562 [0.531,0.612] | 1.514 [1.304,1.828] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid_unemb | causal_unemb | 20 | -0.050 [-0.085,-0.011] | 0.40 |
| 0.3 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.3 | euclid | euclid_unemb | 20 | +0.120 [+0.031,+0.211] | 0.80 |
| 0.3 | euclid | causal_unemb | 20 | +0.070 [-0.026,+0.159] | 0.75 |
| 0.5 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid_unemb | causal_unemb | 20 | -0.019 [-0.058,+0.022] | 0.45 |
| 0.5 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.5 | euclid | euclid_unemb | 20 | +0.140 [+0.032,+0.256] | 0.80 |
| 0.5 | euclid | causal_unemb | 20 | +0.121 [+0.013,+0.223] | 0.80 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.009 [-0.046,+0.074] | 0.65 |
| 0.7 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | euclid_unemb | 20 | +0.146 [+0.008,+0.302] | 0.65 |
| 0.7 | euclid | causal_unemb | 20 | +0.155 [+0.008,+0.295] | 0.80 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.082 [+0.047,+0.115] | 0.90 |
| 0.9 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | euclid_unemb | 20 | +0.077 [-0.124,+0.287] | 0.45 |
| 0.9 | euclid | causal_unemb | 20 | +0.159 [-0.022,+0.351] | 0.75 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid_unemb | causal_unemb | 20 | +0.206 [+0.169,+0.240] | 0.95 |
| 0.99 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | euclid_unemb | 20 | -0.090 [-0.369,+0.224] | 0.35 |
| 0.99 | euclid | causal_unemb | 20 | +0.116 [-0.143,+0.387] | 0.50 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
