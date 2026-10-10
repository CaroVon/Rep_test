# 最终版实验任务书（V5）— 交给本地模型执行

> **使用方法：** 把本文件、`steer_compare_v5.py`、`analyze_v5.py`、`selfcheck_v5.py` 放进仓库根目录，然后让本地模型"完整阅读本文件并按顺序执行，遇到歧义按本文默认值处理并记入 `DEVIATIONS.md`，不要中途询问"。
> 仓库：`CaroVon/Rep_test`。硬件：RTX 4060 8GB。

---

## 1. 你的角色与硬性规则

你是这个研究项目的**实验执行与整理者**。你的工作是：运行实验、验证实现、从 CSV 生成数字、写出忠实于数据的结论。你**不是**在优化结果。

**硬性规则（违反任何一条，交付作废）：**

1. **所有数字必须来自 CSV 或脚本输出。** 不得手工抄写、估算或"润色"任何数字。任何表格由脚本生成。
2. **不得修改已验证的算法。** `steer_compare_v5.py` 中已有方法的数学定义不可改。若发现 bug，先在 `DEVIATIONS.md` 写明（附 diff 与证据），并重新跑回归。
3. **报告全部运行，包括对假设不利的。** 不得只挑有利的子集。
4. **区间跨 0 时不得写"优于"。** 只能用第 8 节的四个结论标签。
5. **指标政策：** `cf` 无方向，不得写"`cf` 越高越好"。凡说"某方法更好/更差"，必须同时写出 `kl`、`kl_park`、`rd`、`cf_dev` 四个指标各自的方向。
6. **独立单元计数：** 独立单元 = （模型，种子，概念，区域）。固定方法的结果与 α 无关，同一单元内只计一次；不同 α 是单元内的敏感性，不是独立重复。
7. **未运行的内容写"未检验"**，不得推断或估计。
8. **一次只运行一个批处理。** 先检查 `ps`/`nvidia-smi`，禁止并发抢占 GPU（V4 发生过孤儿进程事故）。
9. **结论不放在会被脚本重写的文件里。** 手写结论单独成文件 `CONCLUSIONS_V5.md`。
10. 不得声称"复现成功/失败"，除非本文第 8 节的判定规则明确满足。

---

## 2. 项目背景（你需要知道的事实）

**研究问题：** 在 Park 2026（The Information Geometry of Softmax）的 softmax 层 steering 设定下，预先计算的固定度量 Cov(γ)⁻¹（Park 2024 的因果内积）能捕获自适应对偶 steering 多少优势？它在哪些上下文失效？

**三类方法（只有方向不同，步长、探针、停止规则相同）：**

| 度量 | 方向 | 含义 |
|---|---|---|
| `euc` | v = 探针 | 欧氏 |
| `cau` | v = (S₀ + εI)⁻¹ · 探针 | S₀ = 整个词表的**均匀**协方差，只算一次 |
| `dua` | v = (Σₜ + αI)⁻¹ · 探针 | Σₜ = Cov[γ∣λₜ]（softmax 加权，top-K 加共轭梯度），每步重算 |
| `frq`（V5 新增） | v = (S_w + εI)⁻¹ · 探针 | S_w = **数据平均分布**加权的协方差，只算一次 |

**三种探针：** `ctx`（上下文均值差）、`unemb`（unembedding 词对差，Park 2024 的原法）、`dmd`（Dual MD：φ(λ) 的均值差，Park 2026 主图用的）。
方法名 = `{euc|cau|dua|frq}_{ctx|unemb|dmd}`。

**已有结论（V1–V4，已核实）：**

- 实现与作者代码逐步等价：第一步方向余弦 1.000000（区域 A 与 C），轨迹相对差 4.8e-6。
- 探针类型决定自适应方法好坏：α=5e-3 时 `dua_ctx` 的 KL 约 3.3，`dua_dmd` 约 0.96。
- Cov⁻¹ 预处理改进原始 unembedding 差（`cau_unemb` 优于 `euc_unemb`），在两个概念、多个模型上成立（区域 C 内收益缩小）。
- **指标分歧：** 在区域 A 与 C 的所有种子上，自适应方法在 `rd`（排名保持）与 `cf_dev`（质量漂移）上显著更好，但在 `kl`（1e-12 下限）上更差，且这个 KL 差几乎全部来自 `kl_neu`（中性 token 内部的重分配）。
- **未解决：** Park 的 KL 在每个概率上加了 5e-3 的偏移，我们没有。区域 C 里中性质量只有约 8% 且分散，这个偏移很可能抹平 `kl_neu`。所以"区域 C 中自适应反而更差"这一结论目前**只对我们的 KL 成立**。
- 超平面最优性差距分析显示：超平面上 KL 最优点的 P1 仅约 0.04，即探针不变性（Park 定理 3.1 的前提）被严重违反。

