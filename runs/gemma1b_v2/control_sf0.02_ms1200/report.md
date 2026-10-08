# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=20, alpha_rel=0.01, step_frac=0.02, max_steps=1200, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.997

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.363 [0.296,0.454] | 0.675 [0.534,0.817] |
| 0.3 | euclid_unemb | 1.00 | 0.354 [0.288,0.438] | 0.576 [0.477,0.671] |
| 0.3 | causal_unemb | 1.00 | 0.331 [0.272,0.406] | 0.612 [0.480,0.734] |
| 0.3 | dual | 1.00 | 0.555 [0.501,0.620] | 0.520 [0.443,0.598] |
| 0.5 | euclid | 1.00 | 0.364 [0.299,0.453] | 0.820 [0.660,0.971] |
| 0.5 | euclid_unemb | 1.00 | 0.366 [0.301,0.447] | 0.701 [0.575,0.835] |
| 0.5 | causal_unemb | 1.00 | 0.345 [0.286,0.424] | 0.714 [0.563,0.854] |
| 0.5 | dual | 1.00 | 0.527 [0.476,0.584] | 1.126 [0.966,1.289] |
| 0.7 | euclid | 1.00 | 0.388 [0.320,0.478] | 0.938 [0.766,1.113] |
| 0.7 | euclid_unemb | 1.00 | 0.400 [0.338,0.483] | 0.826 [0.714,0.968] |
| 0.7 | causal_unemb | 1.00 | 0.377 [0.316,0.454] | 0.795 [0.629,0.979] |
| 0.7 | dual | 1.00 | 0.501 [0.454,0.550] | 1.984 [1.704,2.261] |
| 0.9 | euclid | 1.00 | 0.459 [0.393,0.543] | 1.135 [0.931,1.345] |
| 0.9 | euclid_unemb | 1.00 | 0.473 [0.426,0.540] | 1.103 [0.958,1.307] |
| 0.9 | causal_unemb | 1.00 | 0.453 [0.400,0.527] | 1.020 [0.861,1.245] |
| 0.9 | dual | 1.00 | 0.479 [0.438,0.520] | 3.286 [2.800,3.773] |
| 0.99 | euclid | 1.00 | 0.598 [0.541,0.671] | 1.652 [1.416,1.899] |
| 0.99 | euclid_unemb | 1.00 | 0.579 [0.553,0.618] | 1.813 [1.591,2.116] |
| 0.99 | causal_unemb | 1.00 | 0.568 [0.537,0.616] | 1.564 [1.349,1.857] |
| 0.99 | dual | 1.00 | 0.476 [0.441,0.511] | 4.455 [3.810,5.067] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 20 | +0.155 [+0.020,+0.269] | 0.55 |
| 0.3 | euclid_unemb | causal_unemb | 20 | -0.036 [-0.074,+0.014] | 0.45 |
| 0.3 | euclid_unemb | dual | 20 | +0.056 [-0.046,+0.145] | 0.55 |
| 0.3 | causal_unemb | dual | 20 | +0.092 [-0.023,+0.184] | 0.55 |
| 0.3 | euclid | euclid_unemb | 20 | +0.099 [-0.002,+0.193] | 0.70 |
| 0.3 | euclid | causal_unemb | 20 | +0.063 [-0.025,+0.142] | 0.70 |
| 0.5 | euclid | dual | 20 | -0.307 [-0.522,-0.134] | 0.40 |
| 0.5 | euclid_unemb | causal_unemb | 20 | -0.013 [-0.067,+0.040] | 0.40 |
| 0.5 | euclid_unemb | dual | 20 | -0.426 [-0.625,-0.260] | 0.25 |
| 0.5 | causal_unemb | dual | 20 | -0.412 [-0.586,-0.260] | 0.30 |
| 0.5 | euclid | euclid_unemb | 20 | +0.119 [-0.009,+0.256] | 0.70 |
| 0.5 | euclid | causal_unemb | 20 | +0.106 [-0.004,+0.214] | 0.70 |
| 0.7 | euclid | dual | 20 | -1.046 [-1.346,-0.756] | 0.15 |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.031 [-0.040,+0.111] | 0.70 |
| 0.7 | euclid_unemb | dual | 20 | -1.158 [-1.477,-0.860] | 0.05 |
| 0.7 | causal_unemb | dual | 20 | -1.189 [-1.503,-0.888] | 0.10 |
| 0.7 | euclid | euclid_unemb | 20 | +0.112 [-0.016,+0.261] | 0.50 |
| 0.7 | euclid | causal_unemb | 20 | +0.143 [-0.011,+0.304] | 0.75 |
| 0.9 | euclid | dual | 20 | -2.150 [-2.632,-1.667] | 0.05 |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.083 [+0.028,+0.137] | 0.80 |
| 0.9 | euclid_unemb | dual | 20 | -2.182 [-2.750,-1.621] | 0.05 |
| 0.9 | causal_unemb | dual | 20 | -2.266 [-2.805,-1.681] | 0.05 |
| 0.9 | euclid | euclid_unemb | 20 | +0.032 [-0.183,+0.272] | 0.50 |
| 0.9 | euclid | causal_unemb | 20 | +0.115 [-0.092,+0.316] | 0.60 |
| 0.99 | euclid | dual | 20 | -2.803 [-3.373,-2.203] | 0.00 |
| 0.99 | euclid_unemb | causal_unemb | 20 | +0.249 [+0.169,+0.316] | 0.90 |
| 0.99 | euclid_unemb | dual | 20 | -2.642 [-3.421,-1.856] | 0.10 |
| 0.99 | causal_unemb | dual | 20 | -2.891 [-3.636,-2.117] | 0.05 |
| 0.99 | euclid | euclid_unemb | 20 | -0.161 [-0.448,+0.188] | 0.30 |
| 0.99 | euclid | causal_unemb | 20 | +0.088 [-0.166,+0.349] | 0.50 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
