# 下一步实验方案与交付审查要求（V3）

适用：`CaroVon/Rep_test`，在 `AGGREGATE_V2.md` 之后的下一轮。
配套脚本：`steer_compare_v3.py`（在 v2 基础上新增，见 §2.4）。
本文既是**实验任务书**，也是**交付审查标准**：执行者（包括你的编码代理）按 §3 做，我按 §5 审。

---

## 0. 这一轮要回答的问题

V2 之后的状态：

- dual 的到达问题已解决（α 到 ~5e-3 即到达），但**在 Park 的 α 上，dual（用上下文均值差作探针）的 off-target KL 约为欧氏的 3 倍**（3.31 vs 1.12）；α=0.1 时才小幅优于欧氏（+0.10 [0.03, 0.18]）。
- `causal_unemb`（Cov⁻¹ 作用于 unembedding 差）稳定优于原始 unembedding 差（三个设置下区间不含 0），但相对欧氏上下文均值差的优势在 Gemma 上不稳（`mm0.5` 下差为 +0.001）。
- **探针与度量被混在一起比较**：dual 用的是上下文均值差 β，`causal_unemb` 用的是 unembedding 差 γ̄，两者余弦只有 0.476。Park 2026 的主图用的是第三种探针 Dual MD（β^Φ），我们还没有跑。

所以本轮把"探针"和"度量"分开，做 3×3 因子设计，并回答四个**预先指定**的问题：

| 编号 | 问题 | 比较（a vs b） | 为什么 |
|---|---|---|---|
| Q1 | Park 2026 的主张在我们设置下是否成立？ | `euc_dmd` vs `dua_dmd`（α=5e-3） | 复现其主图设定（Dual MD 探针） |
| Q2 | Park 2024 的 Cov⁻¹ 预处理是否改进原始 unembedding 差？ | `euc_unemb` vs `cau_unemb` | 已有证据，做确认与扩展 |
| Q3 | 同一探针 γ̄ 下，自适应度量比固定度量好多少？ | `cau_unemb` vs `dua_unemb` | **本项目核心问题** |
| Q4 | 同一探针 β^Φ 下，自适应比固定好多少？ | `cau_dmd` vs `dua_dmd` | Q3 的第二个探针重复 |

其余所有比较都是**探索性**的，只能作假设生成，不得作为结论。

**预设判读规则（建议值，由你和 Victor 确认后锁定）：**
- 指标：水平 0.9 的 off-target KL（`kl`）；`kl99`、`rd`、`cf` 为稳健性指标。
- 差值 = a − b，大于 0 表示 b 更好。
- "b 优于 a"：区间下界 > 0。"差异不能确立"：区间跨 0。
- "实质等价"：区间整体落在 ±0.05 以内（约为 KL 1.0 的 5%，这是依据当前效应量选的边际，不是标准值）。

---

## 1. 设计

### 1.1 3×3 因子

| | 欧氏 `euc` | 固定因果 `cau` | 自适应 `dua` |
|---|---|---|---|
| 探针 `ctx`：上下文均值差 β | `euc_ctx` | `cau_ctx` | `dua_ctx` |
| 探针 `unemb`：unembedding 词对差 γ̄ | `euc_unemb` | `cau_unemb` | `dua_unemb` |
| 探针 `dmd`：Dual MD，β^Φ | `euc_dmd` | `cau_dmd` | `dua_dmd` |

方向定义（都归一化后以步长 η 前进）：

| 度量 | 方向 |
|---|---|
| `euc` | v = 探针 |
| `cau` | v = (S₀ + ε I)⁻¹ · 探针，S₀ 为整个词表的均匀协方差，只算一次；ε = `--ridge_rel` × tr(S₀)/d |
| `dua` | v = (Σₜ + α I)⁻¹ · 探针，Σₜ = Cov[γ∣λₜ]（top-K 加共轭梯度），每步重算 |

探针定义：

- `ctx`：β = mean(λ_target,train) − mean(λ_base,train)。
- `unemb`：γ̄ = mean_i (G[y¹ᵢ] − G[y⁰ᵢ])。
- `dmd`：β^Φ = mean(φ(λ_target,train)) − mean(φ(λ_base,train))，φ(λ) = softmax(Gλ)ᵀG，用**完整词表**计算。

