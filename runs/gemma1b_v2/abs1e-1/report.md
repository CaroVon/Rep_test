# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=20, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=1.000

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.364 [0.297,0.455] | 0.660 [0.524,0.796] |
| 0.3 | euclid_unemb | 1.00 | 0.353 [0.288,0.437] | 0.540 [0.433,0.637] |
| 0.3 | causal_unemb | 1.00 | 0.329 [0.271,0.405] | 0.590 [0.458,0.715] |
| 0.3 | dual | 1.00 | 0.429 [0.367,0.511] | 0.454 [0.364,0.534] |
| 0.5 | euclid | 1.00 | 0.362 [0.296,0.451] | 0.799 [0.649,0.946] |
| 0.5 | euclid_unemb | 1.00 | 0.359 [0.294,0.440] | 0.658 [0.545,0.770] |
| 0.5 | causal_unemb | 1.00 | 0.337 [0.278,0.415] | 0.678 [0.535,0.806] |
| 0.5 | dual | 1.00 | 0.426 [0.362,0.511] | 0.590 [0.490,0.690] |
| 0.7 | euclid | 1.00 | 0.384 [0.316,0.473] | 0.922 [0.751,1.097] |
| 0.7 | euclid_unemb | 1.00 | 0.386 [0.325,0.468] | 0.776 [0.665,0.914] |
| 0.7 | causal_unemb | 1.00 | 0.365 [0.305,0.440] | 0.767 [0.612,0.931] |
| 0.7 | dual | 1.00 | 0.443 [0.376,0.523] | 0.741 [0.623,0.855] |
| 0.9 | euclid | 1.00 | 0.454 [0.387,0.540] | 1.120 [0.923,1.320] |
| 0.9 | euclid_unemb | 1.00 | 0.454 [0.401,0.525] | 1.042 [0.902,1.243] |
| 0.9 | causal_unemb | 1.00 | 0.439 [0.386,0.511] | 0.960 [0.806,1.167] |
| 0.9 | dual | 1.00 | 0.495 [0.430,0.571] | 1.017 [0.863,1.185] |
| 0.99 | euclid | 1.00 | 0.593 [0.536,0.666] | 1.630 [1.388,1.881] |
| 0.99 | euclid_unemb | 1.00 | 0.568 [0.538,0.610] | 1.720 [1.515,2.021] |
| 0.99 | causal_unemb | 1.00 | 0.562 [0.528,0.613] | 1.514 [1.304,1.810] |
| 0.99 | dual | 1.00 | 0.598 [0.546,0.662] | 1.618 [1.393,1.840] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 20 | +0.206 [+0.143,+0.263] | 0.90 |
| 0.3 | euclid_unemb | causal_unemb | 20 | -0.050 [-0.085,-0.012] | 0.40 |
| 0.3 | euclid_unemb | dual | 20 | +0.086 [+0.017,+0.171] | 0.70 |
| 0.3 | causal_unemb | dual | 20 | +0.136 [+0.053,+0.233] | 0.70 |
| 0.3 | euclid | euclid_unemb | 20 | +0.120 [+0.031,+0.204] | 0.80 |
| 0.3 | euclid | causal_unemb | 20 | +0.070 [-0.022,+0.156] | 0.75 |
| 0.5 | euclid | dual | 20 | +0.208 [+0.136,+0.276] | 0.85 |
| 0.5 | euclid_unemb | causal_unemb | 20 | -0.019 [-0.057,+0.021] | 0.45 |
| 0.5 | euclid_unemb | dual | 20 | +0.068 [-0.023,+0.158] | 0.55 |
| 0.5 | causal_unemb | dual | 20 | +0.088 [+0.002,+0.192] | 0.60 |
| 0.5 | euclid | euclid_unemb | 20 | +0.140 [+0.030,+0.254] | 0.80 |
| 0.5 | euclid | causal_unemb | 20 | +0.121 [+0.018,+0.222] | 0.80 |
| 0.7 | euclid | dual | 20 | +0.181 [+0.106,+0.261] | 0.85 |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.009 [-0.045,+0.071] | 0.65 |
| 0.7 | euclid_unemb | dual | 20 | +0.035 [-0.094,+0.148] | 0.50 |
| 0.7 | causal_unemb | dual | 20 | +0.027 [-0.085,+0.149] | 0.50 |
| 0.7 | euclid | euclid_unemb | 20 | +0.146 [+0.009,+0.300] | 0.65 |
| 0.7 | euclid | causal_unemb | 20 | +0.155 [+0.017,+0.301] | 0.80 |
| 0.9 | euclid | dual | 20 | +0.103 [+0.034,+0.182] | 0.50 |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.082 [+0.046,+0.115] | 0.90 |
| 0.9 | euclid_unemb | dual | 20 | +0.025 [-0.156,+0.201] | 0.55 |
| 0.9 | causal_unemb | dual | 20 | -0.057 [-0.207,+0.101] | 0.35 |
| 0.9 | euclid | euclid_unemb | 20 | +0.077 [-0.130,+0.296] | 0.45 |
| 0.9 | euclid | causal_unemb | 20 | +0.159 [-0.022,+0.342] | 0.75 |
| 0.99 | euclid | dual | 20 | +0.012 [-0.036,+0.085] | 0.45 |
| 0.99 | euclid_unemb | causal_unemb | 20 | +0.206 [+0.168,+0.240] | 0.95 |
| 0.99 | euclid_unemb | dual | 20 | +0.102 [-0.181,+0.352] | 0.70 |
| 0.99 | causal_unemb | dual | 20 | -0.104 [-0.373,+0.151] | 0.35 |
| 0.99 | euclid | euclid_unemb | 20 | -0.090 [-0.370,+0.237] | 0.35 |
| 0.99 | euclid | causal_unemb | 20 | +0.116 [-0.161,+0.403] | 0.50 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
