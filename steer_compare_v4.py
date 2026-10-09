"""
Stage 2 - steering comparison (Euclidean vs fixed causal metric vs adaptive dual steering).

All methods share: probe beta (primal mean difference), step norm, stopping rule. Only the DIRECTION differs:
    euclid        v = beta
    causal_fixed  v = (S0 + a I)^-1 beta     S0 = uniform covariance of all unembedding rows (computed once)
    dual          v = (S_t + a I)^-1 beta    S_t = Cov[gamma | lambda_t] (softmax-weighted, top-K, conjugate gradient)
(Hessian of the log-partition function at lambda=0 equals S0, so causal_fixed = Newton step with metric frozen at uniform.)

v2 changes: --alpha_abs, methods euclid_unemb/causal_unemb (Park 2024 recipe), Sigma_t spectrum diagnostics,
cluster bootstrap by subject, final.csv (end-state of non-reaching paths), --methods selector,
paired.csv column win_b_lower_kl renamed frac_ctx_b_lower_kl.

Usage
  python steer_compare.py --selftest                       # verify code paths (run this first)
  python steer_compare.py --synthetic --out runs/syn       # no data needed
  python steer_compare.py --data_dir data/gpt2 --out runs/gpt2/a0.01_s0 --alpha_rel 0.01 --seed 0
  python steer_compare.py --data_dir data/gemma4b --backend torch --topk 20000 --out runs/gemma4b/a0.01_s0
Outputs (in --out): config.json checks.json summary.csv paired.csv per_context.csv curves.png report.md
"""
import argparse, json, csv, os, math, time, platform
from pathlib import Path
import numpy as np


# =============================================================================== helpers
import re as _re

def safe_run_dir(raw, base=None):
    """Rebuild a user-supplied run directory from whitelist tokens only ('..' and separators cannot appear)."""
    parts = [p for p in str(raw).replace("\\", "/").split("/") if _re.fullmatch(r"[A-Za-z0-9._-]+", p) and p not in (".", "..")]
    if not parts:
        raise SystemExit(f"unsafe output directory (only [A-Za-z0-9._-] path components allowed): {raw!r}")
    return os.path.join(*parts)


def out_file(root, name):
    """Validated output file path: whitelist-sanitized run dir + literal basename."""
    return os.path.join(safe_run_dir(root, "runs"), os.path.basename(name))


def softmax64(z):
    z = z.astype(np.float64); z = z - z.max(); e = np.exp(z); return e / e.sum()