注意：`cau_*` 的正则是 ε（`--ridge_rel`），`dua_*` 的正则是 α（`--alpha_abs`）。两者含义不同，不要混用。

### 1.2 指标

| 名称 | 定义 | 方向 |
|---|---|---|
| `kl` | KL(P⁰ᶻ ‖ Pᵗᶻ)，对"各反事实对的合并质量 + 每个中性 token"求和 | 越低越好 |
| `kl99` | 同上，但只在 P⁰ᶻ 累计 0.99 质量的 token 子集上求和（不重新归一化） | 越低越好 |
| `rd` | Σ_{z∈S} P⁰ᶻ(z)·\|1/rankₜ(z) − 1/rank₀(z)\|，S 同上；排名只在 S 内计算 | 越低越好 |
| `cf` | 反事实质量和（各对 y⁰、y¹ 的概率和） | 越高越好 |

`rd` 是 Park 2026 逆排名差的简化版：他们对多个步骤的 top-0.99 token 取并集，我们只用起点的 S。报告里必须注明这一偏离。

### 1.3 上下文、种子、水平

- 水平：目标概率 P(W=1) ∈ {0.3, 0.5, 0.7, 0.9, 0.99}；主水平 0.9。
- 上下文：先沿用现有模板做试点，终稿用扩展模板（≥16 个主语、10 种前缀，见 `EXPERIMENT_REVIEW_AND_FIXES.md` §2.3）。**两组必须使用相同句式框架**，只让主语数不同。
- 种子：试点 1 个，终稿 ≥3 个（每个种子**重新提取**上下文并重新划分训练/测试）。
- 到达率必须报告。配对比较只用两种方法都到达的上下文，到达率低时要同时给出水平 0.5 的结果作敏感性检验。

---

## 2. 代码

### 2.1 基线
基于仓库当前的 `steer_compare_v2.py`（含路径清洗 `safe_run_dir`）。

### 2.2 新增文件
`steer_compare_v3.py`，由 v2 改动而来，**不改任何已有方法的数学定义**。

### 2.3 测试状态
- numpy 后端：已在合成数据上完整端到端测试，`--selftest` 通过，输出文件齐全。
- **torch 后端：新增的四个算子 `phi`、`top_idx`、`kl_sub`、`rankdiff` 没有测试过**（我的沙箱装不上 torch）。WP0 必须验证。

### 2.4 v3 相对 v2 的改动

| 改动 | 说明 |
|---|---|
| `--methods grid`（默认） | 运行上表 9 种方法；仍可传逗号列表，旧名称（`euclid`、`causal_fixed`、`dual`、`euclid_unemb`、`causal_unemb`）仍可用 |
| Dual MD 探针 | 新增 `ops.phi`，计算 β^Φ |
| `kl99`、`rd` | 每个水平记录，写入 `summary.csv`（末尾新增列）与 `per_context.csv` |
| `paired_long.csv` | 长格式，所有比较 × 4 个指标，含 `is_primary` 标记；列：`level,a,b,metric,n_paired,diff_mean,diff_lo,diff_hi,frac_ctx_b_better,is_primary,ci_type` |
| `checks.json` | 新增 `probe_cos`（三种探针两两余弦） |
| `--primary_level` | 默认 0.9，用于 `is_primary` 标记 |

`paired_long.csv` 里 `frac_ctx_b_better` 的含义：对 `kl`、`kl99`、`rd`，是 b 的数值更低的上下文比例；对 `cf`，是 b 更高的上下文比例。

---

## 3. 工作包

预估时间来自你们 V1/V2 的运行时间（gemma-1b、80 条上下文、三种方法约 30 分钟，主要耗时在 dual 未到达时跑满 600 步）。**都是估计，请先用 `--n_ctx 5` 实测。**

### WP0：环境与后端对等（门槛 G0）

```bash
python steer_compare_v3.py --selftest
python steer_compare_v3.py --synthetic --backend numpy --n_ctx 10 --max_steps 100 --topk 1500 --out runs/syn_v3_np
python steer_compare_v3.py --synthetic --backend torch --n_ctx 10 --max_steps 100 --topk 1500 --out runs/syn_v3_torch
python - <<'PY'
import pandas as pd
a=pd.read_csv('runs/syn_v3_np/summary.csv'); b=pd.read_csv('runs/syn_v3_torch/summary.csv')
cols=['reach_rate','cf_mean','kl_mean','kl99_mean','rd_mean','steps_mean']
print((a[cols]-b[cols]).abs().max())
PY
```

