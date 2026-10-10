"""WP-5: generate runs/AGGREGATE_V5.md (all tables and numbers) from the V5 run outputs.

Usage: python aggregate_v5.py
Every number in the generated markdown is read from CSV/JSON files by this script;
nothing is hand-typed. Conclusions live in a SEPARATE file (CONCLUSIONS_V5.md) that
this script never touches.
Independent unit = (model, seed, concept, region) per task doc section 1 rule 6.
Sections follow FINAL_EXPERIMENT_PROMPT_V5.md section 5 (WP-5), 1-8.
"""
import json, os, glob, re
from pathlib import Path
import numpy as np
import pandas as pd

L0 = 0.9
METHODS = ["euc_ctx", "cau_ctx", "frq_ctx", "dua_ctx", "euc_unemb", "cau_unemb", "frq_unemb", "dua_unemb",
           "euc_dmd", "cau_dmd", "frq_dmd", "dua_dmd"]
PANEL_METRICS = ["kl", "kl_park", "rd", "cf_dev", "kl_neu"]
CONFIRM = [("euc_dmd", "dua_dmd", "C1"), ("cau_unemb", "dua_unemb", "C2")]
AN = "results_v5/full"          # analyze_v5.py full output (source of sections 3-6)
ALPHA_MAIN = 0.005


def runs_in(pattern):
    return sorted(d for d in glob.glob(pattern) if os.path.exists(f"{d}/summary.csv"))


def meta_of(d):
    cfg = json.load(open(f"{d}/config.json"))
    chk = json.load(open(f"{d}/checks.json"))
    dd = cfg["args"]["data_dir"] or "synthetic"
    model = ("synthetic" if dd == "synthetic" else "gemma-1b" if "gemma1b" in dd else
             "gemma-4b" if "gemma4b" in dd else "gpt2" if "gpt2" in dd else dd)
    concept = "ing" if re.search(r"_ing_", dd) else "syn" if dd == "synthetic" else "third"
    region = "C" if chk.get("filter") == "park" else "A"
    name = os.path.basename(d)
    if name.startswith("syn_v5"):
        typ = "WP-0 parity (synthetic)"
    elif not cfg["args"].get("with_freq"):
        typ = "WP-1 regression vs V4"
    elif model == "gemma-1b" and re.fullmatch(r"[AC]_s\d_abs5e-3", name):
        typ = "P0"
    elif model == "gemma-4b" or concept == "ing":
        typ = "P2"
    else:  # alpha 2e-2 runs, Cbig runs, gpt2 A runs
        typ = "P1"
    H0 = pd.read_csv(f"{d}/ctx_features.csv")["H0"]
    return dict(dir=d, name=name, model=model, seed=cfg["args"]["seed"], alpha=cfg["args"].get("alpha_abs"),
                concept=concept, region=region, type=typ, chk=chk, cfg=cfg, runtime=cfg.get("runtime_s"),
                H0_mean=float(H0.mean()), n_ctx=len(H0))


def fmt(t, nd=3):
    if t is None or not np.isfinite(t[0]):
        return "n/a"
    return f"{t[0]:.{nd}f} [{t[1]:.{nd}f},{t[2]:.{nd}f}]"


def cell(row, m, nd=3):
    """mean [lo,hi] with an (ns) marker when the interval crosses zero."""
    if row is None or not np.isfinite(row[m]):
        return "n/a"
    s = f"{row[m]:.{nd}f} [{row[f'lo']:.{nd}f},{row[f'hi']:.{nd}f}]"
    return s + (" (ns)" if row["lo"] <= 0 <= row["hi"] else "")


def ratio(num, den):
    return f"{num / den:.2f}" if (den is not None and np.isfinite(den) and den != 0 and num is not None and np.isfinite(num)) else "n/a"


