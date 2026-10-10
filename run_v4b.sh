#!/usr/bin/env bash
# V4 batch stage 1b + 2: optgap convergence fix reruns, then WP-D (C4) + WP-E (-ing)
set -uo pipefail
PY=/home/administrator/dev/ML/lrg_env/bin/python
STAGE() { echo "=== [$(date +%H:%M:%S)] $1 ==="; }

STAGE "optgap reruns with hyperplane_min iters=120 (task-doc remedy; see DEVIATIONS V4.3)"
rm -rf runs/gemma1b_v4/optgap_s0_abs5e-3 runs/gemma1b_v4/optgap_s1_abs5e-3 runs/gemma1b_v4/optgap_s2_abs5e-3 runs/gpt2_v4/optgap_s0_abs5e-3
$PY steer_compare_v4.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed 0 --out runs/gemma1b_v4/optgap_s0_abs5e-3
$PY steer_compare_v4.py --data_dir data/gemma1b_s1 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed 1 --out runs/gemma1b_v4/optgap_s1_abs5e-3
$PY steer_compare_v4.py --data_dir data/gemma1b_s2 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed 2 --out runs/gemma1b_v4/optgap_s2_abs5e-3
$PY steer_compare_v4.py --data_dir data/gpt2_s0 --backend torch --topk 5000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed 0 --out runs/gpt2_v4/optgap_s0_abs5e-3

STAGE "WP-D: C4 extraction, gemma-1b seeds 0/1/2 (5000 docs each)"
for S in 0 1 2; do
  [ -f data/gemma1b_c4_s$S/G.npy ] || $PY extract_embeddings.py --model google/gemma-3-1b-pt --dtype bfloat16 --seed $S --ctx_source c4 --c4_docs 5000 --out_dir data/gemma1b_c4_s$S
done

STAGE "WP-D: region C runs (park filter), 3 seeds x 3 alphas"
for S in 0 1 2; do
  for A in 5e-3 2e-2 1e-1; do
    [ -f runs/gemma1b_v4/c4_s${S}_abs${A}/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma1b_c4_s$S --backend torch --topk 20000 --methods grid --filter park --park_mass 0.7 --park_k 3 --alpha_abs $A --n_ctx 60 --seed $S --out runs/gemma1b_v4/c4_s${S}_abs${A}
  done
done

STAGE "WP-E: -ing concept extraction (templates), gemma-1b seeds 0/1/2 + gpt2 seed 0"
for S in 0 1 2; do
  [ -f data/gemma1b_ing_s$S/G.npy ] || $PY extract_embeddings.py --model google/gemma-3-1b-pt --dtype bfloat16 --seed $S --concept ing --out_dir data/gemma1b_ing_s$S
done
[ -f data/gpt2_ing_s0/G.npy ] || $PY extract_embeddings.py --model gpt2 --dtype float32 --seed 0 --concept ing --out_dir data/gpt2_ing_s0

STAGE "WP-E: -ing runs (region A, alpha 5e-3)"
for S in 0 1 2; do
  [ -f runs/gemma1b_v4/ing_s${S}_abs5e-3/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma1b_ing_s$S --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed $S --out runs/gemma1b_v4/ing_s${S}_abs5e-3
done
[ -f runs/gpt2_v4/ing_s0_abs5e-3/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gpt2_ing_s0 --backend torch --topk 5000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --out runs/gpt2_v4/ing_s0_abs5e-3

STAGE "STAGE 2 COMPLETE"
