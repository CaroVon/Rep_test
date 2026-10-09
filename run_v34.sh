#!/usr/bin/env bash
# WP4 + WP5 batch (commands mirrored in commands.log)
set -uo pipefail
PY=/home/administrator/dev/ML/lrg_env/bin/python
STAGE() { echo "=== [$(date +%H:%M:%S)] $1 ==="; }

STAGE "WP4 extraction: gemma-1b seeds 0/1/2 (expanded templates)"
for S in 0 1 2; do
  [ -f data/gemma1b_s$S/G.npy ] || $PY extract_embeddings.py --model google/gemma-3-1b-pt --dtype bfloat16 --seed $S --out_dir data/gemma1b_s$S
done
STAGE "WP4 extraction: gpt2 seeds 0/1/2 (expanded templates)"
for S in 0 1 2; do
  [ -f data/gpt2_s$S/G.npy ] || $PY extract_embeddings.py --model gpt2 --dtype float32 --seed $S --out_dir data/gpt2_s$S
done

STAGE "WP4 gemma-1b final grid: 3 seeds x 3 alphas, n_ctx=60"
for S in 0 1 2; do
  for A in 5e-3 2e-2 1e-1; do
    [ -f runs/gemma1b_v3/s${S}_abs${A}/summary.csv ] || $PY steer_compare_v3.py --data_dir data/gemma1b_s$S --backend torch --topk 20000 --methods grid --alpha_abs $A --n_ctx 60 --seed $S --out runs/gemma1b_v3/s${S}_abs${A}
  done
done

STAGE "WP4 gpt2 grid: 3 seeds x 3 alphas, n_ctx=60, ridge 1e-6 (default)"
for S in 0 1 2; do
  for A in 5e-3 2e-2 1e-1; do
    [ -f runs/gpt2_v3/s${S}_abs${A}/summary.csv ] || $PY steer_compare_v3.py --data_dir data/gpt2_s$S --backend torch --topk 5000 --methods grid --alpha_abs $A --n_ctx 60 --seed $S --out runs/gpt2_v3/s${S}_abs${A}
  done
done

STAGE "WP5 robustness on gemma1b_s0, alpha 5e-3, n_ctx=60"
$PY steer_compare_v3.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --ridge_rel 1e-8 --out runs/gemma1b_v3/rob_ridge1e-8
$PY steer_compare_v3.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --ridge_rel 1e-4 --out runs/gemma1b_v3/rob_ridge1e-4
$PY steer_compare_v3.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --min_mass 0.5 --out runs/gemma1b_v3/rob_mm0.5
$PY steer_compare_v3.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --min_mass 0.7 --out runs/gemma1b_v3/rob_mm0.7
$PY steer_compare_v3.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --step_frac 0.02 --max_steps 1200 --out runs/gemma1b_v3/rob_sf0.02ms1200

STAGE "WP4.4 gemma-4b (4-bit): re-extract with expanded templates seed 0, alpha 5e-3 only"
[ -f data/gemma4b_s0/G.npy ] || $PY extract_embeddings.py --model google/gemma-3-4b-pt --dtype bfloat16 --load_in_4bit --seed 0 --out_dir data/gemma4b_s0
$PY steer_compare_v3.py --data_dir data/gemma4b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --out runs/gemma4b_v3/s0_abs5e-3

STAGE "BATCH COMPLETE"
