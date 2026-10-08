#!/usr/bin/env bash
# usage: bash run_all.sh <hf_model> <tag> ["<extract args>"] ["<steer args>"]
# e.g.   bash run_all.sh gpt2 gpt2 "--dtype float32" "--topk 5000"
#        bash run_all.sh google/gemma-3-1b-pt gemma1b "--dtype bfloat16" "--topk 20000 --backend torch"
set -euo pipefail
MODEL=${1:?hf model}; TAG=${2:?tag}; EXT=${3:-}; STE=${4:-}
[ -f data/$TAG/G.npy ] || python extract_embeddings.py --model "$MODEL" --out_dir data/$TAG $EXT
for A in 0.001 0.01 0.1; do
  python steer_compare.py --data_dir data/$TAG --alpha_rel $A --seed 0 --out runs/$TAG/alpha${A}_seed0 $STE
done
echo "done. results in runs/$TAG/*/{summary.csv,paired.csv,curves.png,report.md}"
