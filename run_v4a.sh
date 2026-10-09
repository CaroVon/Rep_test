#!/usr/bin/env bash
# V4 batch stage 1: WP-A1 regression reruns + WP-C optgap runs
set -uo pipefail
PY=/home/administrator/dev/ML/lrg_env/bin/python
STAGE() { echo "=== [$(date +%H:%M:%S)] $1 ==="; }

# the regression probe run already used exactly these params - reuse it
[ -d runs/gemma1b_v4/s0_abs5e-3 ] || mv runs/gemma1b_v4/regress_s0_abs5e-3 runs/gemma1b_v4/s0_abs5e-3

STAGE "WP-A1: gemma-1b 3 seeds x 3 alphas (v4, identical params to V3)"
for S in 0 1 2; do
  for A in 5e-3 2e-2 1e-1; do
    [ -f runs/gemma1b_v4/s${S}_abs${A}/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma1b_s$S --backend torch --topk 20000 --methods grid --alpha_abs $A --n_ctx 60 --seed $S --filter mass --min_mass 0.15 --out runs/gemma1b_v4/s${S}_abs${A}
  done
done

STAGE "WP-A1: gpt2 3 seeds x 3 alphas"
for S in 0 1 2; do
  for A in 5e-3 2e-2 1e-1; do
    [ -f runs/gpt2_v4/s${S}_abs${A}/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gpt2_s$S --backend torch --topk 5000 --methods grid --alpha_abs $A --n_ctx 60 --seed $S --filter mass --min_mass 0.15 --out runs/gpt2_v4/s${S}_abs${A}
  done
done

STAGE "WP-A1: gemma-4b seed 0, alpha 5e-3"
[ -f runs/gemma4b_v4/s0_abs5e-3/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma4b_s0 --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --seed 0 --filter mass --min_mass 0.15 --out runs/gemma4b_v4/s0_abs5e-3

STAGE "WP-C: optgap runs"
for A in 5e-3 1e-1; do
  [ -f runs/gemma1b_v4/optgap_s0_abs${A}/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma1b_s0 --backend torch --topk 20000 --methods grid --alpha_abs $A --n_ctx 60 --optgap 20 --seed 0 --out runs/gemma1b_v4/optgap_s0_abs${A}
done
for S in 1 2; do
  [ -f runs/gemma1b_v4/optgap_s${S}_abs5e-3/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gemma1b_s$S --backend torch --topk 20000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed $S --out runs/gemma1b_v4/optgap_s${S}_abs5e-3
done
[ -f runs/gpt2_v4/optgap_s0_abs5e-3/summary.csv ] || $PY steer_compare_v4.py --data_dir data/gpt2_s0 --backend torch --topk 5000 --methods grid --alpha_abs 5e-3 --n_ctx 60 --optgap 20 --seed 0 --out runs/gpt2_v4/optgap_s0_abs5e-3

STAGE "STAGE 1 COMPLETE"
