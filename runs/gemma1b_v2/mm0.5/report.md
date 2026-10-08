# Steering comparison: google/gemma-3-1b-pt

backend=torch, V=262144, d=1152, pairs=144, steered contexts=20, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.002942702267318964, probe held-out AUC=1.000, cos(euclid,causal)=0.997

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.383 [0.257,0.480] | 0.686 [0.426,1.023] |
| 0.3 | euclid_unemb | 1.00 | 0.387 [0.271,0.472] | 0.632 [0.363,1.013] |
| 0.3 | causal_unemb | 1.00 | 0.363 [0.252,0.445] | 0.676 [0.392,1.139] |
| 0.3 | dual | 1.00 | 0.598 [0.573,0.618] | 0.553 [0.485,0.628] |
| 0.5 | euclid | 1.00 | 0.382 [0.258,0.483] | 0.816 [0.551,1.163] |
| 0.5 | euclid_unemb | 1.00 | 0.392 [0.280,0.473] | 0.744 [0.459,1.141] |
| 0.5 | causal_unemb | 1.00 | 0.370 [0.262,0.450] | 0.782 [0.471,1.252] |
| 0.5 | dual | 1.00 | 0.566 [0.542,0.583] | 1.227 [1.080,1.389] |
| 0.7 | euclid | 1.00 | 0.404 [0.273,0.509] | 0.942 [0.680,1.301] |
| 0.7 | euclid_unemb | 1.00 | 0.422 [0.300,0.508] | 0.913 [0.632,1.328] |
| 0.7 | causal_unemb | 1.00 | 0.394 [0.275,0.479] | 0.879 [0.571,1.329] |
| 0.7 | dual | 1.00 | 0.532 [0.510,0.547] | 2.172 [1.905,2.430] |
| 0.9 | euclid | 1.00 | 0.475 [0.340,0.574] | 1.138 [0.896,1.496] |
| 0.9 | euclid_unemb | 1.00 | 0.477 [0.358,0.560] | 1.201 [0.904,1.597] |
| 0.9 | causal_unemb | 1.00 | 0.465 [0.339,0.552] | 1.137 [0.823,1.563] |
| 0.9 | dual | 1.00 | 0.502 [0.483,0.515] | 3.480 [3.103,3.840] |
| 0.99 | euclid | 1.00 | 0.610 [0.498,0.693] | 1.636 [1.400,1.959] |
| 0.99 | euclid_unemb | 1.00 | 0.561 [0.464,0.635] | 1.956 [1.644,2.375] |
| 0.99 | causal_unemb | 1.00 | 0.550 [0.436,0.637] | 1.742 [1.409,2.194] |
| 0.99 | dual | 1.00 | 0.491 [0.471,0.507] | 4.615 [4.163,5.061] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 20 | +0.133 [-0.136,+0.445] | 0.50 |
| 0.3 | euclid_unemb | causal_unemb | 20 | -0.044 [-0.104,-0.009] | 0.40 |
| 0.3 | euclid_unemb | dual | 20 | +0.079 [-0.206,+0.463] | 0.45 |
| 0.3 | causal_unemb | dual | 20 | +0.123 [-0.182,+0.553] | 0.45 |
| 0.3 | euclid | euclid_unemb | 20 | +0.055 [-0.126,+0.211] | 0.70 |
| 0.3 | euclid | causal_unemb | 20 | +0.010 [-0.222,+0.184] | 0.70 |
| 0.5 | euclid | dual | 20 | -0.410 [-0.782,+0.006] | 0.35 |
| 0.5 | euclid_unemb | causal_unemb | 20 | -0.037 [-0.116,+0.005] | 0.40 |
| 0.5 | euclid_unemb | dual | 20 | -0.482 [-0.873,-0.031] | 0.25 |
| 0.5 | causal_unemb | dual | 20 | -0.445 [-0.868,+0.127] | 0.30 |
| 0.5 | euclid | euclid_unemb | 20 | +0.072 [-0.115,+0.228] | 0.75 |
| 0.5 | euclid | causal_unemb | 20 | +0.035 [-0.225,+0.214] | 0.75 |
| 0.7 | euclid | dual | 20 | -1.230 [-1.678,-0.706] | 0.05 |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.033 [-0.044,+0.087] | 0.80 |
| 0.7 | euclid_unemb | dual | 20 | -1.259 [-1.740,-0.692] | 0.05 |
| 0.7 | causal_unemb | dual | 20 | -1.293 [-1.786,-0.617] | 0.10 |
| 0.7 | euclid | euclid_unemb | 20 | +0.029 [-0.176,+0.192] | 0.75 |
| 0.7 | euclid | causal_unemb | 20 | +0.063 [-0.206,+0.245] | 0.80 |
| 0.9 | euclid | dual | 20 | -2.342 [-2.852,-1.818] | 0.00 |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.063 [+0.008,+0.121] | 0.65 |
| 0.9 | euclid_unemb | dual | 20 | -2.279 [-2.852,-1.627] | 0.05 |
| 0.9 | causal_unemb | dual | 20 | -2.342 [-2.915,-1.643] | 0.05 |
| 0.9 | euclid | euclid_unemb | 20 | -0.063 [-0.269,+0.080] | 0.45 |
| 0.9 | euclid | causal_unemb | 20 | +0.001 [-0.255,+0.158] | 0.65 |
| 0.99 | euclid | dual | 20 | -2.979 [-3.420,-2.508] | 0.00 |
| 0.99 | euclid_unemb | causal_unemb | 20 | +0.214 [+0.180,+0.260] | 0.90 |
| 0.99 | euclid_unemb | dual | 20 | -2.659 [-3.256,-2.023] | 0.05 |
| 0.99 | causal_unemb | dual | 20 | -2.873 [-3.468,-2.238] | 0.05 |
| 0.99 | euclid | euclid_unemb | 20 | -0.320 [-0.533,-0.143] | 0.10 |
| 0.99 | euclid | causal_unemb | 20 | -0.106 [-0.310,+0.055] | 0.45 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
