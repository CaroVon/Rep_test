# Steering comparison: gpt2

backend=numpy, V=50257, d=768, pairs=143, steered contexts=20, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=6.392812679223425e-07, probe held-out AUC=0.931, cos(euclid,causal)=0.979

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.184 [0.104,0.242] | 0.612 [0.534,0.727] |
| 0.3 | euclid_unemb | 1.00 | 0.249 [0.141,0.315] | 0.972 [0.836,1.177] |
| 0.3 | causal_unemb | 1.00 | 0.190 [0.106,0.245] | 0.436 [0.372,0.537] |
| 0.5 | euclid | 1.00 | 0.188 [0.109,0.252] | 0.730 [0.659,0.824] |
| 0.5 | euclid_unemb | 1.00 | 0.301 [0.169,0.388] | 1.235 [1.087,1.352] |
| 0.5 | causal_unemb | 1.00 | 0.190 [0.105,0.246] | 0.519 [0.454,0.613] |
| 0.7 | euclid | 1.00 | 0.215 [0.130,0.286] | 0.812 [0.744,0.887] |
| 0.7 | euclid_unemb | 1.00 | 0.310 [0.195,0.391] | 1.270 [1.181,1.355] |
| 0.7 | causal_unemb | 1.00 | 0.211 [0.124,0.271] | 0.590 [0.531,0.678] |
| 0.9 | euclid | 1.00 | 0.293 [0.198,0.368] | 0.946 [0.881,0.988] |
| 0.9 | euclid_unemb | 1.00 | 0.310 [0.193,0.388] | 1.270 [1.179,1.351] |
| 0.9 | causal_unemb | 1.00 | 0.281 [0.170,0.353] | 0.725 [0.684,0.790] |
| 0.99 | euclid | 1.00 | 0.492 [0.425,0.539] | 1.492 [1.328,1.587] |
| 0.99 | euclid_unemb | 1.00 | 0.493 [0.383,0.558] | 2.750 [2.177,3.149] |
| 0.99 | causal_unemb | 1.00 | 0.440 [0.326,0.510] | 1.250 [1.171,1.317] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid_unemb | causal_unemb | 20 | +0.535 [+0.428,+0.675] | 1.00 |
| 0.3 | euclid | euclid_unemb | 20 | -0.360 [-0.476,-0.246] | 0.20 |
| 0.3 | euclid | causal_unemb | 20 | +0.175 [+0.135,+0.207] | 1.00 |
| 0.5 | euclid_unemb | causal_unemb | 20 | +0.716 [+0.555,+0.862] | 1.00 |
| 0.5 | euclid | euclid_unemb | 20 | -0.505 [-0.654,-0.377] | 0.00 |
| 0.5 | euclid | causal_unemb | 20 | +0.211 [+0.167,+0.241] | 0.95 |
| 0.7 | euclid_unemb | causal_unemb | 20 | +0.680 [+0.546,+0.803] | 1.00 |
| 0.7 | euclid | euclid_unemb | 20 | -0.457 [-0.558,-0.336] | 0.00 |
| 0.7 | euclid | causal_unemb | 20 | +0.223 [+0.147,+0.261] | 0.95 |
| 0.9 | euclid_unemb | causal_unemb | 20 | +0.544 [+0.448,+0.638] | 1.00 |
| 0.9 | euclid | euclid_unemb | 20 | -0.324 [-0.400,-0.239] | 0.05 |
| 0.9 | euclid | causal_unemb | 20 | +0.220 [+0.121,+0.264] | 0.90 |
| 0.99 | euclid_unemb | causal_unemb | 20 | +1.500 [+0.987,+1.854] | 1.00 |
| 0.99 | euclid | euclid_unemb | 20 | -1.258 [-1.591,-0.749] | 0.00 |
| 0.99 | euclid | causal_unemb | 20 | +0.242 [+0.087,+0.340] | 0.90 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