**原计划的三个交付物及状态：**

| 交付物 | 状态 | V5 的任务 |
|---|---|---|
| 1. 复现 Park 2026 的一个概念，确认环境无偏差 | 实现已等价；"主张"取决于指标 | 用 `kl_park`（Park 的偏移）重新检验 |
| 2. 欧氏、因果、**词频加权**、对偶四种方法加区间与**随机方向对照** | 词频加权与随机对照**从未做** | 实现 `frq_*` 与随机探针对照 |
| 3. **优势预测分析**（起点熵、反事实质量、Hessian 有效秩能否预测对偶的优势） | **未做** | 逐上下文回归 |

---

## 3. V5 要回答的问题

| 编号 | 问题 | 对应输出 |
|---|---|---|
| Q-A | 在 Park 的 KL（ε=5e-3）下，区域 C 中的 C1、C2 是否仍然反向？ | `kl_park` 的 paired 差，每个种子 |
| Q-B | 固定度量（`cau`）与词频加权度量（`frq`）各自捕获了"欧氏→自适应"变化的多大比例？ | `capture_ratio.csv` |
| Q-C | 自适应相对其他方法的优势，能否由起点熵 H0、cf0、Σₜ 有效秩预测？ | `advantage_regression.csv` |
| Q-D | 自适应的 KL 代价有多少是度量本身带来的（与概念无关）？ | `null_control_summary.csv` |
| Q-E | 以上在两个区域（A、C）与多个模型上是否一致？ | `metric_panel.csv` + 汇总 |

---

## 4. 代码与测试状态

提供三个脚本，**放在仓库根目录**：

| 文件 | 作用 |
|---|---|
| `steer_compare_v5.py` | 在**仓库当前的** `steer_compare_v4.py`（含你们的 RNG 回归修复与优化器修复）基础上新增功能。默认参数下与 V4 的共有列逐位一致 |
| `analyze_v5.py` | 回归、捕获比例、随机探针对照汇总、指标面板 |
| `selfcheck_v5.py` | 交付前的自动检查 |

**v5 相对 v4 的新增：**

| 新增 | 说明 |
|---|---|
| `kl_park` | Park 的偏移 KL：Σ_z z₀·(log(z₀+5e-3) − log(zₜ+5e-3))，**不是真正的 KL（可以为负）**，只作为 Park 度量的复现。写入 `summary.csv`（末尾 `klpark_*`）、`per_context.csv`、`paired_long.csv`（指标 `kl_park`） |
| `ctx_features.csv` | **每个测试上下文**的起点特征：`H0`、`cf0`、`P1_0`、`sigma_trace`、`sigma_eig_max`、`sigma_pr`（参与比 (Σλ)²/Σλ²，即有效秩）、`sigma_n95`、`sigma_frac_above_alpha`、`cluster` |
| `--with_freq` | 增加 `frq_{ctx,unemb,dmd}`；权重 = 若干原始上下文（`--freq_ctx`，默认 300）上 softmax 的平均 |
| `--null_draws R --null_ctx N` | 随机探针对照：用**结构化零探针**（标签打乱的 `ctx`/`dmd` 探针；随机词对差作 `unemb` 探针），经**同一种度量**，走与真实路径**相同步数**，记录终点各指标，写 `null_control.csv` |
| 独立 RNG | 新增列使用独立随机数流，不改变已有列的自助法区间 |

**测试状态（必须读）：**

- numpy 后端：已在合成数据上完整测试。`kl_park`、`ctx_features.csv`、`frq_*`、`null_control.csv`、`analyze_v5.py`、`selfcheck_v5.py` 都跑通；默认参数下与 V4 的共有列**逐位一致**（max abs diff = 0.0）。
- **torch 后端新增的四个算子没有测试过**：`kl_park`、`probs_np`、`diff_mean_ids`、`weighted_cov`。**WP-0 必须先验证它们。**
- 我没有在真实模型上运行过任何 V5 代码。

---

## 5. 工作包（按顺序执行）

**时间都是粗估**（依据 V4 的计时：gemma-1b 约 12 分钟/运行）。先用 `--n_ctx 5` 实测。

### WP-0：环境与对等（门槛 G6）