通过标准：`SELFTEST PASS`（两后端）；`reach_rate` 完全一致；`cf_mean`、`kl_mean`、`kl99_mean` 差 ≤1e-3；`rd_mean` 差 ≤1e-2（排名在近似并列时对浮点误差敏感）；`steps_mean` 差 ≤1 步。若超出，必须定位原因，不能直接跳过。

### WP1：与作者实现逐步对照（门槛 G0）

目的：判断"dual 在 α=5e-3 时 KL 约为欧氏 3 倍"是实现差异还是现象。

做法：在同一个上下文 λ₀、同一个探针 β、同一个 α、同一个 top-K 下，分别调用你们的 `dual_dir` 与作者仓库 `KihoPark/dual-steering` 的实现，比较：
1. 第一步方向的余弦；
2. 前 20 步的 P(W=1) 与分布熵的轨迹；
3. 差异的代码位置（归一化、top-K 取法、CG 容差、正则位置等）。

交付：`repro_check.md`，含上述三项的表格。

通过标准：第一步余弦 ≥ 0.99，且前 20 步 P(W=1) 的相对差 ≤ 5%；否则**必须**写明差异点，并判断哪一方偏离了论文描述。

限制：我没有读过作者代码。若他们的函数依赖 4B 模型或特定数据格式而无法单独调用，退一步：逐行对照算法并列出差异，同时在 `repro_check.md` 里如实说明没能做数值对照。

### WP2：gemma-1b 3×3 试点（门槛 G1）

```bash
for A in 1e-3 5e-3 2e-2 1e-1; do
  python steer_compare_v3.py --data_dir data/gemma1b --backend torch --topk 20000 \
    --methods grid --alpha_abs $A --n_ctx 20 --seed 0 --out runs/gemma1b_v3/pilot_abs${A}
done
```

预估：dual 三种方法 × 20 条上下文 × 4 个 α，约 30–60 分钟（视到达步数）。

产出：每个 run 的标准文件（见 §4）。

### WP3：指标与长尾敏感性（门槛 G1）

从 WP2 的 `summary.csv` 与 `paired_long.csv` 读出：

1. `dua_ctx` 在 α=5e-3 时 `kl` 与 `kl99` 的差。若 `kl99` 明显更小，说明 3.3 里有大量来自长尾，写入报告。
2. Q1–Q4 的 `kl`、`kl99`、`rd`、`cf` 四个指标是否同向。若不同向，如实报告，不得只挑一个。
3. 起点 Σₜ 谱诊断（`checks.json:sigma_t_diag`）与 `final.csv` 的熵变化，用来解释 dual 的行为。

### WP4：扩大样本（门槛 G2）

只在 G1 通过后进行。

1. 用扩展模板在 gemma-1b 上重新提取，种子 0、1、2：`extract_embeddings.py --seed S --out_dir data/gemma1b_s{S}`。
2. 每个种子：`--n_ctx 60`，α_dual ∈ {5e-3, 2e-2, 1e-1}（若 WP2 显示某个 α 到达率过低，可替换，并记录原因）。
3. 第二个模型：GPT-2，同样的网格（GPT-2 上 S₀ 近奇异，`--ridge_rel` 用 1e-6）。
4. gemma-4b 4-bit 仅在前面全部完成且时间允许时做，只跑 α=5e-3，并标注量化。

### WP5：稳健性

在一个种子、gemma-1b 上各做一次：

| 因素 | 取值 |
|---|---|
| `--ridge_rel` | 1e-8、1e-6、1e-4 |
| `--min_mass` | 0.15、0.5、0.7（要说明保留的上下文数） |
| `--step_frac` / `--max_steps` | 0.01/600、0.02/1200 |

### WP6：汇总

写 `aggregate.py`，从各 run 的 CSV 自动生成 `runs/AGGREGATE_V3.md` 中的**所有表格与数字**。**不得手工抄数。**

---

## 4. 交付物

