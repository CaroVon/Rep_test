# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=20, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.976

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.364 [0.297,0.455] | 0.660 [0.524,0.796] |
| 0.3 | euclid_unemb | 1.00 | 0.353 [0.288,0.437] | 0.540 [0.433,0.637] |
| 0.3 | causal_unemb | 1.00 | 0.329 [0.271,0.405] | 0.590 [0.458,0.715] |
| 0.3 | dual | 1.00 | 0.533 [0.489,0.586] | 2.300 [1.942,2.698] |
| 0.5 | euclid | 1.00 | 0.362 [0.296,0.451] | 0.799 [0.649,0.946] |
| 0.5 | euclid_unemb | 1.00 | 0.359 [0.294,0.440] | 0.658 [0.545,0.770] |
| 0.5 | causal_unemb | 1.00 | 0.337 [0.278,0.415] | 0.678 [0.535,0.806] |
| 0.5 | dual | 1.00 | 0.473 [0.433,0.516] | 4.051 [3.589,4.523] |
| 0.7 | euclid | 1.00 | 0.384 [0.316,0.473] | 0.922 [0.751,1.097] |
| 0.7 | euclid_unemb | 1.00 | 0.386 [0.325,0.468] | 0.776 [0.665,0.914] |
| 0.7 | causal_unemb | 1.00 | 0.365 [0.305,0.440] | 0.767 [0.612,0.931] |
| 0.7 | dual | 0.80 | 0.413 [0.378,0.453] | 5.362 [4.756,5.998] |
| 0.9 | euclid | 1.00 | 0.454 [0.387,0.537] | 1.120 [0.923,1.318] |
| 0.9 | euclid_unemb | 1.00 | 0.454 [0.401,0.526] | 1.042 [0.901,1.247] |
| 0.9 | causal_unemb | 1.00 | 0.439 [0.387,0.511] | 0.960 [0.805,1.171] |
| 0.9 | dual | 0.30 | 0.345 [0.291,0.410] | 5.947 [5.092,7.201] |
| 0.99 | euclid | 1.00 | 0.593 [0.535,0.664] | 1.630 [1.381,1.883] |
| 0.99 | euclid_unemb | 1.00 | 0.568 [0.539,0.611] | 1.720 [1.507,2.017] |
| 0.99 | causal_unemb | 1.00 | 0.562 [0.529,0.613] | 1.514 [1.305,1.815] |
| 0.99 | dual | 0.10 | nan [nan,nan] | nan [nan,nan] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 20 | -1.640 [-2.049,-1.320] | 0.10 |
| 0.3 | euclid_unemb | causal_unemb | 20 | -0.050 [-0.085,-0.011] | 0.40 |
| 0.3 | euclid_unemb | dual | 20 | -1.760 [-2.135,-1.439] | 0.05 |
| 0.3 | causal_unemb | dual | 20 | -1.710 [-2.110,-1.395] | 0.05 |
| 0.3 | euclid | euclid_unemb | 20 | +0.120 [+0.039,+0.207] | 0.80 |
| 0.3 | euclid | causal_unemb | 20 | +0.070 [-0.029,+0.162] | 0.75 |
| 0.5 | euclid | dual | 20 | -3.252 [-3.796,-2.784] | 0.00 |
| 0.5 | euclid_unemb | causal_unemb | 20 | -0.019 [-0.057,+0.023] | 0.45 |
| 0.5 | euclid_unemb | dual | 20 | -3.393 [-3.907,-2.941] | 0.00 |
| 0.5 | causal_unemb | dual | 20 | -3.373 [-3.846,-2.933] | 0.00 |
| 0.5 | euclid | euclid_unemb | 20 | +0.140 [+0.032,+0.261] | 0.80 |
| 0.5 | euclid | causal_unemb | 20 | +0.121 [+0.011,+0.223] | 0.80 |
| 0.7 | euclid | dual | 16 | -4.406 [-5.050,-3.809] | 0.00 |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.009 [-0.047,+0.072] | 0.65 |
| 0.7 | euclid_unemb | dual | 16 | -4.578 [-5.274,-3.966] | 0.00 |
| 0.7 | causal_unemb | dual | 16 | -4.591 [-5.255,-4.035] | 0.00 |
| 0.7 | euclid | euclid_unemb | 20 | +0.146 [+0.008,+0.308] | 0.65 |
| 0.7 | euclid | causal_unemb | 20 | +0.155 [+0.008,+0.301] | 0.80 |
| 0.9 | euclid | dual | 6 | -4.871 [-6.250,-4.181] | 0.00 |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.082 [+0.046,+0.114] | 0.90 |
| 0.9 | euclid_unemb | dual | 6 | -4.810 [-6.399,-4.015] | 0.00 |
| 0.9 | causal_unemb | dual | 6 | -4.890 [-6.507,-4.082] | 0.00 |
| 0.9 | euclid | euclid_unemb | 20 | +0.077 [-0.112,+0.287] | 0.45 |
| 0.9 | euclid | causal_unemb | 20 | +0.159 [-0.022,+0.347] | 0.75 |
| 0.99 | euclid | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.99 | euclid_unemb | causal_unemb | 20 | +0.206 [+0.168,+0.240] | 0.95 |
| 0.99 | euclid_unemb | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.99 | causal_unemb | dual | 2 | +nan [+nan,+nan] | 0.00 |
| 0.99 | euclid | euclid_unemb | 20 | -0.090 [-0.366,+0.210] | 0.35 |
| 0.99 | euclid | causal_unemb | 20 | +0.116 [-0.151,+0.382] | 0.50 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