```bash
python steer_compare_v5.py --selftest
for B in numpy torch; do
  python steer_compare_v5.py --synthetic --backend $B --n_ctx 12 --max_steps 150 --topk 1500 --alpha_abs 5e-3 \
     --with_freq --null_draws 2 --null_ctx 5 --out runs/syn_v5_$B
done
```

通过标准（逐文件比较两个后端）：

| 文件 | 标准 |
|---|---|
| `summary.csv` | `reach_rate` 完全一致；`kl_mean`、`klpark_mean`、`kl99_mean`、`klneu_mean`、`cfdev_mean` 差 ≤1e-3；`rd_mean` 差 ≤1e-2 |
| `ctx_features.csv` | `H0`、`cf0` 差 ≤1e-4；`sigma_pr`、`sigma_trace` 相对差 ≤1e-3 |
| `null_control.csv` | 行数一致；同一行的 `kl`、`kl_park` 差 ≤1e-3 |
| `checks.json` | `v5.freq_info.mean_eig_Sw` 相对差 ≤1e-3（验证 `weighted_cov`） |

若超出，必须先定位原因（精度？实现？），写入 `DEVIATIONS.md`，不得直接跳过。

### WP-1：回归（门槛 G6，硬门槛）

用 v5 的**默认参数**（不加 `--with_freq`、`--null_draws`）重跑两个 V4 运行，与 V4 输出逐列对比：

```bash
# 使用 V4 的同一数据目录与参数（见 commands.log），只换脚本与输出目录
python steer_compare_v5.py <与 V4 相同的参数> --out runs/gemma1b_v5/reg_s0_abs5e-3
python steer_compare_v5.py <与 V4 相同的参数> --out runs/gpt2_v5/reg_s0_abs5e-3
python selfcheck_v5.py --runs "runs/gemma1b_v5/reg_*" "runs/gpt2_v5/reg_*" --ref_from _v5 --ref_to _v4
```

通过标准：F7 无 FAIL，即 `summary.csv` 与 `per_context.csv` 的共有数值列与 V4 差 ≤1e-6。**不通过不得继续。**

### WP-2：主运行矩阵（门槛 G7）

所有运行统一参数：`--backend torch --methods grid --topk 20000 --n_ctx 60 --with_freq`。
α=5e-3 的运行加：`--null_draws 3 --null_ctx 30`。
区域 C 的运行加：`--filter park --park_mass 0.7 --park_k 3`。
输出目录：`runs/<model>_v5/<region>_s{S}_abs{α}`。

**优先级（P0 必须完成；P1、P2 视时间）：**

| 优先级 | 内容 | 运行数 |
|---|---|---|
| **P0** | gemma-1b，区域 A，concept third，种子 0、1、2，α=5e-3；区域 C，同样种子，α=5e-3 | 6 |
| P1 | gemma-1b 区域 A 与 C，种子 0、1、2，α=2e-2（**不加** null）；GPT-2 区域 A，种子 0、1、2，α=5e-3 | 9 |
| P1 | **扩大区域 C 的目标上下文**：重新提取，`--c4_docs` 增大（V4 的目标侧只有 25 条，探针只用其中约 12 条训练），目标是 ≥40 条目标上下文；数据目录 `data/gemma1b_c4big_s{S}`；重跑区域 C 的 α=5e-3 | 3 |
| P2 | gemma-4b（4-bit），区域 A，种子 0，α=5e-3 | 1 |
| P2 | concept ing，区域 A，gemma-1b 种子 0、1、2 与 GPT-2 种子 0，α=5e-3 | 4 |

**区域 C 的数据：** 用 V4 已有的 `data/gemma1b_c4_s{S}`；P1 的扩大版是补充，不得替代 V4 版（两者都要报告）。

**P0 完成后，立刻运行 WP-3、WP-4，产出中期 `STATUS.md`，再继续 P1/P2。**

### WP-3：分析

```bash
python analyze_v5.py --out results_v5/p0 \
  --group A_third_a5e-3 runs/gemma1b_v5/A_s0_abs5e-3,runs/gemma1b_v5/A_s1_abs5e-3,runs/gemma1b_v5/A_s2_abs5e-3 \
  --group C_third_a5e-3 runs/gemma1b_v5/C_s0_abs5e-3,runs/gemma1b_v5/C_s1_abs5e-3,runs/gemma1b_v5/C_s2_abs5e-3 \
  --pairs euc_dmd:dua_dmd,cau_unemb:dua_unemb,frq_unemb:dua_unemb,cau_unemb:frq_unemb,frq_dmd:dua_dmd
```