```
runs/
  AGGREGATE_V3.md            # 由 aggregate.py 生成 + 人写的结论节
  gemma1b_v3/<run>/          # 每个 run 一个目录
    config.json  checks.json  summary.csv  paired.csv  paired_long.csv
    per_context.csv  final.csv  curves.png  report.md
  gpt2_v3/<run>/
repro_check.md               # WP1
DEVIATIONS.md                # 任何偏离本文的地方
commands.log                 # 实际执行过的全部命令，按时间顺序
aggregate.py
data_manifest.json           # data/* 各文件的 sha256、形状、模型名与量化设置
env.txt                      # pip freeze + python/torch/transformers/CUDA 版本 + GPU 型号
```

`AGGREGATE_V3.md` 必须包含的表：

1. 数据与检验：每个模型/种子的 `logits_rel_err`、探针 AUC、保留上下文数、`probe_cos`。
2. 3×3 网格主表：水平 0.9 下 9 种方法的 `reach_rate`、`kl`、`kl99`、`rd`、`cf`（均值与区间）、平均步数。
3. 预先指定的 Q1–Q4：差值、区间、`n_paired`、`frac_ctx_b_better`，以及按下文 §5 的判读标签。
4. 探索性比较：全部列出，标明"探索性"。
5. 稳健性（WP5）与长尾敏感性（WP3）。
6. 逐步对照结果（WP1）摘要。
7. **证据—结论对应表**：每条结论一行，列出所依据的 run 目录与 CSV 行。

图：
- 每个模型一张：9 种方法的 `kl` 与 `cf` 随目标概率的曲线（含区间）。
- 一张森林图：Q1–Q4 的差值与区间（四个指标各一版）。

---

## 5. 交付审查要求

审查分三道门，每道门**不通过就不进入下一阶段**。

### 5.1 门槛清单

| 门槛 | 时点 | 提交内容 | 必须通过 |
|---|---|---|---|
| G0 | WP0–WP1 后 | 后端对等输出、`repro_check.md`、`env.txt`、`commands.log` | §5.2 的 A、B 项；WP0、WP1 的通过标准 |
| G1 | WP2–WP3 后 | `gemma1b_v3/pilot_*`、WP3 表格、初步 `AGGREGATE_V3.md` | §5.2 的 A–D 项 |
| G2 | 全部完成后 | 全部交付物 | §5.2 全部项 |

### 5.2 审查项

**A. 可复现性**
- [ ] 每个 run 的 `config.json` 记录全部参数、种子、后端、版本、运行时间。
- [ ] `data_manifest.json` 含 `G.npy`、`E_base.npy`、`E_target.npy`、`pairs.npy`、`contexts.json` 的 sha256。
- [ ] `commands.log` 完整，按其顺序可以重跑出同样的 CSV（允许浮点小差）。
- [ ] 提交到仓库，并打标签 `v3-g0`、`v3-g1`、`v3-g2`；提交信息说明本次变更。
- [ ] 脚本相对 `steer_compare_v3.py` 的任何修改，列在 `DEVIATIONS.md` 并给出 diff。

**B. 代码与检验**
- [ ] `--selftest` 在两后端通过；WP0 对等检验满足 §3 的容差。
- [ ] 保留了 `safe_run_dir`。
- [ ] 没有改动已有方法的数学定义；若改了，必须在 `DEVIATIONS.md` 里写明，且之前的结论作废重跑。
- [ ] 每个 run 满足护栏：`logits_rel_err` ≤ 5e-2（fp32 模型 ≤ 1e-3）；探针留出 AUC ≥ 0.8；`n_steered` 试点 ≥ 20、终稿 ≥ 60。
- [ ] 终稿中聚类自助法的簇数 ≥ 12；`ci_type` 为 `cluster`。

**C. 统计规范**
- [ ] 只有 Q1–Q4 作为确认性比较；其余一律标"探索性"。
- [ ] 报告所有指定的运行，**包括对假设不利的**（例如 `mm0.5` 那一次）。不得只挑一部分。
- [ ] 每个比较报告 `n_paired` 与到达率；到达率 < 0.8 的方法必须注明，并给出水平 0.5 的敏感性结果。
- [ ] 效应量用原始 KL 差，同时给出相对比例（差 / 基线）。
- [ ] 终稿报告跨种子的差异（每个种子的点估计，不只是合并后的区间）。
- [ ] 多重比较：对 Q1–Q4 说明是否做校正；若不校正，明确写"未校正"。
- [ ] 不用 p 值措辞描述 `frac_ctx_b_better`。

**D. 结论纪律**

