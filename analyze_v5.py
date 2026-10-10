"""
analyze_v5.py - final analyses for the steering study (reads the CSVs written by steer_compare_v5.py)

Usage example:
  python analyze_v5.py --out results_v5 \
     --group A_third_a5e-3 runs/gemma1b_v5/s0_abs5e-3,runs/gemma1b_v5/s1_abs5e-3,runs/gemma1b_v5/s2_abs5e-3 \
     --group C_third_a5e-3 runs/gemma1b_v5/c4_s0_abs5e-3,runs/gemma1b_v5/c4_s1_abs5e-3,runs/gemma1b_v5/c4_s2_abs5e-3 \
     --pairs euc_dmd:dua_dmd,cau_unemb:dua_unemb

Outputs (in --out):
  advantage_regression.csv   per-context regression of the adaptive advantage on start-point features
  predictor_corr.csv         correlation among predictors (collinearity check)
  capture_ratio.csv          fraction of the Euclid->adaptive change reproduced by the fixed (cau) and frequency-weighted (frq) metrics
  null_control_summary.csv   real vs random-probe control at the same path length
  metric_panel.csv           paired differences for kl, kl_park, rd, cf_dev, kl_neu per run (sign consistency across units)
  analysis_v5.md             the same tables as markdown (auto-generated; no hand-edited numbers)
Convention: diff = metric(a) - metric(b); for every metric used here LOWER is better, so diff > 0 means b is better.
"""
import argparse, os, json, itertools
import numpy as np, pandas as pd

METRICS = ["kl", "kl_park", "rd", "cf_dev", "kl_neu"]
PRED = {"H0": lambda f: f["H0"], "cf0": lambda f: f["cf0"], "log_pr": lambda f: np.log(f["sigma_pr"].clip(lower=1e-9))}


def load_run(r, level):
    pc = pd.read_csv(f"{r}/per_context.csv"); pc = pc[(pc.level == level) & (pc.reached == 1)]
    ft = pd.read_csv(f"{r}/ctx_features.csv"); return pc, ft


def pair_frame(r, a, b, level, metrics):
    pc, ft = load_run(r, level)
    A = pc[pc.method == a].set_index("ctx_id"); B = pc[pc.method == b].set_index("ctx_id"); ids = A.index.intersection(B.index)
    out = pd.DataFrame({"ctx_id": ids})
    for m in metrics:
        if m in A.columns: out[m] = (A.loc[ids, m] - B.loc[ids, m]).values
    out = out.merge(ft[["ctx_id", "cluster", "H0", "cf0", "sigma_pr"]], on="ctx_id", how="left"); out["run"] = r
    out["cl"] = r + "|" + out["cluster"].astype(str); return out


def cluster_boot_coef(X, y, cl, B, rng):
    """OLS (with intercept) coefficients with a cluster bootstrap over clusters. X: (n,p) already standardized."""
    cls = np.unique(cl); idx = {c: np.where(cl == c)[0] for c in cls}; Xd = np.c_[np.ones(len(y)), X]
    beta = np.linalg.lstsq(Xd, y, rcond=None)[0]; bs = []
    for _ in range(B):
        pick = rng.choice(cls, len(cls), replace=True); ii = np.concatenate([idx[c] for c in pick])
        bs.append(np.linalg.lstsq(Xd[ii], y[ii], rcond=None)[0])
    bs = np.array(bs); r2 = 1 - ((y - Xd @ beta) ** 2).sum() / max(((y - y.mean()) ** 2).sum(), 1e-12)
    return beta[1:], np.quantile(bs[:, 1:], 0.025, axis=0), np.quantile(bs[:, 1:], 0.975, axis=0), r2