（运行目录名以你实际命名为准，保持 `<region>_s{S}_abs{α}`。）

约定：`diff = metric(a) − metric(b)`；所有指标都是越低越好；`diff > 0` 表示 b 更好。

### WP-4：自检（门槛 G7）

```bash
python selfcheck_v5.py --runs "runs/*_v5/*"
```

不得有 FAIL。F6 的 WARN（到达率 < 0.8）必须在汇总里逐条说明。

### WP-5：汇总

写 `aggregate_v5.py`（可在 `aggregate_v4.py` 基础上扩展），生成 `runs/AGGREGATE_V5.md`，**所有数字由脚本从 CSV 生成**。必须包含的节：

1. 数据与检验表：模型、区域、概念、种子、α、`logits_rel_err`、探针 AUC、保留数、`n_clusters`、`cf0_mean`、`H0` 均值。
2. 回归：与 V4 的最大差（WP-1）。
3. **指标面板**（核心表）：对 C1（`euc_dmd` vs `dua_dmd`）与 C2（`cau_unemb` vs `dua_unemb`），区域 A、C，每个种子一行，列出 `kl`、`kl_park`、`rd`、`cf_dev`、`kl_neu` 的差与区间（来自 `metric_panel.csv`）。
4. 捕获比例表（`capture_ratio.csv`）。
5. 优势回归表（`advantage_regression.csv`）与预测变量相关（`predictor_corr.csv`）。
6. 随机探针对照表（`null_control_summary.csv`）。
7. 成本表（沿用 V4 的 `timing.csv` 汇总，加 `frq_*`）。
8. 证据—结论对应表（每条结论：run 目录、CSV 文件与行、独立单元数、区域标签）。

### WP-6：结论

手写 `CONCLUSIONS_V5.md`，遵循第 8 节的标签与判定规则。**每个数字必须能在 `AGGREGATE_V5.md` 或 CSV 中找到。** 未运行的部分写"未检验"。

### WP-7：整理

1. `DEVIATIONS.md` 追加 V5 的所有偏离（包括任何你修改过的代码、未完成的优先级、计时异常）。
2. `commands.log` 追加全部实际命令（含 `git rev-parse HEAD`）。
3. `data_manifest.json` 追加新数据的 sha256。
4. `env.txt` 更新。
5. 作者仓库缺失 `F` 导入的问题：起草 issue 文本放进 `repro_check.md`，**不要自行提交**。
6. 打标签 `v5-g6`、`v5-g7`、`v5-final`。

---

## 6. 输出格式（新增文件）

**`ctx_features.csv`**（每个运行一个，每个测试上下文一行）：
`ctx_id, cluster, text, H0, cf0, P1_0, sigma_trace, sigma_eig_max, sigma_pr, sigma_n95, sigma_frac_above_alpha`

**`null_control.csv`**：
`ctx_id, method, draw, steps, P1_end, cf, cf0, kl, kl99, rd, cf_dev, kl_bin, kl_pair, kl_neu, kl_park`
（`steps` = 真实路径到达 0.9 水平所用步数；零探针走同样步数。）

**`summary.csv`、`per_context.csv`、`paired_long.csv`**：在 V4 的列之后追加 `klpark_*`、`kl_park`。

**`analyze_v5.py` 输出：**
- `advantage_regression.csv`：`group, pair(a-b), metric, model, term, coef_per_SD, lo, hi, R2, n, n_clusters`。模型含 `uni_H0`、`uni_cf0`、`uni_log_pr`、`joint`。区间为按簇的自助法；已做运行固定效应（按运行去均值）。
- `capture_ratio.csv`：`group, probe, metric, n, gap_euc_minus_dua, gap_lo, gap_hi, gap_defined, rho_cau(+lo/hi), rho_frq(+lo/hi)`。
 ρ = mean(euc − X) / mean(euc − dua)：1 表示与自适应相同，0 表示与欧氏相同。**只有 `gap_defined=True`（欧氏与自适应之间的差距本身的区间不含 0）时才可解读。**
- `null_control_summary.csv`、`metric_panel.csv`、`predictor_corr.csv`、`analysis_v5.md`。

---

## 7. 交付物清单