每条结论只能使用下列标签之一：

| 标签 | 条件 |
|---|---|
| 已确立 | 区间下界 > 0，且在所有指定种子与稳健性设置下方向一致 |
| 方向一致但未确立 | 点估计同向，但区间跨 0，或只在部分设置下同向 |
| 不能确立 | 区间跨 0 且方向不一致 |
| 实质等价 | 区间整体落在 ±0.05 以内 |

另外：
- [ ] 每条结论注明适用范围：模型、概念（动词第三人称）、上下文类型（模板）、probe 类型。
- [ ] 不得把不同探针的结果合并成一个结论。
- [ ] 禁用表述：
  - "复现成功/失败"：除非 WP1 通过，且 Q1 有明确结果；
  - "在所有 α 下"：固定方向与 α 无关，不能这样说；
  - "机制已证实"：熵与特征谱只能作为支持证据；
  - "没有优势"：必须配"在本设置下"。
- [ ] 与 Park 2026 的差异（`rd` 的简化、4-bit、模板上下文）列在"局限"一节。

**E. 报告与数字一致性**
- [ ] `AGGREGATE_V3.md` 中所有数字由 `aggregate.py` 生成；我会随机抽 10 个数字对照 CSV。
- [ ] 证据—结论对应表中的每个引用都能在对应 CSV 里找到。

### 5.3 红线（出现即退回）

1. 汇总中的数字与 CSV 不符，或手工抄写。
2. 遗漏已运行的 run，或只报告对结论有利的子集。
3. 修改算法未记录。
4. 结论的措辞与区间矛盾（例如区间跨 0 却写"优于"）。
5. 缺少到达率，或把到达率不同的方法直接合并比较。
6. 把不同探针家族的结果混在一个结论里。

### 5.4 我审查时会看什么

1. 先看 `checks.json` 与 `config.json`，确认护栏通过、参数与本文一致。
2. 再看 `summary.csv` 的到达率，然后看 `paired_long.csv` 的 Q1–Q4。
3. 抽查 `per_context.csv` 与 `final.csv`，核对汇总里的数字与图。
4. 最后读结论节与"证据—结论对应表"，逐条核对标签与区间。

---

## 6. 决策树

| WP2/WP3 的结果 | 下一步 | 可写的研究表述 |
|---|---|---|
| Q1 成立：`dua_dmd` 显著优于 `euc_dmd` | 进入 WP4，聚焦 Q3、Q4 | "Dual MD 探针下可复现对偶 steering 的优势；固定度量能保留其中多少" |
| Q1 不成立，但 `dua_dmd` 与 `euc_dmd` 实质等价 | 做 WP1 的差异定位后，仍可做 Q2–Q4 | "在我们的设置下对偶 steering 无优势；探针与度量的作用被分离" |
| Q1 不成立，且 `dua_dmd` 明显更差，WP1 显示实现一致 | 写成负结果，并联系作者 | "α 与探针选择对对偶 steering 的敏感性" |
| WP1 显示实现差异 | 修正后**重跑 WP2**，之前的 V2 结论作废 | — |
| Q3/Q4 的 `cau` 与 `dua` 实质等价 | 固定度量足够，便宜得多 | "预先计算的度量可以替代自适应度量" |
| Q3/Q4 的 `dua` 明显更好 | 刻画差距随上下文集中度的变化（用 `final.csv`、Σₜ 谱） | "自适应度量在低熵上下文中的价值" |
| Q2 在新设置下不再成立 | 查看 `probe_cos`、上下文过滤的影响 | 作为稳健性限制写入 |

---

## 7. 已知风险与限制

- 只有一个概念（动词第三人称）、一类模板上下文，结论不能外推到其他概念或自然文本。
- `rd` 是简化版，与 Park 的定义不完全一致。
- 4-bit 的 gemma-4b 与 Park 的模型不是严格同一设置。
- 聚类自助法的区间在簇数较少时仍然很粗；这是需要扩大主语列表的原因。
- 预设的 ±0.05 等价边际是我基于当前效应量的建议，需要你与 Victor 确认。
- Park 的 α=5e-3 能否与我们的嵌入尺度直接对应，没有被验证；WP1 的对照应当一并说明。
- 本文没有涉及 torch 路径新算子在真实 GPU 上的数值精度，WP0 只在合成数据上检验。