def capture_ratio(runs, probe, metric, level, boot, rng):
    """rho = mean(euc - X) / mean(euc - dua): fraction of the Euclid->adaptive change reproduced by method X (cau / frq).
    1 = same as adaptive, 0 = same as Euclid. Only meaningful when the Euclid->adaptive gap is itself non-zero (CI excludes 0)."""
    parts = []
    for r in runs:
        pc, ft = load_run(r, level); w = pc.pivot_table(index="ctx_id", columns="method", values=metric)
        need = [f"euc_{probe}", f"cau_{probe}", f"dua_{probe}"]
        if not all(c in w.columns for c in need): return None
        w = w.dropna(subset=need).join(ft.set_index("ctx_id")["cluster"]); w["cl"] = r + "|" + w["cluster"].astype(str); parts.append(w)
    w = pd.concat(parts); cl = w["cl"].values; cls = np.unique(cl); idx = {c: np.where(cl == c)[0] for c in cls}
    E, D, C = w[f"euc_{probe}"].values, w[f"dua_{probe}"].values, w[f"cau_{probe}"].values
    Fq = w[f"frq_{probe}"].values if f"frq_{probe}" in w.columns and w[f"frq_{probe}"].notna().all() else None
    def stat(ii):
        gap = (E[ii] - D[ii]).mean(); out = [gap, (E[ii] - C[ii]).mean() / gap if gap != 0 else np.nan]
        out.append((E[ii] - Fq[ii]).mean() / gap if (Fq is not None and gap != 0) else np.nan); return out
    base = stat(np.arange(len(E))); bs = np.array([stat(np.concatenate([idx[c] for c in rng.choice(cls, len(cls), replace=True)])) for _ in range(boot)])
    q = lambda k: (round(float(np.nanquantile(bs[:, k], .025)), 4), round(float(np.nanquantile(bs[:, k], .975)), 4))
    gl, gh = q(0); return [len(E), round(float(base[0]), 5), gl, gh, bool(gl > 0 or gh < 0), round(float(base[1]), 4), *q(1), round(float(base[2]), 4) if Fq is not None else np.nan, *(q(2) if Fq is not None else (np.nan, np.nan))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--group", nargs=2, action="append", metavar=("NAME", "RUNS"), required=True)
    ap.add_argument("--pairs", default="euc_dmd:dua_dmd,cau_unemb:dua_unemb"); ap.add_argument("--level", type=float, default=0.9)
    ap.add_argument("--out", default="results_v5"); ap.add_argument("--boot", type=int, default=2000); ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    # security guard (WP-7, pre-commit hook finding): --out must resolve inside this repository
    # (no path traversal); input run dirs are read-only and stay CLI-controlled.
    _root = os.path.dirname(os.path.abspath(__file__))
    _out = os.path.abspath(a.out)
    if _out != _root and not _out.startswith(_root + os.sep):
        raise SystemExit(f"--out must stay inside the repository: {a.out!r}")
    a.out = _out
    os.makedirs(a.out, exist_ok=True); rng = np.random.default_rng(a.seed)
    pairs = [tuple(p.split(":")) for p in a.pairs.split(",")]
    reg_rows, corr_rows, null_rows, panel_rows, cap_rows = [], [], [], [], []
    for gname, runs in a.group:
        runs = runs.split(",")
        for (pa, pb) in pairs:
            fr = pd.concat([pair_frame(r, pa, pb, a.level, METRICS) for r in runs], ignore_index=True).dropna(subset=["H0", "cf0", "sigma_pr"])
            if len(fr) < 20: continue
            # run fixed effects: demean y and x within run; scale x by pooled SD
            X = pd.DataFrame({k: f(fr) for k, f in PRED.items()}); Xc = X - X.groupby(fr["run"]).transform("mean"); Xs = Xc / Xc.std(ddof=0).replace(0, 1)
            corr = Xs.corr(); [corr_rows.append([gname, pa, pb, i, j, round(float(corr.loc[i, j]), 3)]) for i, j in itertools.combinations(corr.columns, 2)]
            for met in METRICS:
                if met not in fr: continue
                y = fr[met] - fr[met].groupby(fr["run"]).transform("mean"); ok = y.notna(); cl = fr["cl"].values[ok.values]
                for setname, cols in [(f"uni_{c}", [c]) for c in PRED] + [("joint", list(PRED))]:
                    co, lo, hi, r2 = cluster_boot_coef(Xs.loc[ok, cols].values, y[ok].values, cl, a.boot, rng)
                    for k, c in enumerate(cols):
                        reg_rows.append([gname, f"{pa} - {pb}", met, setname, c, round(float(co[k]), 5), round(float(lo[k]), 5), round(float(hi[k]), 5),
                                         round(float(r2), 4), int(ok.sum()), int(len(np.unique(cl)))])
            # metric panel per run (sign consistency across independent units)
            for r in runs:
                p = pair_frame(r, pa, pb, a.level, METRICS); cl = p["cl"].values
                for met in METRICS:
                    if met not in p or p[met].notna().sum() < 5: continue
                    v = p[met].values; cls = np.unique(cl); idx = {c: np.where(cl == c)[0] for c in cls}
                    bs = [np.concatenate([v[idx[c]] for c in rng.choice(cls, len(cls), replace=True)]).mean() for _ in range(a.boot)]
                    panel_rows.append([gname, r, f"{pa} - {pb}", met, round(float(v.mean()), 5), round(float(np.quantile(bs, .025)), 5), round(float(np.quantile(bs, .975)), 5), len(v)])
        for probe in ("ctx", "unemb", "dmd"):
            for met in METRICS:
                c_ = capture_ratio(runs, probe, met, a.level, a.boot, rng)
                if c_: cap_rows.append([gname, probe, met] + c_)
        # random-probe control
        for r in runs:
            fn = f"{r}/null_control.csv"
            if not os.path.exists(fn): continue
            nc = pd.read_csv(fn); pc, ft = load_run(r, a.level); ft = ft.set_index("ctx_id")
            nm = nc.groupby(["ctx_id", "method"])[["kl", "kl_park", "rd", "cf_dev", "kl_neu", "P1_end"]].mean().reset_index()
            m = nm.merge(pc[["ctx_id", "method", "kl", "kl_park", "rd", "cf_dev", "kl_neu", "P1"]], on=["ctx_id", "method"], suffixes=("_null", "_real"))
            m["cl"] = r + "|" + m["ctx_id"].map(ft["cluster"]).astype(str)
            for meth, g in m.groupby("method"):
                row = [gname, r, meth, len(g)]
                for met in ["kl", "kl_park", "rd", "cf_dev", "kl_neu"]:
                    real, nul = g[met + "_real"].values, g[met + "_null"].values; d = real - nul; cls = np.unique(g["cl"].values); idx = {c: np.where(g["cl"].values == c)[0] for c in cls}
                    bs = [np.concatenate([d[idx[c]] for c in rng.choice(cls, len(cls), replace=True)]).mean() for _ in range(a.boot)] if len(cls) > 2 else [np.nan, np.nan]
                    row += [round(float(real.mean()), 4), round(float(nul.mean()), 4), round(float(d.mean()), 4), round(float(np.nanquantile(bs, .025)), 4), round(float(np.nanquantile(bs, .975)), 4)]
                row += [round(float(g["P1_null"].mean()), 4) if "P1_null" in g else round(float(g["P1_end"].mean()), 4) if "P1_end" in g else np.nan]
                null_rows.append(row)
    cols_n = ["group", "run", "method", "n_ctx"] + [f"{m}_{s}" for m in ["kl", "kl_park", "rd", "cf_dev", "kl_neu"] for s in ["real", "null", "real_minus_null", "lo", "hi"]] + ["P1_null_end"]
    pd.DataFrame(reg_rows, columns=["group", "pair(a-b)", "metric", "model", "term", "coef_per_SD", "lo", "hi", "R2", "n", "n_clusters"]).to_csv(f"{a.out}/advantage_regression.csv", index=False)
    pd.DataFrame(corr_rows, columns=["group", "a", "b", "pred_i", "pred_j", "corr"]).to_csv(f"{a.out}/predictor_corr.csv", index=False)
    pd.DataFrame(cap_rows, columns=["group", "probe", "metric", "n", "gap_euc_minus_dua", "gap_lo", "gap_hi", "gap_defined", "rho_cau", "rho_cau_lo", "rho_cau_hi", "rho_frq", "rho_frq_lo", "rho_frq_hi"]).to_csv(f"{a.out}/capture_ratio.csv", index=False)
    pd.DataFrame(null_rows, columns=cols_n).to_csv(f"{a.out}/null_control_summary.csv", index=False)
    pd.DataFrame(panel_rows, columns=["group", "run", "pair(a-b)", "metric", "diff_mean", "lo", "hi", "n"]).to_csv(f"{a.out}/metric_panel.csv", index=False)
    # sink restructured for the pre-commit security scan (static CWE-22 check on open() with a
    # variable path, WP-7 / DEVIATIONS V5.12): build the markdown in memory and write once via
    # pathlib into the already-validated a.out; output bytes identical to the previous open()/write loop.
    from pathlib import Path
    _md = ["# analysis_v5 (auto-generated)\n\nconvention: diff = a - b; lower is better for every metric; diff > 0 means b (adaptive) is better.\n\n"]
    for nme in ["metric_panel", "capture_ratio", "advantage_regression", "predictor_corr", "null_control_summary"]:
        d = pd.read_csv(os.path.join(a.out, f"{nme}.csv")); _md.append(f"## {nme}\n\n" + (d.to_markdown(index=False) if len(d) else "(empty)") + "\n\n")
    Path(a.out, "analysis_v5.md").write_text("".join(_md))
    print("wrote", a.out)


if __name__ == "__main__":
    main()
