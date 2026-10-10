# V4 conclusions (hand-written; all numbers quoted appear in runs/AGGREGATE_V4.md or the referenced CSVs)

Scope labels on every claim: [region A = symmetric templates | region C = C4 natural
text with Park's top-3/mass>=0.7 filter] x [concept: third | ing] x [model] x
[level 0.9, metric kl unless stated]. Independent unit = (model, seed, concept,
region) per task doc section 2.5. Equivalence margin +-0.05 (proposed, not yet
confirmed by Victor). Uncorrected multiplicity; C1/C2 are the only confirmatory
comparisons.

## 1. Pre-specified comparisons

**C1 (euc_dmd vs dua_dmd; confirmatory)** - [region C, concept third, gemma-1b,
alpha 5e-3]: **cannot establish that the adaptive method is better; the REVERSE
direction is established in this setting** - all 3 independent units (seeds)
give dua_dmd WORSE with CIs excluding 0: s0 -0.80 [-1.06,-0.53], s1 -0.91
[-1.27,-0.59], s2 -0.75 [-1.05,-0.45] (3/3 units, "established" bar met for
the reverse claim within region C). Within-unit alpha sensitivity: at
alpha>=2e-2 the sign flips to dua better in 3/3 seeds (s0 +0.35 [+0.17,+0.54],
s1 +0.31 [+0.04,+0.57], s2 +0.38 [+0.13,+0.63] at 2e-2; +0.46..+0.64 at 1e-1).
- [region A, concept third]: direction consistent, not established (3/3 seeds
  positive, CI excludes 0 in 2/3: s0 +0.162 [+0.023,+0.316], s2 +0.248
  [+0.048,+0.488], s1 +0.113 [-0.061,+0.311]).
- [region A, concept ing]: dua_dmd better, 3/3 seeds CI excluding 0
  (+0.92..+1.59) - BUT the dmd probe is frame-confounded on the -ing concept
  (auxiliary verb), so this is hypothesis-generating only.

**C2 (cau_unemb vs dua_unemb; confirmative)** - [region C, third, gemma-1b,
alpha 5e-3]: **fixed metric better, established in this setting** - 3/3 units,
CIs excluding 0 (-1.11 .. -1.24). At alpha 1e-1 the difference crosses 0
(+0.01..+0.06) but the interval upper bounds (up to +0.141) exceed the +-0.05
margin, so formal practical equivalence holds in 0/3 seeds (point estimates
within margin in 2/3).
- [region A, third, alpha 5e-3]: fixed better 3/3 (-0.58..-0.64, CIs exclude
  0); at alpha 1e-1 crosses 0 (same pattern as region C).

## 2. Descriptive / exploratory (D1-D3)

**D1 - KL decomposition (R1 answer)**: the adaptive methods' excess KL is
almost entirely **kl_neu (redistribution inside the neutral set)**, not mass
transfer to the counterfactual pairs: for C2 at alpha 5e-3, kl_neu carries
-0.70..-0.79 (region A) and -1.17..-1.23 (region C) of the total -0.58..-1.24,
while kl_bin (+0.04..+0.18) and kl_pair (+0.03..+0.06) actually favor the
adaptive method slightly, and its cf_dev is SMALLER (Q3 cf_dev +0.07..+0.16,
i.e. dua deviates less from the starting pair mass). Both branches of the
task's R1 expectation are therefore resolved: not "moving mass onto the
pairs" but "reshuffling the neutral tail", and this cost grows in the
concentrated regime (region C, cf0~0.92).

**D3 - second concept (-ing)** [region A]: the Cov^-1 preprocessing gain
(Q2: cau_unemb better than euc_unemb) **replicates on the second concept**:
gemma-1b 3/3 seeds +0.09..+0.11 (CIs exclude 0), gpt2 +0.628 [+0.491,+0.776]
=> 4/4 new independent units, consistent with the 7/7 units of concept
"third" from V3 (now counted correctly). Q3 on -ing: fixed better 3/3
(-0.92..-1.08, CIs exclude 0) - consistent with concept "third".
ctx/dmd rows on -ing carry the frame confound and are reported but not
concluded on.

**Q2 region dependence**: in region C (concept third) Q2 drops to +0.045..+0.112
with CIs crossing 0 in 2/3 seeds (s1 excludes 0) - direction consistent, not
established; the preprocessing gain established in region A is thus
regime-dependent (it shrinks when starts are already concentrated, cf0~0.92).

## 3. Optimality gap (R3)

- Implementation equivalence extends to region C: first-step direction cosine
  vs the author's cg_solve = 1.000000 on a natural-text context
  (repro_check_c4.json; task-doc decision-tree requirement for the C1-reversal
  branch).
- No method is at its hyperplane optimum: gaps are 1.3-7.9 across all 9
  methods (gemma-1b 3 seeds + gpt2, 5 optgap runs, 180 rows each; >=95% rows
  gap >= -0.01: 100%/100%/100%/99.4% at 5e-3, 100% at 1e-1). dua_ctx has the
  largest gap (5.3-7.9); euc/cau methods sit at 1.5-3.9.
- Probe-invariance is strongly violated: the KL-optimal point on each
  method's endpoint hyperplane has P1_opt ~ 0.005-0.07 (vs P1_end ~ 0.9) -
  holding the probe projection fixed does NOT hold the concept.

## 4. Cost (R5)

Adaptive steering costs ~3-20x the Euclidean direction of the same probe:
gemma-1b 0.85-3.21 s/context vs 0.14-0.30 (6-11x); gemma-4b 2.4-18.0 vs
0.26-0.92 (3-20x); per-step ~4x plus more steps. The fixed causal metric adds
only a one-time S0 computation and a single solve (timing indistinguishable
from Euclidean: 0.14-0.16 s/ctx on gemma-1b).

## 5. Decision-tree outcomes (task doc section 7)

- C1 reversed in region C at Park's alpha, with WP1 equivalence re-verified
  on region-C contexts => the reversal is a property of the setting
  (concentrated starts + alpha), consistent with Park section 5.3's own
  remark; "adaptive advantage depends on the concentration of the starting
  distribution" is the dose-response reading (min_mass 0.5 in V3 and region C
  here both shrink/reverse it; alpha >= 2e-2 restores it in 3/3 seeds).
