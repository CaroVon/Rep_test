# Steering comparison: gpt2

backend=torch, V=50257, d=768, pairs=143, steered contexts=80, alpha_rel=0.1, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=6.392812679223425e-07, probe held-out AUC=0.931, cos(euclid,causal)=0.966

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.193 [0.169,0.219] | 0.671 [0.628,0.716] |
| 0.3 | causal_fixed | 1.00 | 0.131 [0.104,0.159] | 2.260 [2.007,2.524] |
| 0.3 | dual | 0.99 | 0.441 [0.416,0.465] | 5.440 [4.999,5.906] |
| 0.5 | euclid | 1.00 | 0.198 [0.172,0.224] | 0.773 [0.725,0.820] |
| 0.5 | causal_fixed | 1.00 | 0.072 [0.050,0.097] | 3.631 [3.282,3.996] |
| 0.5 | dual | 0.39 | 0.315 [0.288,0.342] | 5.904 [5.256,6.579] |
| 0.7 | euclid | 1.00 | 0.224 [0.197,0.251] | 0.847 [0.800,0.893] |
| 0.7 | causal_fixed | 1.00 | 0.040 [0.023,0.062] | 5.274 [4.818,5.735] |
| 0.7 | dual | 0.20 | 0.255 [0.232,0.279] | 6.457 [5.750,7.177] |
| 0.9 | euclid | 1.00 | 0.304 [0.273,0.335] | 0.967 [0.921,1.014] |
| 0.9 | causal_fixed | 1.00 | 0.016 [0.005,0.033] | 8.108 [7.568,8.633] |
| 0.9 | dual | 0.03 | nan [nan,nan] | nan [nan,nan] |
| 0.99 | euclid | 1.00 | 0.497 [0.470,0.523] | 1.427 [1.348,1.503] |
| 0.99 | causal_fixed | 1.00 | 0.002 [0.000,0.004] | 13.357 [12.678,13.989] |
| 0.99 | dual | 0.00 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 79 | -4.774 [-5.223,-4.337] | 0.00 |
| 0.3 | causal_fixed | dual | 79 | -3.210 [-3.732,-2.703] | 0.11 |
| 0.3 | euclid | causal_fixed | 80 | -1.589 [-1.835,-1.359] | 0.00 |
| 0.5 | euclid | dual | 31 | -5.149 [-5.806,-4.483] | 0.00 |
| 0.5 | causal_fixed | dual | 31 | -2.330 [-3.236,-1.445] | 0.29 |
| 0.5 | euclid | causal_fixed | 80 | -2.858 [-3.203,-2.545] | 0.00 |
| 0.7 | euclid | dual | 16 | -5.752 [-6.526,-5.044] | 0.00 |
| 0.7 | causal_fixed | dual | 16 | -0.737 [-1.955,+0.412] | 0.44 |
| 0.7 | euclid | causal_fixed | 80 | -4.428 [-4.858,-4.013] | 0.00 |
| 0.9 | euclid | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.9 | causal_fixed | dual | 2 | +nan [+nan,+nan] | 1.00 |
| 0.9 | euclid | causal_fixed | 80 | -7.141 [-7.680,-6.594] | 0.00 |
| 0.99 | euclid | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | causal_fixed | dual | 0 | +nan [+nan,+nan] | nan |
| 0.99 | euclid | causal_fixed | 80 | -11.931 [-12.609,-11.293] | 0.00 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
