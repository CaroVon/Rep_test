# Steering comparison: synthetic

backend=torch, V=3000, d=64, pairs=120, steered contexts=19, alpha_rel=0.01, step_frac=0.01, max_steps=600, seed=0

Checks: logits_rel_err=0.0, probe held-out AUC=1.000, cos(euclid,causal)=0.613

## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)

| level | method | reach | cf mass | off-target KL |
|---|---|---|---|---|
| 0.3 | euclid | 1.00 | 0.291 [0.251,0.330] | 0.043 [0.015,0.077] |
| 0.3 | causal_fixed | 1.00 | 0.283 [0.242,0.327] | 0.048 [0.014,0.089] |
| 0.3 | dual | 1.00 | 0.290 [0.255,0.329] | 0.042 [0.021,0.067] |
| 0.5 | euclid | 1.00 | 0.343 [0.297,0.391] | 0.118 [0.072,0.175] |
| 0.5 | causal_fixed | 1.00 | 0.326 [0.276,0.378] | 0.125 [0.075,0.190] |
| 0.5 | dual | 0.95 | 0.289 [0.258,0.325] | 0.195 [0.158,0.234] |
| 0.7 | euclid | 1.00 | 0.434 [0.374,0.492] | 0.270 [0.203,0.350] |
| 0.7 | causal_fixed | 1.00 | 0.405 [0.341,0.471] | 0.275 [0.201,0.365] |
| 0.7 | dual | 0.95 | 0.313 [0.275,0.350] | 0.962 [0.620,1.326] |
| 0.9 | euclid | 1.00 | 0.635 [0.564,0.700] | 0.753 [0.638,0.883] |
| 0.9 | causal_fixed | 1.00 | 0.592 [0.519,0.666] | 0.739 [0.619,0.881] |
| 0.9 | dual | 0.58 | 0.296 [0.269,0.325] | 1.383 [1.110,1.720] |
| 0.99 | euclid | 1.00 | 0.910 [0.883,0.934] | 2.403 [2.135,2.703] |
| 0.99 | causal_fixed | 1.00 | 0.880 [0.841,0.919] | 2.398 [2.055,2.785] |
| 0.99 | dual | 0.42 | 0.357 [0.328,0.386] | 3.343 [3.004,3.739] |

## Paired KL difference a - b (>0 means b is better)

| level | a | b | n | diff [CI] | P(b lower KL) |
|---|---|---|---|---|---|
| 0.3 | euclid | dual | 19 | +0.001 [-0.024,+0.023] | 0.32 |
| 0.3 | causal_fixed | dual | 19 | +0.006 [-0.022,+0.037] | 0.26 |
| 0.3 | euclid | causal_fixed | 19 | -0.006 [-0.020,+0.002] | 0.37 |
| 0.5 | euclid | dual | 18 | -0.074 [-0.121,-0.023] | 0.17 |
| 0.5 | causal_fixed | dual | 18 | -0.069 [-0.123,-0.003] | 0.11 |
| 0.5 | euclid | causal_fixed | 19 | -0.007 [-0.033,+0.012] | 0.58 |
| 0.7 | euclid | dual | 18 | -0.688 [-1.076,-0.322] | 0.17 |
| 0.7 | causal_fixed | dual | 18 | -0.686 [-1.105,-0.327] | 0.11 |
| 0.7 | euclid | causal_fixed | 19 | -0.005 [-0.048,+0.035] | 0.63 |
| 0.9 | euclid | dual | 11 | -0.579 [-0.955,-0.254] | 0.18 |
| 0.9 | causal_fixed | dual | 11 | -0.615 [-1.017,-0.256] | 0.09 |
| 0.9 | euclid | causal_fixed | 19 | +0.014 [-0.080,+0.107] | 0.58 |
| 0.99 | euclid | dual | 8 | -0.860 [-1.472,-0.270] | 0.12 |
| 0.99 | causal_fixed | dual | 8 | -0.695 [-1.493,-0.016] | 0.25 |
| 0.99 | euclid | causal_fixed | 19 | +0.004 [-0.246,+0.253] | 0.53 |

## Caveats (keep these when presenting)
- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).
- Template contexts, one concept (verb -> 3rd person), small model unless stated.
- Results depend on alpha_rel; report the sweep.
- Probe is trained on templates; AUC above is held-out within the same templates.