- No "contact the author" action has been taken yet (see repro_check.md
  addendum); the missing-F-import report is drafted for a GitHub issue.

## 6. Corrections to V3 wording (task doc section 8)

1. "27 grid runs all positive" -> 7 independent (model, seed) units were all
   positive (fixed methods are alpha-independent; runs at different alphas on
   the same unit are not independent).
2. "19/19 point estimates positive (Q1)" -> per-unit counting: region A
   concept third: 3/3 units positive (CI excluding 0 in 2/3).
3. "at alpha 1e-1 within the margin" (Q3) -> point estimates within margin in
   2/3 seeds; interval-based practical equivalence in 0/3 (upper bounds up to
   +0.089/+0.141 exceed +-0.05).
4. "adaptive methods have the best pair mass (cf)" -> withdrawn; cf has no
   direction. Correct statement: adaptive methods have the smallest cf_dev
   (least pair-mass drift) while their kl is higher - the cost sits in kl_neu.
5. "adaptive advantage concentrates in less peaked starts" -> now supported
   by dose-response (min_mass 0.15/0.5 gradient in V3) AND region C (natural
   text, cf0~0.92, reversal at 5e-3).
6. "margin of 5%" -> the +-0.05 equivalence margin is a PROPOSED value, not
   yet confirmed by Victor; all equivalence labels above are conditional on
   it.

## 7. Limitations

Two concepts, one model family per region (region C only on gemma-1b), gemma-4b
4-bit and only at 5e-3 in region A; rd is the simplified start-set variant; KL
floor 1e-12 vs the authors' 5e-3 offset (absolute KL not comparable to theirs);
step size eta = 0.01*||lambda_0|| and stop at 0.99 vs authors' absolute steps
and 0.9999 stop; the -ing concept's ctx/dmd probes carry an auxiliary-verb
frame confound; alpha=5e-3's correspondence to the authors' checkpoint is
unverified; region C clusters are C4 document ids (>=30 docs satisfied);
multiplicity uncorrected.
