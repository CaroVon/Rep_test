# Steering comparison: synthetic

backend=numpy, V=3000, d=64, pairs=120, steered contexts=10, alpha_rel=0.01, step_frac=0.01, max_steps=100, seed=0

Checks: logits_rel_err=0.0, probe held-out AUC=1.000, cos(euclid,causal)=0.613

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euc_ctx | 1.00 | 0.272 [0.212,0.331] | 0.067 [0.021,0.123] |
| 0.3 | cau_ctx | 1.00 | 0.262 [0.202,0.318] | 0.080 [0.022,0.163] |
| 0.3 | dua_ctx | 1.00 | 0.280 [0.231,0.315] | 0.049 [0.024,0.075] |
| 0.3 | euc_unemb | 1.00 | 0.287 [0.231,0.338] | 0.043 [0.014,0.079] |
| 0.3 | cau_unemb | 1.00 | 0.291 [0.235,0.335] | 0.024 [0.009,0.044] |
| 0.3 | dua_unemb | 1.00 | 0.290 [0.244,0.325] | 0.021 [0.009,0.034] |
| 0.3 | euc_dmd | 1.00 | 0.277 [0.215,0.333] | 0.062 [0.020,0.114] |
| 0.3 | cau_dmd | 1.00 | 0.280 [0.219,0.330] | 0.039 [0.012,0.073] |
| 0.3 | dua_dmd | 1.00 | 0.287 [0.246,0.323] | 0.031 [0.013,0.049] |
| 0.5 | euc_ctx | 1.00 | 0.318 [0.248,0.392] | 0.158 [0.078,0.251] |
| 0.5 | cau_ctx | 1.00 | 0.298 [0.233,0.359] | 0.178 [0.081,0.296] |
| 0.5 | dua_ctx | 0.50 | 0.263 [0.190,0.303] | 0.163 [0.141,0.197] |
| 0.5 | euc_unemb | 1.00 | 0.342 [0.272,0.401] | 0.106 [0.058,0.162] |
| 0.5 | cau_unemb | 1.00 | 0.348 [0.280,0.401] | 0.065 [0.041,0.093] |
| 0.5 | dua_unemb | 1.00 | 0.314 [0.269,0.352] | 0.076 [0.054,0.097] |
| 0.5 | euc_dmd | 1.00 | 0.326 [0.258,0.391] | 0.144 [0.073,0.229] |
| 0.5 | cau_dmd | 1.00 | 0.330 [0.265,0.389] | 0.093 [0.049,0.147] |
| 0.5 | dua_dmd | 1.00 | 0.309 [0.265,0.346] | 0.123 [0.093,0.154] |
| 0.7 | euc_ctx | 1.00 | 0.402 [0.327,0.477] | 0.320 [0.206,0.453] |
| 0.7 | cau_ctx | 1.00 | 0.371 [0.299,0.443] | 0.348 [0.213,0.519] |
| 0.7 | dua_ctx | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.7 | euc_unemb | 1.00 | 0.444 [0.359,0.523] | 0.244 [0.178,0.319] |
| 0.7 | cau_unemb | 1.00 | 0.450 [0.364,0.514] | 0.168 [0.135,0.199] |
| 0.7 | dua_unemb | 0.50 | 0.322 [0.243,0.366] | 0.139 [0.124,0.162] |
| 0.7 | euc_dmd | 1.00 | 0.416 [0.334,0.495] | 0.302 [0.198,0.421] |
| 0.7 | cau_dmd | 1.00 | 0.424 [0.339,0.495] | 0.210 [0.153,0.272] |
| 0.7 | dua_dmd | 0.50 | 0.324 [0.244,0.366] | 0.301 [0.255,0.370] |
| 0.9 | euc_ctx | 1.00 | 0.595 [0.512,0.678] | 0.803 [0.615,0.990] |
| 0.9 | cau_ctx | 0.70 | 0.630 [0.548,0.762] | 0.672 [0.522,0.957] |
| 0.9 | dua_ctx | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euc_unemb | 1.00 | 0.652 [0.561,0.728] | 0.689 [0.576,0.800] |
| 0.9 | cau_unemb | 1.00 | 0.667 [0.569,0.737] | 0.551 [0.483,0.601] |
| 0.9 | dua_unemb | 0.20 | nan [nan,nan] | nan [nan,nan] |
| 0.9 | euc_dmd | 1.00 | 0.616 [0.524,0.698] | 0.787 [0.624,0.958] |
| 0.9 | cau_dmd | 1.00 | 0.634 [0.560,0.709] | 0.618 [0.514,0.722] |
| 0.9 | dua_dmd | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euc_ctx | 1.00 | 0.894 [0.861,0.924] | 2.471 [2.099,2.872] |
| 0.99 | cau_ctx | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | dua_ctx | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euc_unemb | 1.00 | 0.918 [0.880,0.945] | 2.193 [1.945,2.443] |
| 0.99 | cau_unemb | 0.40 | 0.945 [0.923,0.977] | 1.987 [1.563,2.492] |
| 0.99 | dua_unemb | 0.00 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euc_dmd | 1.00 | 0.906 [0.876,0.932] | 2.447 [2.114,2.773] |
| 0.99 | cau_dmd | 0.90 | 0.926 [0.891,0.956] | 2.118 [1.848,2.465] |
| 0.99 | dua_dmd | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