```
steer_compare_v5.py  analyze_v5.py  selfcheck_v5.py  aggregate_v5.py
runs/<model>_v5/<run>/   (config checks summary paired paired_long per_context final ctx_features timing [null_control] [optgap])
results_v5/              (analyze_v5.py 的全部输出)
runs/AGGREGATE_V5.md     (脚本生成)
CONCLUSIONS_V5.md        (手写)
STATUS.md                (P0 完成后的中期状态；最终版覆盖)
DEVIATIONS.md  commands.log  data_manifest.json  env.txt  repro_check.md
```

---

## 8. 预先指定的判定规则（不得事后更改）

### 8.1 确认性比较

| 编号 | 比较 | 区域 | α | 指标 | 单元 |
|---|---|---|---|---|---|
| **K1** | `euc_dmd` vs `dua_dmd`（C1） | C | 5e-3 | **`kl_park`** | 3 个种子 |
| **K2** | `cau_unemb` vs `dua_unemb`（C2） | C | 5e-3 | **`kl_park`** | 3 个种子 |

K1、K2 在区域 A 上的同样比较作为**复现**，不是确认。

### 8.2 K1 的解读表

| 结果（3 个种子，α=5e-3，区域 C） | 写法 |
|---|---|
| ≥2 个种子的区间下界 > 0（自适应更好），且无种子显著反向 | "在 Park 的 KL 下，区域 C 的反向消失，方向与 Park 一致；我们的 KL（1e-12 下限）下的反向是度量造成的" |
| 3 个种子都显著反向 | "反向对 Park 的偏移稳健" |
| 其他 | "不能确立" |

K2 同理。`kl_park` 不是真正的 KL，写法里必须注明。

### 8.3 描述性问题的预设判读

- **Q-B（捕获比例）：** 只在 `gap_defined=True` 时报告 ρ；用"区间与 0 和 1 的关系"描述（区间包含 1：与自适应无法区分；区间包含 0：与欧氏无法区分）。
- **Q-C（优势预测）：** 以 `joint` 模型为主，报告每个标准化预测变量的系数与区间、R²。**不得做因果表述。** 若三个预测变量高度相关（|corr| > 0.7），说明共线性，主要看单变量模型。判定"可预测"需同时满足：至少一个预测变量的区间在区域 A 与 C 中都排除 0 且方向一致，且 R² ≥ 0.1；否则写"这些特征未能稳定预测优势"。
- **Q-D（随机探针对照）：** 对每个方法报告 real、null、real − null 及区间，并报告 null/real 比。若 `dua_*` 的 `kl` 的 null/real ≥ 0.5，写"自适应的 KL 代价有一半以上与概念无关，来自度量本身"。

### 8.4 结论标签（每条结论只能用其一，并注明区域、概念、模型、指标）

| 标签 | 条件 |
|---|---|
| 已确立 | 区间下界 > 0，且在所有指定的独立单元里方向一致 |
| 方向一致但未确立 | 点估计同向，但区间跨 0 或只在部分单元一致 |
| 不能确立 | 区间跨 0 且方向不一致 |
| 实质等价 | 区间整体落在 ±0.05 内，逐种子判断（±0.05 为建议值，未经 Victor 确认，必须这样注明） |

### 8.5 必须出现在结论里的内容

1. 对 Q-A 的答案（K1、K2 的结论）。
2. 一张"指标面板"：C1、C2 在 `kl`、`kl_park`、`rd`、`cf_dev` 上各自的方向与是否显著，区域 A 与 C 各一张。
3. 对原问题的最终回答："固定度量捕获了多少，在哪里失效"，用 Q-B 的 ρ 与指标面板表述；**必须说明答案取决于指标。**
4. 局限（见第 10 节）。

---

## 9. 审查标准（你的交付将按此检查）

### 9.1 门槛

| 门槛 | 时点 | 提交内容 | 必须通过 |
|---|---|---|---|
| G6 | WP-0、WP-1 后 | 对等输出、回归结果 | WP-0 全部标准；WP-1 的 F7 |
| G7 | P0 完成后 | P0 的全部运行、`results_v5/p0`、`selfcheck` 输出、中期 `STATUS.md` | 自检无 FAIL；K1、K2 的结果已报告 |
| G8 | 最终 | 全部交付物 | 下面全部项 |

### 9.2 检查项

**A. 可复现性**
- [ ] 每个运行有完整 `config.json`、`checks.json`；`commands.log` 完整；`data_manifest.json` 含新数据哈希。
- [ ] 脚本相对提供版本的任何修改都在 `DEVIATIONS.md` 并附 diff。

**B. 对等与回归**
- [ ] WP-0、WP-1 通过。
- [ ] `selfcheck_v5.py` 对全部运行无 FAIL。