def auc(pos, neg):
    s = np.concatenate([pos, neg]); r = s.argsort().argsort() + 1.0
    n1, n0 = len(pos), len(neg)
    return float((r[:n1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def boot_ci(x, rng, B=2000):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    if len(x) < 3: return (float("nan"),) * 3
    m = np.array([x[rng.integers(0, len(x), len(x))].mean() for _ in range(B)])
    return float(x.mean()), float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))


def cluster_boot_ci(x, groups, rng, B=2000):
    """Resample whole clusters (e.g. subjects) so that correlated template contexts are not treated as independent."""
    x = np.asarray(x, float); g = np.asarray(groups); ok = ~np.isnan(x); x, g = x[ok], g[ok]
    ug = np.unique(g)
    if len(x) < 3 or len(ug) < 3: return (float("nan"),) * 3
    idx = {u: np.where(g == u)[0] for u in ug}
    m = np.array([np.concatenate([x[idx[u]] for u in rng.choice(ug, len(ug), replace=True)]).mean() for _ in range(B)])
    return float(x.mean()), float(np.quantile(m, 0.025)), float(np.quantile(m, 0.975))


_SUBJ = ["Many people", "The workers", "Our customers", "These kids", "Most doctors", "The engineers", "Both of them", "The teacher",
         "This company", "My brother", "My sister", "Our customer", "That kid", "The doctor", "The engineer", "Her mother",
         "The farmer", "The voter", "The man", "Students", "People", "Parents", "Farmers", "Voters", "Everyone",
         "They", "You", "We", "He", "She", "It", "I"]          # add new subjects here if you extend the templates
_PREF = ("Every day, ", "At work, ", "Honestly, ", "Today, ", "In this case, ", "Lately, ", "At home, ", "Over time, ", "Usually, ")


def subject_of(text):
    if text.startswith("syn_"): return "g" + str(int(text.split("_")[-1]) % 8)
    t = text
    for p in _PREF:
        if t.startswith(p): t = t[len(p):]
    for sname in _SUBJ:
        if t == sname or t.startswith(sname + " "): return sname
    return "?"


# =============================================================================== backends
class BaseOps:
    def solve_fixed(self, S0, beta, alpha):
        v = np.linalg.solve(S0 + alpha * np.eye(len(S0)), np.asarray(beta, np.float64))
        return self.vec(v / np.linalg.norm(v))


class NumpyOps(BaseOps):
    name = "numpy"
    def __init__(self, G, y0, y1):
        self.G = np.ascontiguousarray(G, dtype=np.float32); self.V, self.d = self.G.shape
        self.y0, self.y1 = np.asarray(y0), np.asarray(y1)
        self.neutral = np.setdiff1d(np.arange(self.V), np.concatenate([self.y0, self.y1]))
    def vec(self, x): return np.asarray(x, dtype=np.float32)
    def tonp(self, x): return np.asarray(x)
    def copy(self, x): return x.copy()
    def norm(self, x): return float(np.linalg.norm(x))
    def probs(self, lam): return softmax64(self.G @ lam)
    def stats(self, p):
        m0, m1 = p[self.y0].sum(), p[self.y1].sum(); return float(m1 / (m0 + m1 + 1e-30)), float(m0 + m1)
    def zvec(self, p): return np.concatenate([p[self.y0] + p[self.y1], p[self.neutral]]) + 1e-12
    def kl(self, z0, zt): return float((z0 * (np.log(z0) - np.log(zt))).sum())
    def uniform_cov(self, chunk=16384):
        mu = self.G.mean(0, dtype=np.float64); S = np.zeros((self.d, self.d))
        for i in range(0, self.V, chunk):
            X = (self.G[i:i + chunk] - mu.astype(np.float32)); S += (X.T @ X).astype(np.float64)
        return S / (self.V - 1)
    def dual_dir(self, lam, beta, alpha, topk, iters=20, tol=1e-5):
        logits = self.G @ lam
        idx = np.argpartition(-logits, topk)[:topk] if topk < len(logits) else np.arange(len(logits))
        GK = self.G[idx]; pK = softmax64(logits[idx]).astype(np.float32); mu = pK @ GK
        A = lambda x: GK.T @ (pK * (GK @ x)) - mu * (mu @ x) + alpha * x
        b = beta.astype(np.float32); x = np.zeros_like(b); r = b.copy(); p = r.copy()
        rs = float(r @ r); bn = math.sqrt(rs)
        for _ in range(iters):
            Ap = A(p); a = rs / (float(p @ Ap) + 1e-30); x += a * p; r -= a * Ap; rs2 = float(r @ r)
            if math.sqrt(rs2) < tol * bn: break
            p = r + (rs2 / rs) * p; rs = rs2
        return x / (np.linalg.norm(x) + 1e-30)


class TorchOps(BaseOps):
    name = "torch"
    def __init__(self, G, y0, y1, device="cuda"):
        import torch; self.t = torch; self.dev = torch.device(device if torch.cuda.is_available() else "cpu")
        self.G = torch.from_numpy(np.ascontiguousarray(G)).to(self.dev).float(); self.V, self.d = self.G.shape
        self.y0 = torch.as_tensor(np.asarray(y0), dtype=torch.long, device=self.dev)
        self.y1 = torch.as_tensor(np.asarray(y1), dtype=torch.long, device=self.dev)
        mask = torch.ones(self.V, dtype=torch.bool, device=self.dev); mask[self.y0] = False; mask[self.y1] = False
        self.neutral = torch.nonzero(mask).squeeze(1)
    def vec(self, x): return self.t.as_tensor(np.asarray(x), dtype=self.t.float32, device=self.dev)
    def tonp(self, x): return x.detach().cpu().numpy()
    def copy(self, x): return x.clone()
    def norm(self, x): return float(self.t.linalg.norm(x).item())
    def probs(self, lam): return self.t.softmax(self.G @ lam, dim=0)
    def stats(self, p):
        m0, m1 = p[self.y0].sum(), p[self.y1].sum(); return float((m1 / (m0 + m1 + 1e-30)).item()), float((m0 + m1).item())
    def zvec(self, p): return self.t.cat([p[self.y0] + p[self.y1], p[self.neutral]]).double() + 1e-12
    def kl(self, z0, zt): return float((z0 * (self.t.log(z0) - self.t.log(zt))).sum().item())
    def uniform_cov(self, chunk=16384):
        t = self.t; mu = t.zeros(self.d, dtype=t.float64, device=self.dev)
        for i in range(0, self.V, chunk): mu += self.G[i:i + chunk].double().sum(0)
        mu = (mu / self.V); muf = mu.float(); S = t.zeros(self.d, self.d, dtype=t.float64, device=self.dev)
        for i in range(0, self.V, chunk):
            X = self.G[i:i + chunk] - muf; S += (X.T @ X).double()
        return (S / (self.V - 1)).cpu().numpy()
    def dual_dir(self, lam, beta, alpha, topk, iters=20, tol=1e-5):
        t = self.t; logits = self.G @ lam; k = min(topk, len(logits)); vals, idx = t.topk(logits, k)
        GK = self.G[idx]; pK = t.softmax(vals, dim=0); mu = pK @ GK
        A = lambda x: GK.T @ (pK * (GK @ x)) - mu * (mu @ x) + alpha * x
        b = beta.float(); x = t.zeros_like(b); r = b.clone(); p = r.clone(); rs = r @ r; bn = t.sqrt(rs)
        for _ in range(iters):
            Ap = A(p); a = rs / (p @ Ap + 1e-30); x = x + a * p; r = r - a * Ap; rs2 = r @ r
            if bool(t.sqrt(rs2) < tol * bn): break
            p = r + (rs2 / rs) * p; rs = rs2
        return x / (t.linalg.norm(x) + 1e-30)


def _np_pair_diff_mean(self): return (self.G[self.y1] - self.G[self.y0]).astype(np.float64).mean(0)
def _np_entropy(self, p): return float(-(p * np.log(p + 1e-30)).sum())
def _np_sigma_spec(self, lam, topk):
    logits = self.G @ lam
    idx = np.argpartition(-logits, topk)[:topk] if topk < len(logits) else np.arange(len(logits))
    GK = self.G[idx].astype(np.float64); p = softmax64(logits[idx]); mu = p @ GK
    S = (GK * p[:, None]).T @ GK - np.outer(mu, mu)
    return np.linalg.eigvalsh(S)[::-1]
def _np_phi(self, lam): return (softmax64(self.G @ lam).astype(np.float32) @ self.G).astype(np.float64)
def _np_top_idx(self, z0, mass=0.99):
    order = np.argsort(-z0); c = np.cumsum(z0[order]); k = int(np.searchsorted(c, mass * c[-1])) + 1; return order[:k]
def _np_kl_sub(self, z0, zt, S): a, b = z0[S], zt[S]; return float((a * (np.log(a) - np.log(b))).sum())
def _np_rankdiff(self, z0, zt, S):
    a, b = z0[S], zt[S]; r0 = np.arange(1, len(S) + 1); rt = (-b).argsort().argsort() + 1
    return float((a * np.abs(1.0 / rt - 1.0 / r0)).sum())
def _np_kl_parts(self, z0, zt):
    n = len(self.y0); a0, at, b0, bt = z0[:n].sum(), zt[:n].sum(), z0[n:].sum(), zt[n:].sum()
    SA = (z0[:n] * (np.log(z0[:n]) - np.log(zt[:n]))).sum(); SB = (z0[n:] * (np.log(z0[n:]) - np.log(zt[n:]))).sum()
    kb = a0 * np.log(a0 / at) + b0 * np.log(b0 / bt)
    return float(kb), float(SA - a0 * np.log(a0 / at)), float(SB - b0 * np.log(b0 / bt))
def _np_kl_full(self, p0, p): return float((p0 * (np.log(p0 + 1e-300) - np.log(p + 1e-300))).sum())
def _np_topk_in(self, p, ids, k):
    idx = np.argpartition(-p, k)[:k]; return bool(np.isin(idx, ids).all()), float(p[idx].sum())
def _np_hyperplane_min(self, lam0, beta, c, topk, iters=40, tol=1e-6):
    """argmin_{lam: beta.lam = c} KL(P_lam0 || P_lam)  (Park 2026, Thm 3.1). Newton with top-K Hessian, exact f and gradient."""
    G = self.G; beta = np.asarray(beta, np.float64); lam0 = np.asarray(lam0, np.float64); phi0 = self.phi(lam0.astype(np.float32))
    def fg(lam):
        lg = (G @ lam.astype(np.float32)).astype(np.float64); m = lg.max(); lse = m + np.log(np.exp(lg - m).sum())
        p = np.exp(lg - lse); phi = (p.astype(np.float32) @ G).astype(np.float64); return lse - phi0 @ lam, phi - phi0, lg, p
    lam = lam0 + (c - beta @ lam0) / (beta @ beta) * beta
    for it in range(iters):
        f, g, lg, p = fg(lam)
        idx = np.argpartition(-lg, topk)[:topk] if topk < len(lg) else np.arange(len(lg))
        GK = G[idx].astype(np.float64); pK = p[idx] / p[idx].sum(); mu = pK @ GK
        H = (GK * pK[:, None]).T @ GK - np.outer(mu, mu); H += (1e-8 * np.trace(H) / len(H) + 1e-12) * np.eye(len(H))
        Hg = np.linalg.solve(H, g); Hb = np.linalg.solve(H, beta); nu = -(beta @ Hg) / (beta @ Hb)
        r = g + nu * beta
        if np.linalg.norm(r) < tol * (1 + np.linalg.norm(g)): break
        D = -(Hg + nu * Hb); t = 1.0; slope = g @ D
        for _ in range(30):
            if fg(lam + t * D)[0] <= f + 1e-4 * t * slope: break
            t *= 0.5
        else: break
        lam = lam + t * D
    return lam.astype(np.float32)
NumpyOps.kl_parts = _np_kl_parts; NumpyOps.kl_full = _np_kl_full; NumpyOps.topk_in = _np_topk_in; NumpyOps.hyperplane_min = _np_hyperplane_min
NumpyOps.phi = _np_phi; NumpyOps.top_idx = _np_top_idx; NumpyOps.kl_sub = _np_kl_sub; NumpyOps.rankdiff = _np_rankdiff
NumpyOps.pair_diff_mean = _np_pair_diff_mean; NumpyOps.entropy = _np_entropy; NumpyOps.sigma_spec = _np_sigma_spec


def _t_pair_diff_mean(self): return (self.G[self.y1] - self.G[self.y0]).double().mean(0).cpu().numpy()
def _t_entropy(self, p): return float(-(p * self.t.log(p + 1e-30)).sum().item())
def _t_sigma_spec(self, lam, topk):
    t = self.t; logits = self.G @ lam; k = min(topk, len(logits)); vals, idx = t.topk(logits, k)
    GK = self.G[idx].double(); p = t.softmax(vals.double(), dim=0); mu = p @ GK
    S = (GK * p[:, None]).T @ GK - t.outer(mu, mu)
    return t.linalg.eigvalsh(S).flip(0).cpu().numpy()
def _t_phi(self, lam): return (self.t.softmax(self.G @ lam, dim=0) @ self.G).double().cpu().numpy()
def _t_top_idx(self, z0, mass=0.99):
    t = self.t; order = t.argsort(z0, descending=True); c = t.cumsum(z0[order], 0)
    k = int(t.searchsorted(c, mass * c[-1]).item()) + 1; return order[:k]
def _t_kl_sub(self, z0, zt, S): a, b = z0[S], zt[S]; return float((a * (self.t.log(a) - self.t.log(b))).sum().item())
def _t_rankdiff(self, z0, zt, S):
    t = self.t; a, b = z0[S], zt[S]; r0 = t.arange(1, len(S) + 1, device=a.device, dtype=a.dtype)
    rt = t.argsort(t.argsort(-b)).to(a.dtype) + 1
    return float((a * (1.0 / rt - 1.0 / r0).abs()).sum().item())
def _t_kl_parts(self, z0, zt):
    t = self.t; n = len(self.y0); a0, at, b0, bt = z0[:n].sum(), zt[:n].sum(), z0[n:].sum(), zt[n:].sum()
    SA = (z0[:n] * (t.log(z0[:n]) - t.log(zt[:n]))).sum(); SB = (z0[n:] * (t.log(z0[n:]) - t.log(zt[n:]))).sum()
    kb = a0 * t.log(a0 / at) + b0 * t.log(b0 / bt)
    return float(kb.item()), float((SA - a0 * t.log(a0 / at)).item()), float((SB - b0 * t.log(b0 / bt)).item())
def _t_kl_full(self, p0, p): t = self.t; return float((p0.double() * (t.log(p0.double() + 1e-300) - t.log(p.double() + 1e-300))).sum().item())
def _t_topk_in(self, p, ids, k):
    t = self.t; v, i = t.topk(p, k); idsT = t.as_tensor(np.asarray(ids), dtype=t.long, device=p.device)
    return bool(t.isin(i, idsT).all().item()), float(v.sum().item())
def _t_hyperplane_min(self, lam0, beta, c, topk, iters=40, tol=1e-6):
    t = self.t; G = self.G; dev = self.dev
    beta = t.as_tensor(np.asarray(beta), dtype=t.float64, device=dev); lam = lam0.double().clone(); phi0 = (t.softmax(G @ lam0.float(), dim=0) @ G).double()
    def fg(l):
        lg = (G @ l.float()).double(); lse = t.logsumexp(lg, 0); p = t.exp(lg - lse)
        phi = (p.float() @ G).double(); return float((lse - phi0 @ l).item()), phi - phi0, lg, p
    lam = lam + (float(c) - beta @ lam) / (beta @ beta) * beta
    for it in range(iters):
        f, g, lg, p = fg(lam)
        k = min(topk, len(lg)); idx = t.topk(lg, k).indices
        GK = G[idx]; pK = p[idx] / p[idx].sum(); muK = (pK.float() @ GK)
        H = ((GK * pK.float()[:, None]).T @ GK - t.outer(muK, muK)).double(); H += (1e-8 * t.trace(H) / len(H) + 1e-12) * t.eye(len(H), dtype=t.float64, device=dev)
        Hg = t.linalg.solve(H, g); Hb = t.linalg.solve(H, beta); nu = -(beta @ Hg) / (beta @ Hb); r = g + nu * beta
        if float(t.linalg.norm(r)) < tol * (1 + float(t.linalg.norm(g))): break
        D = -(Hg + nu * Hb); step = 1.0; slope = float((g @ D).item())
        for _ in range(30):
            if fg(lam + step * D)[0] <= f + 1e-4 * step * slope: break
            step *= 0.5
        else: break
        lam = lam + step * D
    return lam.float()
TorchOps.kl_parts = _t_kl_parts; TorchOps.kl_full = _t_kl_full; TorchOps.topk_in = _t_topk_in; TorchOps.hyperplane_min = _t_hyperplane_min
TorchOps.phi = _t_phi; TorchOps.top_idx = _t_top_idx; TorchOps.kl_sub = _t_kl_sub; TorchOps.rankdiff = _t_rankdiff
TorchOps.pair_diff_mean = _t_pair_diff_mean; TorchOps.entropy = _t_entropy; TorchOps.sigma_spec = _t_sigma_spec


def make_ops(kind, G, y0, y1, device):
    if kind == "numpy": return NumpyOps(G, y0, y1)
    if kind == "torch": return TorchOps(G, y0, y1, device)
    try:
        import torch
        if torch.cuda.is_available(): return TorchOps(G, y0, y1, device)
    except Exception: pass
    return NumpyOps(G, y0, y1)


# =============================================================================== steering path
def run_path(ops, lam0, dir_fn, eta, max_steps, levels, keep_level=None):
    p0 = ops.probs(lam0); z0 = ops.zvec(p0); lam = ops.copy(lam0); reached = {L: None for L in levels}; H0 = ops.entropy(p0); S = ops.top_idx(z0, 0.99); cf0 = ops.stats(p0)[1]
    for t in range(max_steps + 1):
        p = ops.probs(lam); P1, cf = ops.stats(p); zt = ops.zvec(p); kl = ops.kl(z0, zt)
        for L in levels:
            if reached[L] is None and P1 >= L:
                kb_, kp_, kn_ = ops.kl_parts(z0, zt)
                reached[L] = dict(step=t, P1=P1, cf=cf, kl=kl, kl99=ops.kl_sub(z0, zt, S), rd=ops.rankdiff(z0, zt, S),
                                  cf0=cf0, cf_dev=abs(cf - cf0), kl_bin=kb_, kl_pair=kp_, kl_neu=kn_)
                if keep_level is not None and abs(L - keep_level) < 1e-9: reached["_lam"] = ops.copy(lam)
        if P1 >= levels[-1]: break
        lam = lam + eta * dir_fn(lam)
    reached["_final"] = dict(step=t, P1=P1, cf=cf, kl=kl, H_start=H0, H_end=ops.entropy(p), cf0=cf0)
    return reached


# =============================================================================== synthetic data
def make_synthetic(rng, V=3000, d=64, n_pairs=120, n_ctx=160):
    spec = np.exp(-np.arange(d) / 12) + 0.05
    Q = np.linalg.qr(rng.standard_normal((d, d)))[0]; A = Q * np.sqrt(spec)
    G = rng.standard_normal((V, d)) @ A.T
    b = rng.standard_normal(d) @ A.T; b = b / np.linalg.norm(b) * 3.0
    y0 = np.arange(n_pairs); y1 = np.arange(n_pairs, 2 * n_pairs)
    G[y1] = G[y0] + b + 0.3 * rng.standard_normal((n_pairs, d)) @ A.T
    G = G.astype(np.float32)
    def ctx(side, n):
        out = []
        for _ in range(n):
            sub = rng.choice(n_pairs, 4, replace=False); tgt = (y1 if side else y0)[sub]
            m = G[tgt].mean(0); s = 9.0 / (G @ m).max()
            out.append(s * m + 0.02 * rng.standard_normal(d).astype(np.float32))
        return np.stack(out)
    return dict(G=G, pairs=np.stack([y0, y1], 1), Eb=ctx(0, n_ctx), Et=ctx(1, n_ctx),
                tb=[f"syn_base_{i}" for i in range(n_ctx)], tt=[f"syn_target_{i}" for i in range(n_ctx)],
                meta=dict(model="synthetic", logits_rel_err=0.0))


def load_data(d):
    ctx = json.load(open(f"{d}/contexts.json")); meta = json.load(open(f"{d}/meta.json"))
    return dict(G=np.load(f"{d}/G.npy"), pairs=np.load(f"{d}/pairs.npy"), Eb=np.load(f"{d}/E_base.npy"),
                Et=np.load(f"{d}/E_target.npy"), tb=ctx["base"], tt=ctx["target"], meta=meta, cb=ctx.get("base_cluster"))


# =============================================================================== selftest
def selftest():
    rng = np.random.default_rng(0); D = make_synthetic(rng, V=1500, d=32, n_pairs=60, n_ctx=20)
    G, pairs = D["G"], D["pairs"]; V, d = G.shape; ok = True
    S_ref = np.cov(G.astype(np.float64).T); alpha = 1e-2 * np.trace(S_ref) / d
    _o = NumpyOps(G, pairs[:, 0], pairs[:, 1]); lam = None
    for _l in D["Eb"]:
        _P1, _cf = _o.stats(_o.probs(_l))
        if _P1 < 0.3 and _cf > 0.15: lam = _l; break
    assert lam is not None, "selftest: no suitable base context"
    beta = (D["Et"][:5].mean(0) - D["Eb"][:5].mean(0)).astype(np.float64)
    p = softmax64(G @ lam); mu = p @ G; Gc = G - mu; Sig = (Gc.T * p) @ Gc
    v_ref = np.linalg.solve(Sig + alpha * np.eye(d), beta); v_ref /= np.linalg.norm(v_ref)
    ops_list = [NumpyOps(G, pairs[:, 0], pairs[:, 1])]
    try:
        import torch; ops_list.append(TorchOps(G, pairs[:, 0], pairs[:, 1], "cuda"))
    except Exception as e:
        print("[selftest] torch backend skipped:", repr(e)[:80])
    ref_paths = None
    for ops in ops_list:
        S = ops.uniform_cov(); rel = np.linalg.norm(S - S_ref) / np.linalg.norm(S_ref)
        v = ops.tonp(ops.dual_dir(ops.vec(lam), ops.vec(beta), alpha, topk=V)).astype(np.float64)
        cos = float(v @ v_ref / np.linalg.norm(v))
        eta = 0.01 * ops.norm(ops.vec(lam))
        r = run_path(ops, ops.vec(lam), lambda l: ops.vec(beta / np.linalg.norm(beta)), eta, 200, [0.3, 0.5])
        good = rel < 1e-3 and cos > 0.99
        print(f"[selftest:{ops.name}] cov rel.err={rel:.2e}  cg-vs-exact cos={cos:.4f}  "
              f"path L=0.5 -> {r[0.5] and (r[0.5]['step'], round(r[0.5]['kl'], 4))}  {'PASS' if good else 'FAIL'}")
        sig = (r[0.5]["step"], round(r[0.5]["kl"], 3)) if r[0.5] else None
        if ref_paths is None: ref_paths = sig
        elif sig != ref_paths: print("  WARNING: path differs between backends:", ref_paths, sig); ok = False
        ok &= good
    print("SELFTEST", "PASS" if ok else "FAIL")


# =============================================================================== main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data_dir"); ap.add_argument("--out", default="runs/out")
    ap.add_argument("--synthetic", action="store_true"); ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--backend", default="auto", choices=["auto", "numpy", "torch"]); ap.add_argument("--device", default="cuda")
    ap.add_argument("--n_ctx", type=int, default=80); ap.add_argument("--min_mass", type=float, default=0.15)
    ap.add_argument("--alpha_rel", type=float, default=1e-2, help="alpha = alpha_rel * tr(S0)/d (ignored if --alpha_abs)")
    ap.add_argument("--alpha_abs", type=float, default=None, help="absolute alpha (Park 2026 used 5e-3); overrides --alpha_rel")
    ap.add_argument("--ridge_rel", type=float, default=1e-6, help="ridge for causal_unemb: ridge_rel * tr(S0)/d")
    ap.add_argument("--methods", default="grid", help="'grid' = 9 methods {euc,cau,dua}_{ctx,unemb,dmd}; or comma list incl. legacy names")
    ap.add_argument("--no_cluster_boot", action="store_true")
    ap.add_argument("--filter", default="mass", choices=["mass", "park"], help="mass: cf mass >= --min_mass; park: top-k tokens all in group and cumulative >= --park_mass")
    ap.add_argument("--park_mass", type=float, default=0.7); ap.add_argument("--park_k", type=int, default=3)
    ap.add_argument("--optgap", type=int, default=0, help="number of test contexts for the exact-hyperplane optimality-gap analysis (0 = off)")
    ap.add_argument("--primary_level", type=float, default=0.9, help="level used to mark primary comparisons in paired_long.csv")
    ap.add_argument("--topk", type=int, default=5000); ap.add_argument("--step_frac", type=float, default=0.01)
    ap.add_argument("--max_steps", type=int, default=600); ap.add_argument("--levels", default="0.3,0.5,0.7,0.9,0.99")
    ap.add_argument("--seed", type=int, default=0); ap.add_argument("--boot", type=int, default=2000)
    a = ap.parse_args()
    if a.selftest: selftest(); return
    t_start = time.time(); rng = np.random.default_rng(a.seed)
    outdir = safe_run_dir(a.out, "runs"); os.makedirs(outdir, exist_ok=True)
    levels = [float(x) for x in a.levels.split(",")]
    D = make_synthetic(rng) if a.synthetic else load_data(a.data_dir)
    G, pairs, Eb, Et = D["G"], D["pairs"], D["Eb"], D["Et"]; y0, y1 = pairs[:, 0], pairs[:, 1]
    ops = make_ops(a.backend, G, y0, y1, a.device); V, d = ops.V, ops.d
    topk = min(a.topk, V)
    print(f"backend={ops.name} V={V} d={d} pairs={len(pairs)} contexts base={len(Eb)} target={len(Et)}")

    def stats_all(E):
        P1, cf = [], []
        for lam in E:
            s = ops.stats(ops.probs(ops.vec(lam))); P1.append(s[0]); cf.append(s[1])
        return np.array(P1), np.array(cf)
    P1b, cfb = stats_all(Eb); P1t, cft = stats_all(Et)
    if a.filter == "park":
        def _ok(E, ids):
            out = []
            for lam in E:
                allin, cum = ops.topk_in(ops.probs(ops.vec(lam)), ids, a.park_k); out.append(allin and cum >= a.park_mass)
            return np.array(out)
        kb = np.where(_ok(Eb, y0))[0]; kt = np.where(_ok(Et, y1))[0]
        print(f"kept after PARK filter (top-{a.park_k} in group, cum>={a.park_mass}): base={len(kb)}/{len(Eb)} target={len(kt)}/{len(Et)}")
    else:
        kb = np.where((cfb >= a.min_mass) & (P1b < 0.3))[0]; kt = np.where((cft >= a.min_mass) & (P1t > 0.7))[0]
        print(f"kept after filter (cf mass>={a.min_mass}): base={len(kb)}/{len(Eb)} target={len(kt)}/{len(Et)}")
    if len(kb) < 20 or len(kt) < 20:
        print("Too few contexts: lower --min_mass or change templates."); return
    kb = rng.permutation(kb); kt = rng.permutation(kt); hb, ht = len(kb) // 2, len(kt) // 2
    beta = Et[kt[:ht]].mean(0).astype(np.float64) - Eb[kb[:hb]].mean(0).astype(np.float64)
    probe_auc = auc(Et[kt[ht:]] @ beta, Eb[kb[hb:]] @ beta)
    print(f"[probe] held-out AUC = {probe_auc:.3f}")
    test_idx = kb[hb:][: a.n_ctx]

    S0 = ops.uniform_cov(); mean_eig_S0 = float(np.trace(S0)) / d
    alpha = a.alpha_abs if a.alpha_abs is not None else a.alpha_rel * mean_eig_S0
    v_euc = ops.vec(beta / np.linalg.norm(beta)); v_cau = ops.solve_fixed(S0, beta, alpha); beta_v = ops.vec(beta)
    cos_ec = float(ops.tonp(v_euc) @ ops.tonp(v_cau))
    print(f"alpha={alpha:.3e}  cos(euclid, causal_fixed)={cos_ec:.3f}")
    rr0 = np.random.default_rng(1)
    gbar = ops.pair_diff_mean()                                   # unembedding-space concept direction (Park 2024)
    v_eu = ops.vec(gbar / np.linalg.norm(gbar)); v_cu = ops.solve_fixed(S0, gbar, a.ridge_rel * mean_eig_S0)
    print(f"[diag] cos(beta, gbar)={float(beta @ gbar / (np.linalg.norm(beta) * np.linalg.norm(gbar))):.3f}  "
          f"cos(euclid_unemb, causal_unemb)={float(ops.tonp(v_eu) @ ops.tonp(v_cu)):.3f}  alpha/mean_eig(S0)={alpha / mean_eig_S0:.3g}")
    all_methods = {"euclid": lambda lam: v_euc, "causal_fixed": lambda lam: v_cau,
                   "dual": lambda lam: ops.dual_dir(lam, beta_v, alpha, topk),
                   "euclid_unemb": lambda lam: v_eu, "causal_unemb": lambda lam: v_cu}
    # ---- 3x3 grid: probe in {ctx (context mean diff), unemb (unembedding pair diff), dmd (dual mean diff)} x metric in {euc, cau, dua}
    phi_b = np.mean([ops.phi(ops.vec(Eb[i])) for i in kb[:hb]], 0)
    phi_t = np.mean([ops.phi(ops.vec(Et[i])) for i in kt[:ht]], 0)
    beta_phi = phi_t - phi_b
    probes = {"ctx": beta, "unemb": gbar, "dmd": beta_phi}
    def _cos(u, v): return float(u @ v / (np.linalg.norm(u) * np.linalg.norm(v)))
    probe_cos = {"ctx-unemb": _cos(beta, gbar), "ctx-dmd": _cos(beta, beta_phi), "unemb-dmd": _cos(gbar, beta_phi)}
    print("[diag] probe cosines:", {k: round(v, 3) for k, v in probe_cos.items()})
    for pn, pv in probes.items():
        pvv = ops.vec(pv); vE = ops.vec(pv / np.linalg.norm(pv)); vC = ops.solve_fixed(S0, pv, a.ridge_rel * mean_eig_S0)
        all_methods[f"euc_{pn}"] = (lambda lam, v=vE: v)
        all_methods[f"cau_{pn}"] = (lambda lam, v=vC: v)
        all_methods[f"dua_{pn}"] = (lambda lam, pv_=pvv: ops.dual_dir(lam, pv_, alpha, topk))
    names = [f"{m}_{p}" for p in ("ctx", "unemb", "dmd") for m in ("euc", "cau", "dua")] if a.methods == "grid" else a.methods.split(",")
    methods = {k: all_methods[k] for k in names}
    # Sigma_t spectrum at the starting points: choose alpha relative to THIS scale, not S0's
    sp = [ops.sigma_spec(ops.vec(Eb[i]), topk) for i in test_idx[: min(5, len(test_idx))]]
    sig_diag = dict(trace_mean=float(np.mean([x.sum() for x in sp])), eig_max_mean=float(np.mean([x[0] for x in sp])),
                    eig_p1_mean=float(np.mean([x[max(1, len(x) // 100)] for x in sp])),
                    eig_p10_mean=float(np.mean([x[max(1, len(x) // 10)] for x in sp])),
                    eig_p50_mean=float(np.mean([x[len(x) // 2] for x in sp])),
                    frac_eig_above_alpha=float(np.mean([(x > alpha).mean() for x in sp])))
    print("[diag] Sigma_t at start:", {k: f"{v:.3g}" for k, v in sig_diag.items()}, f"alpha={alpha:.3g}")
    grp = np.array([str(D["cb"][i]) if D.get("cb") else subject_of(D["tb"][i]) for i in test_idx])
    use_cluster = (not a.no_cluster_boot) and len(np.unique(grp)) >= 3
    print(f"[ci] {'cluster bootstrap over ' + str(len(np.unique(grp))) + ' subjects' if use_cluster else 'plain bootstrap over contexts'}")
    bci = (lambda x: cluster_boot_ci(x, grp, rr0, a.boot)) if use_cluster else (lambda x: boot_ci(x, rr0, a.boot))
    res = {m: [] for m in methods}; tim = {m: [] for m in methods}
    for n, i in enumerate(test_idx):
        lam0 = ops.vec(Eb[i]); eta = a.step_frac * ops.norm(lam0)
        for m, fn in methods.items():
            if ops.name == "torch" and ops.t.cuda.is_available(): ops.t.cuda.synchronize()
            t0 = time.perf_counter()
            res[m].append(run_path(ops, lam0, fn, eta, a.max_steps, levels, keep_level=a.primary_level if a.optgap > 0 else None))
            if ops.name == "torch" and ops.t.cuda.is_available(): ops.t.cuda.synchronize()
            tim[m].append((time.perf_counter() - t0, res[m][-1]["_final"]["step"]))
        if (n + 1) % 10 == 0: print(f"  steered {n + 1}/{len(test_idx)}  ({time.time() - t_start:.0f}s)", flush=True)

    def col(m, L, key): return np.array([r[L][key] if r[L] else np.nan for r in res[m]], float)
    rr = np.random.default_rng(1); model = D["meta"].get("model", "?")
    # REGRESSION FIX (recorded in DEVIATIONS.md): the four NEW v4 summary columns draw from a
    # dedicated rng so that rr0 advances exactly as in v3 (4 draws per cell), keeping the shared
    # columns' bootstrap intervals bit-identical to v3 (WP-A1 gate: <= 1e-6).
    rr_new = np.random.default_rng(20260909)
    bci_new = (lambda x: cluster_boot_ci(x, grp, rr_new, a.boot)) if use_cluster else (lambda x: boot_ci(x, rr_new, a.boot))
    with Path(outdir, "summary.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["model", "method", "level", "n_start", "n_reached", "reach_rate", "cf_mean", "cf_lo", "cf_hi",
                                       "kl_mean", "kl_lo", "kl_hi", "steps_mean",
                                       "kl99_mean", "kl99_lo", "kl99_hi", "rd_mean", "rd_lo", "rd_hi",
                                       "cfdev_mean", "cfdev_lo", "cfdev_hi", "klbin_mean", "klbin_lo", "klbin_hi",
                                       "klpair_mean", "klpair_lo", "klpair_hi", "klneu_mean", "klneu_lo", "klneu_hi", "cf0_mean"])
        summ = {}
        for L in levels:
            for m in methods:
                cf = bci(col(m, L, "cf")); kl = bci(col(m, L, "kl"))
                nr = int(np.sum(~np.isnan(col(m, L, "kl")))); st = float(np.nanmean(col(m, L, "step"))) if nr else float("nan")
                summ[(L, m)] = (nr / len(test_idx), cf, kl)
                k99 = bci(col(m, L, "kl99")); rdv = bci(col(m, L, "rd"))
                w.writerow([model, m, L, len(test_idx), nr, round(nr / len(test_idx), 4), *np.round(cf, 5), *np.round(kl, 5), round(st, 1),
                            *np.round(k99, 5), *np.round(rdv, 5),
                            *np.round(bci_new(col(m, L, "cf_dev")), 5), *np.round(bci_new(col(m, L, "kl_bin")), 5),
                            *np.round(bci_new(col(m, L, "kl_pair")), 5), *np.round(bci_new(col(m, L, "kl_neu")), 5),
                            round(float(np.nanmean(col(m, L, "cf0"))), 5) if nr else ""])
    comps = [c for c in [("euclid", "dual"), ("causal_fixed", "dual"), ("euclid", "causal_fixed"), ("euclid_unemb", "causal_unemb"),
                         ("euclid_unemb", "dual"), ("causal_unemb", "dual"), ("euclid", "euclid_unemb"), ("euclid", "causal_unemb")]
             if c[0] in methods and c[1] in methods]; pair_rows = []
    with Path(outdir, "paired.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["level", "a", "b", "n_paired", "kl_diff_mean", "kl_diff_lo", "kl_diff_hi",
                                       "frac_ctx_b_lower_kl", "cf_diff_mean", "cf_diff_lo", "cf_diff_hi"])
        for L in levels:
            for x, y in comps:
                dk = col(x, L, "kl") - col(y, L, "kl"); dc = col(x, L, "cf") - col(y, L, "cf"); ok = ~np.isnan(dk)
                ck = bci(dk); cc = bci(dc); win = float(np.mean(dk[ok] > 0)) if ok.any() else float("nan")
                row = [L, x, y, int(ok.sum()), *np.round(ck, 5), round(win, 4), *np.round(cc, 5)]; w.writerow(row); pair_rows.append(row)
    if a.optgap > 0:
        pr = {"ctx": beta, "unemb": gbar, "dmd": beta_phi}; rows = []
        for n, i in enumerate(test_idx[: a.optgap]):
            lam0 = ops.vec(Eb[i]); p0 = ops.probs(lam0)
            for m in methods:
                pn = m.split("_")[-1]
                if pn not in pr or res[m][n].get("_lam") is None: continue
                lam_end = res[m][n]["_lam"]; bt = pr[pn]; c = float(bt @ ops.tonp(lam_end).astype(np.float64))
                lam_opt = ops.hyperplane_min(lam0, bt, c, topk); p_end = ops.probs(lam_end); p_opt = ops.probs(lam_opt)
                ke, ko = ops.kl_full(p0, p_end), ops.kl_full(p0, p_opt)
                rows.append([int(i), m, pn, round(c, 5), round(ke, 5), round(ko, 5), round(ke - ko, 5),
                             round(ops.stats(p_end)[0], 5), round(ops.stats(p_opt)[0], 5)])
            print(f"  optgap {n + 1}/{min(a.optgap, len(test_idx))}", flush=True)
        with Path(outdir, "optgap.csv").open("w", newline="") as f:
            w = csv.writer(f); w.writerow(["ctx_id", "method", "probe", "c", "kl_full_end", "kl_full_opt", "gap", "P1_end", "P1_opt"]); w.writerows(rows)
    with Path(outdir, "timing.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["ctx_id", "method", "seconds", "steps_run"])
        for n, i in enumerate(test_idx):
            for m in methods: w.writerow([int(i), m, round(tim[m][n][0], 4), tim[m][n][1]])
    PRIMARY = {("euc_dmd", "dua_dmd"), ("euc_unemb", "cau_unemb"), ("cau_unemb", "dua_unemb"), ("cau_dmd", "dua_dmd")}
    gc = []
    for p in ("ctx", "unemb", "dmd"):                       # metric effects within a probe
        gc += [(f"euc_{p}", f"cau_{p}"), (f"euc_{p}", f"dua_{p}"), (f"cau_{p}", f"dua_{p}")]
    for m in ("euc", "cau", "dua"):                         # probe effects within a metric
        gc += [(f"{m}_ctx", f"{m}_unemb"), (f"{m}_ctx", f"{m}_dmd"), (f"{m}_unemb", f"{m}_dmd")]
    gc = [c for c in gc + comps if c[0] in methods and c[1] in methods]
    with Path(outdir, "paired_long.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["level", "a", "b", "metric", "n_paired", "diff_mean", "diff_lo", "diff_hi",
                                       "frac_ctx_b_better", "is_primary", "ci_type"])
        for L in levels:
            for x, y in gc:
                for met in ("kl", "kl99", "rd", "cf_dev", "kl_bin", "kl_pair", "kl_neu", "cf"):
                    dd = col(x, L, met) - col(y, L, met); ok = ~np.isnan(dd)
                    ci = bci(dd); better = (dd[ok] > 0)                    # b better = lower value; 'cf' has NO direction (frac left blank)
                    w.writerow([L, x, y, met, int(ok.sum()), *np.round(ci, 5), round(float(better.mean()), 4) if (ok.any() and met != "cf") else "",
                                int((x, y) in PRIMARY and abs(L - a.primary_level) < 1e-9 and met == "kl"), "cluster" if use_cluster else "plain"])
    with Path(outdir, "per_context.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["ctx_id", "text", "method", "level", "reached", "step", "P1", "cf", "kl", "kl99", "rd", "cf0", "cf_dev", "kl_bin", "kl_pair", "kl_neu"])
        for n, i in enumerate(test_idx):
            for m in methods:
                for L in levels:
                    r = res[m][n][L]
                    w.writerow([int(i), D["tb"][i], m, L, int(r is not None), r["step"] if r else "", round(r["P1"], 5) if r else "",
                                round(r["cf"], 5) if r else "", round(r["kl"], 5) if r else "",
                                round(r["kl99"], 5) if r else "", round(r["rd"], 5) if r else "",
                                round(r["cf0"], 5) if r else "", round(r["cf_dev"], 5) if r else "", round(r["kl_bin"], 5) if r else "",
                                round(r["kl_pair"], 5) if r else "", round(r["kl_neu"], 5) if r else ""])
    with Path(outdir, "final.csv").open("w", newline="") as f:
        w = csv.writer(f); w.writerow(["ctx_id", "method", "step_end", "P1_end", "cf_end", "kl_end", "H_start", "H_end", "cf0"])
        for n, i in enumerate(test_idx):
            for m in methods:
                r = res[m][n]["_final"]
                w.writerow([int(i), m, r["step"], round(r["P1"], 5), round(r["cf"], 5), round(r["kl"], 5),
                            round(r["H_start"], 4), round(r["H_end"], 4), round(r["cf0"], 5)])
    checks = dict(logits_rel_err=D["meta"].get("logits_rel_err"), probe_heldout_auc=probe_auc,
                  n_base_raw=len(Eb), n_base_kept=int(len(kb)), n_target_raw=len(Et), n_target_kept=int(len(kt)),
                  n_steered=int(len(test_idx)), cos_euclid_causal=cos_ec, alpha=alpha, probe_cos=probe_cos, filter=a.filter, park_mass=a.park_mass,
                  cf0_mean_test=float(np.mean([res[next(iter(methods))][n]["_final"]["cf0"] for n in range(len(test_idx))])),
                  alpha_over_mean_eig_S0=alpha / mean_eig_S0, sigma_t_diag=sig_diag, ci_type="cluster" if use_cluster else "plain")
    Path(outdir, "checks.json").write_text(json.dumps(checks, indent=1))
    Path(outdir, "config.json").write_text(json.dumps(
        dict(args=vars(a), backend=ops.name, V=int(V), d=int(d), n_pairs=int(len(pairs)), meta=D["meta"],
             python=platform.python_version(), numpy=np.__version__, runtime_s=round(time.time() - t_start, 1)),
        indent=1, default=str))
    try:
        import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 2, figsize=(9, 3.4))
        for m in methods:
            for j, k in enumerate((1, 2)):
                mu = [summ[(L, m)][k] for L in levels]
                ax[j].errorbar(levels, [x[0] for x in mu], yerr=[[x[0] - x[1] for x in mu], [x[2] - x[0] for x in mu]],
                               marker="o", capsize=3, label=m)
        ax[0].set_title("counterfactual mass (higher = less leakage)"); ax[1].set_title("off-target KL (lower = better)")
        for x in ax: x.set_xlabel("target prob P(W=1)")
        ax[0].legend(); plt.tight_layout(); plt.savefig(Path(outdir, "curves.png"), dpi=150)
    except Exception as e: print("plot skipped:", e)
    with Path(outdir, "report.md").open("w") as f:
        f.write(f"# Steering comparison: {model}\n\nbackend={ops.name}, V={V}, d={d}, pairs={len(pairs)}, steered contexts={len(test_idx)}, "
                f"alpha_rel={a.alpha_rel}, step_frac={a.step_frac}, max_steps={a.max_steps}, seed={a.seed}\n\n"
                f"Checks: logits_rel_err={checks['logits_rel_err']}, probe held-out AUC={probe_auc:.3f}, cos(euclid,causal)={cos_ec:.3f}\n\n"
                "## Reach rate and off-target KL (mean [95% bootstrap CI] over contexts)\n\n| level | method | reach | cf mass | off-target KL |\n|---|---|---|---|---|\n")
        for L in levels:
            for m in methods:
                rch, cf, kl = summ[(L, m)]; f.write(f"| {L} | {m} | {rch:.2f} | {cf[0]:.3f} [{cf[1]:.3f},{cf[2]:.3f}] | {kl[0]:.3f} [{kl[1]:.3f},{kl[2]:.3f}] |\n")
        f.write("\n## Paired KL difference a - b (>0 means b is better)\n\n| level | a | b | n | diff [CI] | P(b lower KL) |\n|---|---|---|---|---|---|\n")
        for r in pair_rows: f.write(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]:+.3f} [{r[5]:+.3f},{r[6]:+.3f}] | {r[7]:.2f} |\n")
        f.write("\n## Caveats (keep these when presenting)\n- Paired comparisons use only contexts where both methods reach the level; check reach rates (selection bias).\n"
                "- Template contexts, one concept (verb -> 3rd person), small model unless stated.\n- Results depend on alpha_rel; report the sweep.\n"
                "- Probe is trained on templates; AUC above is held-out within the same templates.\n")
    print(f"\nsaved to {a.out}/  ({time.time() - t_start:.0f}s)")


if __name__ == "__main__":
    main()
