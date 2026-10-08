# Steering comparison: synthetic

backend=torch, V=3000, d=64, pairs=120, steered contexts=10, alpha_rel=0.01, step_frac=0.01, max_steps=100, seed=0

Checks: logits_rel_err=0.0, probe held-out AUC=1.000, cos(euclid,causal)=0.613

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.272 [0.212,0.331] | 0.067 [0.021,0.123] |
| 0.3 | causal_fixed | 1.00 | 0.263 [0.199,0.317] | 0.080 [0.022,0.154] |
| 0.3 | dual | 1.00 | 0.280 [0.234,0.317] | 0.049 [0.024,0.076] |
| 0.3 | euclid_unemb | 1.00 | 0.287 [0.225,0.338] | 0.043 [0.015,0.078] |
| 0.3 | causal_unemb | 1.00 | 0.291 [0.235,0.338] | 0.024 [0.009,0.045] |
| 0.5 | euclid | 1.00 | 0.318 [0.251,0.381] | 0.158 [0.078,0.252] |
| 0.5 | causal_fixed | 1.00 | 0.299 [0.232,0.359] | 0.175 [0.080,0.301] |
| 0.5 | dual | 0.50 | 0.263 [0.180,0.303] | 0.163 [0.141,0.197] |
| 0.5 | euclid_unemb | 1.00 | 0.342 [0.278,0.401] | 0.106 [0.057,0.164] |
| 0.5 | causal_unemb | 1.00 | 0.348 [0.280,0.402] | 0.065 [0.043,0.093] |
| 0.7 | euclid | 1.00 | 0.402 [0.327,0.479] | 0.320 [0.199,0.453] |
| 0.7 | causal_fixed | 1.00 | 0.371 [0.303,0.435] | 0.343 [0.197,0.526] |
| 0.7 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euclid_unemb | 1.00 | 0.444 [0.358,0.515] | 0.244 [0.174,0.320] |
| 0.7 | causal_unemb | 1.00 | 0.450 [0.361,0.513] | 0.168 [0.135,0.198] |
| 0.9 | euclid | 1.00 | 0.595 [0.510,0.677] | 0.803 [0.615,1.005] |
| 0.9 | causal_fixed | 0.70 | 0.635 [0.552,0.767] | 0.673 [0.513,0.960] |
| 0.9 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euclid_unemb | 1.00 | 0.652 [0.561,0.727] | 0.689 [0.571,0.801] |
| 0.9 | causal_unemb | 1.00 | 0.667 [0.565,0.736] | 0.551 [0.483,0.602] |
| 0.99 | euclid | 1.00 | 0.894 [0.859,0.924] | 2.471 [2.099,2.872] |
| 0.99 | causal_fixed | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid_unemb | 1.00 | 0.918 [0.882,0.945] | 2.193 [1.944,2.436] |
| 0.99 | causal_unemb | 0.40 | 0.945 [0.923,0.977] | 1.987 [1.563,2.492] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 10 | +0.018 [-0.008,+0.050] | 0.40 |
| 0.3 | causal_fixed | dual | 10 | +0.031 [-0.006,+0.090] | 0.40 |
| 0.3 | euclid | causal_fixed | 10 | -0.012 [-0.046,+0.001] | 0.30 |
| 0.3 | euclid_unemb | causal_unemb | 10 | +0.019 [+0.005,+0.035] | 1.00 |
| 0.3 | euclid_unemb | dual | 10 | -0.006 [-0.018,+0.011] | 0.20 |
| 0.3 | causal_unemb | dual | 10 | -0.025 [-0.038,-0.011] | 0.00 |
| 0.3 | euclid | euclid_unemb | 10 | +0.025 [+0.006,+0.046] | 0.90 |
| 0.3 | euclid | causal_unemb | 10 | +0.043 [+0.012,+0.079] | 1.00 |
| 0.5 | euclid | dual | 5 | -0.030 [-0.081,+0.072] | 0.20 |
| 0.5 | causal_fixed | dual | 5 | +0.011 [-0.080,+0.226] | 0.20 |
| 0.5 | euclid | causal_fixed | 10 | -0.017 [-0.072,+0.010] | 0.70 |
| 0.5 | euclid_unemb | causal_unemb | 10 | +0.040 [+0.014,+0.071] | 0.90 |
| 0.5 | euclid_unemb | dual | 5 | -0.063 [-0.097,-0.007] | 0.20 |
| 0.5 | causal_unemb | dual | 5 | -0.096 [-0.113,-0.070] | 0.00 |
| 0.5 | euclid | euclid_unemb | 10 | +0.053 [+0.017,+0.091] | 1.00 |
| 0.5 | euclid | causal_unemb | 10 | +0.093 [+0.033,+0.162] | 1.00 |
| 0.7 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | causal_fixed | 10 | -0.023 [-0.118,+0.028] | 0.70 |
| 0.7 | euclid_unemb | causal_unemb | 10 | +0.076 [+0.036,+0.125] | 0.90 |
| 0.7 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.7 | euclid | euclid_unemb | 10 | +0.075 [+0.025,+0.135] | 1.00 |
| 0.7 | euclid | causal_unemb | 10 | +0.152 [+0.060,+0.255] | 0.90 |
| 0.9 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | causal_fixed | 7 | +0.018 [-0.086,+0.069] | 0.71 |
| 0.9 | euclid_unemb | causal_unemb | 10 | +0.138 [+0.064,+0.227] | 0.90 |
| 0.9 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.9 | euclid | euclid_unemb | 10 | +0.114 [+0.030,+0.204] | 0.70 |
| 0.9 | euclid | causal_unemb | 10 | +0.251 [+0.100,+0.433] | 0.90 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid_unemb | causal_unemb | 4 | +0.267 [+0.186,+0.429] | 1.00 |
| 0.99 | euclid_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_unemb | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | euclid_unemb | 10 | +0.278 [+0.098,+0.478] | 0.90 |
| 0.99 | euclid | causal_unemb | 4 | +0.412 [+0.281,+0.639] | 1.00 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