# ---------------------------------------------------------------- section 1
def section1(R, L):
    L.append("## 1. 数据与检验（全部已运行的 V5 run）")
    L.append("")
    L.append("来源：各 run 的 `config.json`、`checks.json`、`ctx_features.csv`。"
             "`H0 mean` = 该 run `ctx_features.csv` 全部测试上下文 `H0` 的均值；`cf0_mean` = `checks.json` 的 `cf0_mean_test`。")
    L.append("")
    L.append("| run | type | model | region | concept | seed | alpha | logits_rel_err | probe AUC | base kept | target kept | n_ctx | n_clusters | cf0_mean | H0 mean |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in sorted(R, key=lambda x: (x["type"], x["model"], x["region"], x["concept"], x["seed"], str(x["alpha"]))):
        c = r["chk"]
        auc = c.get("probe_heldout_auc"); lre = c.get("logits_rel_err")
        L.append(f"| `{r['dir']}` | {r['type']} | {r['model']} | {r['region']} | {r['concept']} | {r['seed']} | {r['alpha']} | "
                 f"{lre:.2e} | {auc:.5g} | {c.get('n_base_kept')}/{c.get('n_base_raw')} | {c.get('n_target_kept')}/{c.get('n_target_raw')} | "
                 f"{r['n_ctx']} | {c.get('v5', {}).get('n_clusters', 'n/a')} | {c.get('cf0_mean_test'):.3f} | {r['H0_mean']:.3f} |")
    L.append("")
    L.append("说明：`WP-1 regression vs V4` 两个 run 不带 `--with_freq`/null（与 V4 同参数，用于回归对比）；"
             "其余真实模型 run 均带 `--with_freq`，α=5e-3 的 run 另带 `--null_draws 3 --null_ctx 30`。"
             "区域 C 的两个数据集：`C_s*` 用 V4 已有 `data/gemma1b_c4_s{S}`，`Cbig_s*` 用 P1 扩大提取的 `data/gemma1b_c4big_s{S}`。")
    L.append("")


# ---------------------------------------------------------------- section 2
def num_diff(a, b, keys, label):
    """NaN-aware max-abs-diff between two frames merged on keys, over shared numeric columns."""
    shared = [c for c in a.columns if c in b.columns and c not in keys]
    num = [c for c in shared if pd.api.types.is_numeric_dtype(a[c]) and pd.api.types.is_numeric_dtype(b[c])]
    m = a[keys + num].merge(b[keys + num], on=keys, suffixes=("_a", "_b"))
    A = m[[f"{c}_a" for c in num]].values; B = m[[f"{c}_b" for c in num]].values
    nan_mm = int((np.isnan(A) != np.isnan(B)).sum()) if m.size else 0
    ok = ~np.isnan(A) & ~np.isnan(B)
    mx = float(np.abs(A[ok] - B[ok]).max()) if ok.any() else 0.0
    return dict(file=label, n_rows=len(m), n_cols=len(num), nan_mm=nan_mm, mx=mx)


def section2(R, L):
    L.append("## 2. 回归对比（WP-1：与 V4 逐列差；及 WP-0 双后端对等）")
    L.append("")
    L.append("### 2a. WP-1：V5 脚本按 V4 同参数重跑 vs V4 输出（共有数值列，NaN 模式感知；门槛 ≤1e-6）")
    L.append("")
    L.append("| run (v5) | reference (v4) | file | merged rows | shared num cols | NaN-pattern mismatches | max abs diff |")
    L.append("|---|---|---|---|---|---|---|")
    worst = 0.0
    for m in ["gemma1b", "gpt2"]:
        v5 = f"runs/{m}_v5/s0_abs5e-3"; v4 = f"runs/{m}_v4/s0_abs5e-3"
        if not (os.path.exists(f"{v5}/summary.csv") and os.path.exists(f"{v4}/summary.csv")):
            L.append(f"| `{v5}` | `{v4}` | (missing) | - | - | - | - |")
            continue
        s5 = pd.read_csv(f"{v5}/summary.csv"); s4 = pd.read_csv(f"{v4}/summary.csv")
        r1 = num_diff(s5, s4, ["model", "method", "level"], "summary.csv")
        p5 = pd.read_csv(f"{v5}/per_context.csv"); p4 = pd.read_csv(f"{v4}/per_context.csv")
        r2 = num_diff(p5, p4, ["ctx_id", "method", "level"], "per_context.csv")
        for r in (r1, r2):
            worst = max(worst, r["mx"])
            L.append(f"| `{v5}` | `{v4}` | {r['file']} | {r['n_rows']} | {r['n_cols']} | {r['nan_mm']} | {r['mx']:.1e} |")
    verdict = "PASS" if worst <= 1e-6 else "FAIL"
    L.append("")
    L.append(f"Overall max abs diff over shared numeric columns: {worst:.1e} -> {verdict} (threshold 1e-6).")
    L.append("")
    L.append("### 2b. WP-0：合成数据 numpy vs torch 后端对等（任务书 §5 WP-0 容差）")
    L.append("")
    np_, th = "runs/syn_v5_numpy", "runs/syn_v5_torch"
    rows = []
    if os.path.exists(f"{np_}/summary.csv") and os.path.exists(f"{th}/summary.csv"):
        a = pd.read_csv(f"{np_}/summary.csv"); b = pd.read_csv(f"{th}/summary.csv")
        m = a.merge(b, on=["model", "method", "level"], suffixes=("_n", "_t"))
        def d(c): return float(np.abs(m[f"{c}_n"] - m[f"{c}_t"]).max())
        rel = lambda x: float(np.abs(m[f"{x}_n"] - m[f"{x}_t"]).max() / np.abs(m[f"{x}_n"]).max())
        rows.append(("summary reach_rate", d("reach_rate"), "identical", d("reach_rate") == 0.0))
        for c, tol in [("kl_mean", 1e-3), ("klpark_mean", 1e-3), ("kl99_mean", 1e-3), ("klneu_mean", 1e-3),
                       ("cfdev_mean", 1e-3), ("rd_mean", 1e-2)]:
            rows.append((f"summary {c}", d(c), f"<= {tol:g}", d(c) <= tol))
        fa = pd.read_csv(f"{np_}/ctx_features.csv").sort_values("ctx_id").reset_index(drop=True)
        fb = pd.read_csv(f"{th}/ctx_features.csv").sort_values("ctx_id").reset_index(drop=True)
        for c, tol in [("H0", 1e-4), ("cf0", 1e-4)]:
            v = float(np.abs(fa[c] - fb[c]).max()); rows.append((f"ctx_features {c}", v, f"<= {tol:g}", v <= tol))
        for c in ["sigma_pr", "sigma_trace"]:
            v = float((np.abs(fa[c] - fb[c]) / np.abs(fa[c])).max()); rows.append((f"ctx_features {c} (rel)", v, "<= 1e-3", v <= 1e-3))
        na = pd.read_csv(f"{np_}/null_control.csv"); nb = pd.read_csv(f"{th}/null_control.csv")
        same_rows = len(na) == len(nb)
        j = na.merge(nb, on=["ctx_id", "method", "draw"], suffixes=("_n", "_t"))
        for c in ["kl", "kl_park"]:
            v = float(np.abs(j[f"{c}_n"] - j[f"{c}_t"]).max()); rows.append((f"null_control {c} (rows {len(na)}={len(nb)})", v, "<= 1e-3", v <= 1e-3 and same_rows))
        ca = json.load(open(f"{np_}/checks.json"))["v5"]["freq_info"]["mean_eig_Sw"]
        cb = json.load(open(f"{th}/checks.json"))["v5"]["freq_info"]["mean_eig_Sw"]
        v = abs(ca - cb) / abs(ca); rows.append(("checks v5.freq_info.mean_eig_Sw (rel)", v, "<= 1e-3", v <= 1e-3))
        L.append("| item | measured | tolerance | pass |")
        L.append("|---|---|---|---|")
        for it, v, tol, ok in rows:
            L.append(f"| {it} | {v:.3g} | {tol} | {'PASS' if ok else 'FAIL'} |")
        L.append("")
        L.append(f"WP-0 verdict: {'PASS' if all(r[3] for r in rows) else 'FAIL'} ({len(rows)} criteria).")
    else:
        L.append("(synthetic parity runs not found)")
    L.append("")


# ---------------------------------------------------------------- section 3
def section3(panel, R, L):
    L.append("## 3. 指标面板（核心表：C1 = `euc_dmd` vs `dua_dmd`，C2 = `cau_unemb` vs `dua_unemb`）")
    L.append("")
    L.append(f"来源：`{AN}/metric_panel.csv`（analyze_v5.py，level={L0}，簇自助法 95% 区间）。"
             "diff = metric(a) − metric(b)，所有指标越低越好，diff > 0 表示 b（自适应 `dua`）更好；`(ns)` = 区间跨 0。"
             "**`kl_park` 不是真正的 KL**（Park 的 5e-3 偏移，可为负），只作为 Park 度量的复现；`kl` 为我们的 KL（1e-12 下限）。")
    L.append("")
    by = {}
    for g, gr in panel.groupby("group", sort=False):
        by[g] = gr
    order = ["A_third_a5e-3", "gpt2_A_third_a5e-3", "gemma4b_A_third_a5e-3",
             "C_third_a5e-3", "Cbig_third_a5e-3", "A_third_a2e-2", "C_third_a2e-2", "A_ing_a5e-3", "gpt2_A_ing_a5e-3"]
    heads = {
        "A_third_a5e-3": ("3.1 区域 A（复现，非确认）", "gemma-1b，concept third，α=5e-3，种子 0/1/2"),
        "gpt2_A_third_a5e-3": ("3.2 区域 A（描述性，第二模型）", "GPT-2，concept third，α=5e-3，种子 0/1/2"),
        "gemma4b_A_third_a5e-3": ("3.3 区域 A（描述性，第三模型）", "gemma-4b（4-bit），concept third，α=5e-3，种子 0"),
        "C_third_a5e-3": ("3.4 区域 C（**确认性 K1/K2**）", "gemma-1b，concept third，α=5e-3，种子 0/1/2，数据 `gemma1b_c4_s{S}`"),
        "Cbig_third_a5e-3": ("3.5 区域 C 扩大版（描述性）", "gemma-1b，concept third，α=5e-3，种子 0/1/2，数据 `gemma1b_c4big_s{S}`（P1 扩大提取，不替代 3.4）"),
        "A_third_a2e-2": ("3.6 区域 A，α 敏感性（描述性）", "gemma-1b，concept third，α=2e-2，种子 0/1/2"),
        "C_third_a2e-2": ("3.7 区域 C，α 敏感性（描述性）", "gemma-1b，concept third，α=2e-2，种子 0/1/2"),
        "A_ing_a5e-3": ("3.8 概念 -ing（描述性；探针混杂，仅 unemb 行可解读）", "gemma-1b，concept ing，α=5e-3，种子 0/1/2"),
        "gpt2_A_ing_a5e-3": ("3.9 概念 -ing，GPT-2（描述性；同上仅 unemb 可解读）", "GPT-2，concept ing，α=5e-3，种子 0"),
    }
    for g in order:
        if g not in by:
            continue
        h, sub = heads[g]
        L.append(f"### {h}")
        L.append("")
        L.append(f"{sub}。独立单元数：{sum(1 for _ in by[g]['run'].unique())}（每行一个 run = 一个单元内的一个种子）。")
        L.append("")
        L.append("| run | pair | kl | kl_park | rd | cf_dev | kl_neu | n |")
        L.append("|---|---|---|---|---|---|---|---|")
        for (pair, run), gr in by[g].groupby(["pair(a-b)", "run"], sort=False):
            cells = []
            for met in PANEL_METRICS:
                q = gr[gr.metric == met]
                cells.append(cell(q.iloc[0] if len(q) else None, "diff_mean"))
            L.append(f"| `{run}` | {pair} | " + " | ".join(cells) + f" | {int(gr.iloc[0]['n'])} |")
        L.append("")
    L.append("注：3.8/3.9 的 `dmd` 探针行受助动词句式混杂影响（任务书 §10），解读以 `unemb` 行为准；"
             "3.4 与 3.5 为两个独立数据集，均报告。`rd` 为简化版排名保持（起点 top-0.99 集合）；`cf` 无方向，不列。")
    L.append("")


# ---------------------------------------------------------------- section 4
def section4(cap, L):
    L.append("## 4. 捕获比例（Q-B）")
    L.append("")
    L.append(f"来源：`{AN}/capture_ratio.csv`（全表）。"
             "ρ = mean(euc − X)/mean(euc − dua)：1 = 与自适应相同，0 = 与欧氏相同。"
             "**仅当 `gap_defined=True`（欧氏→自适应差距的区间不含 0）时 ρ 才可解读**，否则本表以 `n/a (gap ns)` 占位（CSV 中仍有数值，但按任务书 §8.3 不解读）。")
    L.append("")
    L.append("| group | probe | metric | n | gap(euc−dua) [lo,hi] | gap_defined | rho_cau [lo,hi] | rho_frq [lo,hi] |")
    L.append("|---|---|---|---|---|---|---|---|")
    for _, r in cap.iterrows():
        gap = fmt((r["gap_euc_minus_dua"], r["gap_lo"], r["gap_hi"]), nd=4)
        gd = bool(r["gap_defined"])
        if gd:
            rc = fmt((r["rho_cau"], r["rho_cau_lo"], r["rho_cau_hi"]), nd=3)
            rf = fmt((r["rho_frq"], r["rho_frq_lo"], r["rho_frq_hi"]), nd=3) if np.isfinite(r["rho_frq"]) else "n/a (no frq)"
        else:
            rc = rf = "n/a (gap ns)"
        L.append(f"| {r['group']} | {r['probe']} | {r['metric']} | {int(r['n'])} | {gap} | {gd} | {rc} | {rf} |")
    L.append("")


# ---------------------------------------------------------------- section 5
def section5(reg, corr, L):
    L.append("## 5. 优势回归（Q-C）与预测变量相关")
    L.append("")
    L.append(f"来源：`{AN}/advantage_regression.csv`、`{AN}/predictor_corr.csv`。"
             "回归为逐上下文 OLS（按 run 去均值的固定效应 + 按簇自助法 95% 区间）；`coef_per_SD` = 预测变量标准化后的系数。"
             "本节展示 C1/C2 两个配对在 `kl` 与 `kl_park` 上的 joint 与单变量模型；其余 metric/配对见 CSV 全表（不删减，仅不在本文重复）。"
             "**相关分析，不作因果表述。**")
    L.append("")
    for pa, pb, name in CONFIRM:
        pair = f"{pa} - {pb}"
        q = reg[reg["pair(a-b)"] == pair]
        for model_name, title in [("joint", "joint（三预测变量同入）"), ("uni", "单变量")]:
            want = "joint" if model_name == "joint" else "uni_"
            qq = q[q["model"].str.startswith(want)]
            L.append(f"### {name}（{pair}）：{title}")
            L.append("")
            L.append("| group | model | term | kl coef [lo,hi] | kl R2 | kl_park coef [lo,hi] | kl_park R2 | n | n_clusters |")
            L.append("|---|---|---|---|---|---|---|---|---|")
            for g in list(dict.fromkeys(qq["group"])):
                gq = qq[qq.group == g]
                for term in ["H0", "cf0", "log_pr"]:
                    tq = gq[gq.term == term]
                    c_kl = tq[(tq.metric == "kl") & (tq.model == (f"uni_{term}" if model_name == "uni" else "joint"))]
                    c_pk = tq[(tq.metric == "kl_park") & (tq.model == (f"uni_{term}" if model_name == "uni" else "joint"))]
                    kl_c = fmt((c_kl.iloc[0].coef_per_SD, c_kl.iloc[0].lo, c_kl.iloc[0].hi)) if len(c_kl) else "n/a"
                    kl_r = f"{c_kl.iloc[0].R2:.3f}" if len(c_kl) else "n/a"
                    pk_c = fmt((c_pk.iloc[0].coef_per_SD, c_pk.iloc[0].lo, c_pk.iloc[0].hi)) if len(c_pk) else "n/a"
                    pk_r = f"{c_pk.iloc[0].R2:.3f}" if len(c_pk) else "n/a"
                    nn = int(c_kl.iloc[0].n) if len(c_kl) else (int(c_pk.iloc[0].n) if len(c_pk) else 0)
                    nc = int(c_kl.iloc[0].n_clusters) if len(c_kl) else (int(c_pk.iloc[0].n_clusters) if len(c_pk) else 0)
                    L.append(f"| {g} | {c_kl.iloc[0].model if len(c_kl) else ''} | {term} | {kl_c} | {kl_r} | {pk_c} | {pk_r} | {nn} | {nc} |")
            L.append("")
    L.append("### 预测变量相关（共线性检查；|corr| > 0.7 时以单变量模型为主）")
    L.append("")
    L.append("| group | pair | H0–cf0 | H0–log_pr | cf0–log_pr |")
    L.append("|---|---|---|---|---|")
    for (g, a, b), gr in corr.groupby(["group", "a", "b"], sort=False):
        if f"{a} - {b}" not in [f"{p} - {q}" for p, q, _ in CONFIRM]:
            continue
        d = {r["pred_i"] + "-" + r["pred_j"]: r["corr"] for _, r in gr.iterrows()}
        def c(k):
            if k not in d or not np.isfinite(d[k]):
                return "n/a"
            return f"{d[k]:.3f}" + ("*" if abs(d[k]) > 0.7 else "")
        L.append(f"| {g} | {a} - {b} | {c('H0-cf0')} | {c('H0-log_pr')} | {c('cf0-log_pr')} |")
    L.append("")
    L.append("（`*` = |corr| > 0.7。）")
    L.append("")


# ---------------------------------------------------------------- section 6
def section6(ncs, L):
    L.append("## 6. 随机探针对照（Q-D）")
    L.append("")
    L.append(f"来源：`{AN}/null_control_summary.csv`（全表）。"
             "null = 结构化零探针（标签打乱/随机词对）经**同一种度量**、走与真实路径**相同步数**的终点；每个 run 抽 `--null_ctx 30` 个零探针上下文、每上下文 `--null_draws 3` 次 draw 取均值后，仅保留与真实路径（level 0.9 `reached=1`）可配对的上下文，故 `n` 可小于 30。"
             "`real − null` 为簇自助法 95% 区间。`null/real` 比为本表由 real/null 列计算（real ≤ 0 或非有限时记 `n/a`）。任务书 §8.3 的判读（`dua_*` 的 `kl` null/real ≥ 0.5）属结论层，见 CONCLUSIONS_V5.md。")
    L.append("")
    L.append("| group | run | method | n | kl real | kl null | kl r−n [lo,hi] | kl null/real | kl_park real | kl_park null | kl_park r−n [lo,hi] | rd r−n | cf_dev r−n | kl_neu r−n | P1_null_end |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in ncs.iterrows():
        kr = fmt((r["kl_real_minus_null"], r["kl_lo"], r["kl_hi"]), nd=3)
        kratio = ratio(r["kl_null"], r["kl_real"])
        pr = fmt((r["kl_park_real_minus_null"], r["kl_park_lo"], r["kl_park_hi"]), nd=3)
        pratio = ratio(r["kl_park_null"], r["kl_park_real"])
        rd_ = fmt((r["rd_real_minus_null"], r["rd_lo"], r["rd_hi"]), nd=3)
        cd = fmt((r["cf_dev_real_minus_null"], r["cf_dev_lo"], r["cf_dev_hi"]), nd=3)
        kn = fmt((r["kl_neu_real_minus_null"], r["kl_neu_lo"], r["kl_neu_hi"]), nd=3)
        L.append(f"| {r['group']} | `{r['run']}` | {r['method']} | {int(r['n_ctx'])} | {r['kl_real']:.3f} | {r['kl_null']:.3f} | {kr} | {kratio} | "
                 f"{r['kl_park_real']:.3f} | {r['kl_park_null']:.3f} | {pr} | {rd_} | {cd} | {kn} | {r['P1_null_end']:.3f} |")
    L.append("")


# ---------------------------------------------------------------- section 7
def section7(R, L):
    L.append("## 7. 成本（含 `frq_*`）")
    L.append("")
    L.append("### 7a. 每个 run 的墙钟时间（`config.json` 的 `runtime_s`）")
    L.append("")
    L.append("| run | type | model | region | concept | runtime_s |")
    L.append("|---|---|---|---|---|---|")
    for r in sorted(R, key=lambda x: (x["type"], x["model"], x["region"], x["seed"])):
        rt = r["runtime"]
        L.append(f"| `{r['dir']}` | {r['type']} | {r['model']} | {r['region']} | {r['concept']} | {rt:.1f} |")
    L.append("")
    L.append("### 7b. 每方法平均每上下文耗时（`timing.csv`；真实模型 run，含 `frq_*`）")
    L.append("")
    L.append("| model | method | s/ctx | steps | ms/step | vs euc same probe |")
    L.append("|---|---|---|---|---|---|")
    agg = {}
    for r in R:
        if r["model"] == "synthetic":
            continue
        t = pd.read_csv(f"{r['dir']}/timing.csv").groupby("method").agg(sec=("seconds", "mean"), steps=("steps_run", "mean"))
        for m, row in t.iterrows():
            agg.setdefault((r["model"], m), []).append((row.sec, row.steps))
    for (model, m), v in sorted(agg.items()):
        if m not in METHODS:
            continue
        s_ = float(np.mean([x[0] for x in v])); st = float(np.mean([x[1] for x in v]))
        base = agg.get((model, "euc_" + m.split("_")[-1]))
        rr = ratio(s_, float(np.mean([x[0] for x in base]))) if base else "n/a"
        L.append(f"| {model} | {m} | {s_:.2f} | {st:.1f} | {1000 * s_ / max(st, 1):.0f} | {rr + 'x' if rr != 'n/a' else rr} |")
    L.append("")
    # reach-rate caveat computed from summary.csv
    worst = []
    for r in R:
        if r["type"].startswith(("WP-0", "WP-1")):
            continue
        s = pd.read_csv(f"{r['dir']}/summary.csv"); s9 = s[s.level == L0]
        for _, x in s9.iterrows():
            if x["reach_rate"] < 0.8:
                worst.append((r["dir"], x["method"], x["reach_rate"]))
    if worst:
        L.append("到达率提示（level 0.9 `reach_rate` < 0.8 的方法行，来自各 run `summary.csv`；与 selfcheck F6 的 WARN 对应）："
                 + "; ".join(f"`{d}` {m} reach={rr:.2f}" for d, m, rr in worst) + "。"
                 "这些行在 level 0.9 的端点指标为 NaN，不参与第 3–6 节的配对比较。")
    L.append("")


# ---------------------------------------------------------------- section 8
def section8(panel, cap, reg, corr, ncs, R, L):
    L.append("## 8. 证据—结论对应表（机器生成）")
    L.append("")
    L.append("每行：结论主题 | 证据文件与行（CSV 内 1-based 数据行，不含表头） | run 目录 | 独立单元数（=去重后的（模型,种子,概念,区域）组合） | 区域标签。"
             "确认性比较仅 K1/K2（区域 C、`kl_park`）；其余均为复现或描述性（任务书 §8.1/§9.2-C）。")
    L.append("")
    L.append("| claim | evidence (file: rows) | runs | units | region |")
    L.append("|---|---|---|---|---|")
    RMAP = {r["dir"]: r for r in R}
    # 1-based data-row index (excluding header) for each row of a frame
    def rowmap(df):
        return {i + 1: row for i, row in df.iterrows()}
    def units_of(runs):
        return len({(RMAP[d]["model"], RMAP[d]["seed"], RMAP[d]["concept"], RMAP[d]["region"]) for d in runs if d in RMAP})
    runs_by_group = {g: sorted(gr["run"].unique()) for g, gr in panel.groupby("group", sort=False)}
    # K1/K2 panel claims per group
    pmap = rowmap(panel)
    for g, runs in runs_by_group.items():
        n = units_of(runs)
        regions = sorted({RMAP[d]["region"] for d in runs if d in RMAP})
        concepts = sorted({RMAP[d]["concept"] for d in runs if d in RMAP})
        alphas = sorted({str(RMAP[d]["alpha"]) for d in runs if d in RMAP})
        if g == "C_third_a5e-3":
            tag = {"C1": "K1 确认性（kl_park）", "C2": "K2 确认性（kl_park）"}
        elif regions == ["A"] and concepts == ["third"] and alphas == ["0.005"]:
            tag = {"C1": "C1 区域 A 复现（非确认）", "C2": "C2 区域 A 复现（非确认）"}
        else:
            tag = {"C1": "C1 描述性", "C2": "C2 描述性"}
        for pa, pb, name in CONFIRM:
            pair = f"{pa} - {pb}"
            idxs = [i for i, r in pmap.items() if r["group"] == g and r["pair(a-b)"] == pair]
            if not idxs:
                continue
            kp = [i for i, r in pmap.items() if r["group"] == g and r["pair(a-b)"] == pair and r["metric"] == "kl_park"]
            L.append(f"| {name} @ {g}（{tag[name]}） | {AN}/metric_panel.csv: kl_park rows {kp}；全部指标 rows {min(idxs)}–{max(idxs)} | "
                     + ", ".join(f"`{d}`" for d in runs) + f" | {n} | {','.join(regions)} |")
    # capture ratio / regression / corr / null control per group (runs from the same group's panel rows)
    def group_rows(df):
        m = rowmap(df)
        return {g: [i for i, r in m.items() if r["group"] == g] for g in dict.fromkeys(df["group"])}
    for g, idxs in group_rows(cap).items():
        runs = runs_by_group.get(g, [])
        L.append(f"| Q-B 捕获比例 @ {g}（描述性；ρ 仅在 gap_defined=True 时可解读） | {AN}/capture_ratio.csv: rows {min(idxs)}–{max(idxs)} | "
                 + ", ".join(f"`{d}`" for d in runs) + f" | {units_of(runs)} | {','.join(sorted({RMAP[d]['region'] for d in runs if d in RMAP}))} |")
    for g, idxs in group_rows(reg).items():
        runs = runs_by_group.get(g, [])
        L.append(f"| Q-C 优势回归 @ {g}（描述性，非因果） | {AN}/advantage_regression.csv: rows {min(idxs)}–{max(idxs)} | "
                 + ", ".join(f"`{d}`" for d in runs) + f" | {units_of(runs)} | {','.join(sorted({RMAP[d]['region'] for d in runs if d in RMAP}))} |")
    for g, idxs in group_rows(corr).items():
        runs = runs_by_group.get(g, [])
        L.append(f"| Q-C 预测变量相关 @ {g} | {AN}/predictor_corr.csv: rows {min(idxs)}–{max(idxs)} | "
                 + ", ".join(f"`{d}`" for d in runs) + f" | {units_of(runs)} | {','.join(sorted({RMAP[d]['region'] for d in runs if d in RMAP}))} |")
    for g, idxs in group_rows(ncs).items():
        runs = sorted(ncs[ncs.group == g]["run"].unique())
        L.append(f"| Q-D 随机探针对照 @ {g}（描述性） | {AN}/null_control_summary.csv: rows {min(idxs)}–{max(idxs)} | "
                 + ", ".join(f"`{d}`" for d in runs) + f" | {units_of(runs)} | {','.join(sorted({RMAP[d]['region'] for d in runs if d in RMAP}))} |")
    # gates and cost
    L.append(f"| WP-1 回归 vs V4（G6 硬门槛） | 第 2a 节（summary.csv/per_context.csv 共有数值列逐列差） | `runs/gemma1b_v5/s0_abs5e-3`, `runs/gpt2_v5/s0_abs5e-3` | 2 | A |")
    L.append(f"| WP-0 双后端对等 | 第 2b 节（summary/ctx_features/null_control/checks） | `runs/syn_v5_numpy`, `runs/syn_v5_torch` | 1 | A(syn) |")
    n_all = len({(r["model"], r["seed"], r["concept"], r["region"]) for r in R})
    L.append(f"| 成本（含 frq_*） | 第 7 节（timing.csv；config.json 的 runtime_s） | 全部 run（第 1 节表） | {n_all} | A+C |")
    L.append(f"| 数据与检验 | 第 1 节（config.json/checks.json/ctx_features.csv） | 全部 run（第 1 节表） | {n_all} | A+C |")
    L.append("")


def main():
    R = [meta_of(d) for pat in ["runs/gemma1b_v5/*", "runs/gpt2_v5/*", "runs/gemma4b_v5/*", "runs/syn_v5_*"]
         for d in runs_in(pat)]
    panel = pd.read_csv(f"{AN}/metric_panel.csv"); cap = pd.read_csv(f"{AN}/capture_ratio.csv")
    reg = pd.read_csv(f"{AN}/advantage_regression.csv"); corr = pd.read_csv(f"{AN}/predictor_corr.csv")
    ncs = pd.read_csv(f"{AN}/null_control_summary.csv")

    L = []
    L.append("# V5 aggregate (auto-generated by aggregate_v5.py; conclusions are in CONCLUSIONS_V5.md)")
    L.append("")
    L.append(f"Runs included: {len(R)} (discovered under `runs/*_v5/*` with `summary.csv`). "
             f"Analysis source: `{AN}/` (analyze_v5.py, level {L0}, cluster bootstrap, uncorrected for multiple comparisons). "
             "Independent unit = (model, seed, concept, region); fixed methods are alpha-independent and counted once per unit; "
             "different alphas are within-unit sensitivity. Convention: diff = metric(a) − metric(b); every metric here is "
             "lower-is-better, so diff > 0 means b (the adaptive `dua` method) is better; `(ns)` marks intervals crossing 0. "
             "`kl_park` is NOT a true KL (Park's 5e-3 offset; can be negative); it is only a reproduction of Park's metric. "
             "`cf` has no direction and is never used for better/worse claims.")
    L.append("")
    section1(R, L)
    section2(R, L)
    section3(panel, R, L)
    section4(cap, L)
    section5(reg, corr, L)
    section6(ncs, L)
    section7(R, L)
    section8(panel, cap, reg, corr, ncs, R, L)
    Path("runs/AGGREGATE_V5.md").write_text("\n".join(L) + "\n")
    print(f"wrote runs/AGGREGATE_V5.md ({len(R)} runs, {len(panel)} panel rows)")


if __name__ == "__main__":
    main()