**C. 统计**
- [ ] 确认性比较仅 K1、K2；其余标"描述性"。
- [ ] 每条结论注明**独立单元数**与区域；α 敏感性单列。
- [ ] 区域 C 的聚类 ≥12（目标 ≥30 个文档）；报告 `n_clusters`。
- [ ] 所有已运行的 run 都出现在汇总里。
- [ ] 效应量给出原始值；多重比较"未校正"须明说。

**D. 指标政策**
- [ ] 任何"更好/更差"的表述并列写出四个指标的方向。
- [ ] 没有出现"`cf` 越高越好"。
- [ ] `kl_park` 注明"不是真正的 KL，可为负"。

**E. 数字一致性**
- [ ] `AGGREGATE_V5.md` 的数字全部由脚本生成；审查者将随机抽 10 个数字对照 CSV。
- [ ] `CONCLUSIONS_V5.md` 里每个数字都能在汇总或 CSV 中找到。

### 9.3 红线（出现即退回）

1. 数字与 CSV 不符，或手工抄写。
2. 遗漏已运行的 run，或只报告有利子集。
3. 修改算法未记录，或回归不通过仍继续。
4. 区间跨 0 却写"优于"。
5. 把 α 重复或固定方法的重复算作独立重复。
6. 使用"`cf` 越高越好"。
7. 把 `kl_park` 当作真正的 KL 或与我们的 KL 数值直接比较。
8. 结论只写在会被脚本重写的文件里。
9. 把不同探针家族的结果混成一个结论。
10. 对没有运行的内容给出结论。

---

## 10. 局限（必须原样写入结论的"局限"节，并按实际情况补充）

- 区域 C 只有 gemma-1b（以及 P1 的扩大版本），目标侧上下文少；探针的目标侧训练样本很少。
- 一个主要概念（verb→3rd person）与一个次要概念（verb→ing）；ing 的 `ctx`、`dmd` 探针有助动词句式混杂，只有 `unemb` 行可解读。
- `rd` 是简化版（只用起点的 top-0.99 集合）。
- 我们的 KL 用 1e-12 下限，Park 用 5e-3 偏移；`kl_park` 与其实现的一致性只在公式层面核对，没有用作者代码做数值对照。
- 步长 η = 0.01‖λ₀‖、停止在 P1 ≥ 0.99，与作者的绝对步长和 0.9999 停止规则不同。
- gemma-4b 为 4-bit。
- 零探针是"结构化零"（标签打乱、随机词对），不是各向同性随机向量；不同零探针的选择可能改变数值。
- 词频加权权重来自本次运行的上下文平均，不是语料的 unigram 频率。
- ±0.05 的等价边际为建议值，未经 Victor 确认。
- 多重比较未校正。
- 优势回归是相关性分析，预测变量之间相关，不支持因果解释。

---

## 11. 失败处理

| 情况 | 处理 |
|---|---|
| WP-0 对等失败 | 定位并写入 `DEVIATIONS.md`；若是 torch 新算子精度问题，改用 float64 并重测，不要放宽标准 |
| WP-1 回归失败 | 立刻停止；最常见原因是新增代码消耗了已有的随机数流；修复后重跑 |
| 显存不足 | 降低 `--topk`（不低于 5000）并记录；4B 不跑 `--with_freq` 的大批量 |
| C4 不可访问 | 改用其他自然文本语料（如 Wikipedia），写入 `DEVIATIONS.md`，结论标注"区域 C 使用的语料不是 C4" |
| 区域 C 目标上下文不足 | 增加文档数；仍不足则如实报告，不得放宽 Park 过滤 |
| 运行中途崩溃 | 删除该运行的输出目录后整批重跑；不要拼接不同批次的部分输出 |
| 发现自检 FAIL | 修复原因并重跑，不得删除自检输出 |
| 时间不足 | 只做 P0，其余在 `STATUS.md` 写"未运行"；不得为赶时间省略自检 |

---

## 12. 最终回复格式（你完成后的最后一条消息）

只包含：
1. 已完成与未完成的工作包列表（P0/P1/P2 各自状态）；
2. `selfcheck_v5.py` 的最终输出摘要（FAIL/WARN 数）；
3. K1、K2 的结果（每个种子的 `kl_park` 差与区间），一行一个；
4. 所有偏离（指向 `DEVIATIONS.md` 的条目号）；
5. 任何你无法解决或不确定的问题。

**不要**在这条消息里写任何未出现在 CSV 中的数字，也不要写"实验成功"之类的评价。
