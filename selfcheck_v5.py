"""
selfcheck_v5.py - automated delivery checks. Run before every submission.

  python selfcheck_v5.py --runs "runs/gemma1b_v5/*" "runs/gpt2_v5/*" [--ref_from _v5 --ref_to _v4] [--min_ctx 60]

For every run directory it checks:
  F1 required files exist (null_control.csv only if config says null_draws > 0)
  F2 KL identity: |kl - (kl_bin + kl_pair + kl_neu)| <= 1e-4 on all reached rows
  F3 ctx_features.csv has one row per steered context; sigma_pr in [1, d]; no NaN in H0/cf0
  F4 guardrails from checks.json: logits_rel_err <= 5e-2, probe_heldout_auc >= 0.8, n_steered >= --min_ctx
  F5 cluster bootstrap in use and n_clusters >= --min_clusters
  F6 reach_rate printed for every method at level 0.9 (warn if < 0.8)
  F7 (optional, --ref_from/--ref_to) regression: shared numeric columns of summary.csv / per_context.csv equal the reference run with the
     same relative path within 1e-6  (reference = the corresponding V4 output)
Exit code 1 if any FAIL.
"""
import argparse, glob, json, os, sys
import numpy as np, pandas as pd
from pandas.api.types import is_numeric_dtype

REQ = ["config.json", "checks.json", "summary.csv", "paired_long.csv", "per_context.csv", "final.csv", "ctx_features.csv", "timing.csv"]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--runs", nargs="+", required=True); ap.add_argument("--ref_from", default=None, help="substring of the run path to replace, e.g. _v5"); ap.add_argument("--ref_to", default=None, help="replacement giving the reference (V4) run path, e.g. _v4")
    ap.add_argument("--min_ctx", type=int, default=60); ap.add_argument("--min_clusters", type=int, default=12)
    a = ap.parse_args(); dirs = sorted({d for p in a.runs for d in glob.glob(p) if os.path.isdir(d)}); fails = 0; warns = 0
    def F(ok, run, msg):
        nonlocal fails
        if not ok: fails += 1; print(f"FAIL {run}: {msg}")
    for r in dirs:
        miss = [f for f in REQ if not os.path.exists(f"{r}/{f}")]; F(not miss, r, f"F1 missing {miss}")
        if miss: continue
        cfg = json.load(open(f"{r}/config.json")); chk = json.load(open(f"{r}/checks.json")); d = cfg["d"]
        if cfg["args"].get("null_draws", 0) > 0: F(os.path.exists(f"{r}/null_control.csv"), r, "F1 null_control.csv missing")
        pc = pd.read_csv(f"{r}/per_context.csv"); pr = pc[pc.reached == 1]
        if len(pr): F((pr.kl - (pr.kl_bin + pr.kl_pair + pr.kl_neu)).abs().max() <= 1e-4, r, "F2 KL identity violated")
        ft = pd.read_csv(f"{r}/ctx_features.csv")
        F(len(ft) == chk["n_steered"], r, f"F3 ctx_features rows {len(ft)} != n_steered {chk['n_steered']}")
        F(ft.sigma_pr.between(1 - 1e-6, d + 1e-6).all() and ft[["H0", "cf0"]].notna().all().all(), r, "F3 sigma_pr out of [1,d] or NaN features")
        F((chk.get("logits_rel_err") or 0) <= 5e-2, r, f"F4 logits_rel_err {chk.get('logits_rel_err')}")
        F(chk["probe_heldout_auc"] >= 0.8, r, f"F4 probe AUC {chk['probe_heldout_auc']:.3f}")
        F(chk["n_steered"] >= a.min_ctx, r, f"F4 n_steered {chk['n_steered']} < {a.min_ctx}")
        F(chk.get("ci_type") == "cluster", r, "F5 not cluster bootstrap")
        ncl = (chk.get("v5") or {}).get("n_clusters", 0); F(ncl >= a.min_clusters, r, f"F5 n_clusters {ncl} < {a.min_clusters}")
        s = pd.read_csv(f"{r}/summary.csv"); low = s[(s.level == 0.9) & (s.reach_rate < 0.8)]
        for _, row in low.iterrows(): warns += 1; print(f"WARN {r}: F6 reach_rate {row.reach_rate:.2f} for {row.method} at 0.9")
        if a.ref_from:
            ref = r.replace(a.ref_from, a.ref_to)
            if ref != r and os.path.exists(f"{ref}/summary.csv"):
                for fn in ("summary.csv", "per_context.csv"):
                    x, y = pd.read_csv(f"{r}/{fn}"), pd.read_csv(f"{ref}/{fn}"); cols = [c for c in y.columns if c in x.columns]
                    F(len(x) == len(y), r, f"F7 {fn} row count differs from reference")
                    if len(x) == len(y):
                        mx = max([np.nanmax(np.abs(x[c].values - y[c].values)) for c in cols if is_numeric_dtype(x[c]) and is_numeric_dtype(y[c])] + [0])
                        F(mx <= 1e-6, r, f"F7 {fn} max abs diff vs reference {mx:.2e}")
            else: warns += 1; print(f"WARN {r}: F7 no reference at {ref}")
        print(f"ok   {r}")
    print(f"\n{len(dirs)} runs checked, {fails} FAIL, {warns} WARN"); sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
