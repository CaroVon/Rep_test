# 实验问题诊断与修改说明

适用对象：仓库 `CaroVon/Rep_test`，`runs/AGGREGATE.md` 中的实验（Euclidean vs fixed causal metric vs adaptive dual steering，GPT-2 / Gemma-3-1B / Gemma-3-4B 4-bit，RTX 4060 8GB）。

配套文件：`steer_compare_v2.py`（本文所有"代码修改"已实现在这个文件里，在你仓库当前的 `steer_compare.py` 基础上打补丁而成）。

---

## 0. 一页摘要

**我核实了什么。** 我把 `AGGREGATE.md` 里的数字与每个 run 的 `summary.csv`、`checks.json`、`paired.csv` 逐项核对过，数字一致。你仓库的脚本与我最初给的相比，只多了输出路径清洗（`safe_run_dir`），算法没有改动。所以**执行没有问题，问题在实验设计与结论表述**。

**核心判断。** 目前的结果可以支持"在本配置下，欧氏方向最稳、最省 KL"，**不能支持**"causal-metric / dual steering 没有优势"，也不能支持"未能复现 Park 2026"。原因是下表中的前三项：它们让这次实验没有真正检验到 Park 的方法。

| # | 问题 | 严重程度 | 谁的责任 | 修改位置 |
|---|---|---|---|---|
| P1 | $\alpha$ 的量级比 Park 小几个数量级，且按错误的尺度标定 | **高** | 原方案设计 | §2.1 |
| P2 | `causal_fixed` 不是 Park 2024 的方法 | **高** | 原方案设计 | §2.2 |
| P3 | 上下文设置与 Park 不同（集中度、过滤条件） | 中高 | 原方案设计 | §2.3 |
| P4 | 模板上下文成簇，置信区间过窄 | 中 | 原方案设计 | §2.4 |
| P5 | dual 到达率为 0 时，不知道"卡在哪" | 中 | 原方案设计 | §2.5 |
| P6 | AGGREGATE 的措辞与列名有误导 | 中 | 汇总阶段 | §2.6 |
| P7 | 运行预算、量化与完整性问题 | 低中 | 综合 | §2.7 |
| P8 | 没有与作者实现逐步对照 | 中 | 尚未做 | §2.8 |

"原方案设计"指我在前几轮给出的方案与脚本里的设计缺陷，不是你的执行错误。

---

## 1. 现在能说什么、不能说什么

**可以说（有数据支持）：**
- 流程在三个模型上跑通，护栏检查通过（日志检验误差 ≤3.5e-3，探针留出 AUC 0.93–1.00）。
- 在本配置下，`euclid` 对所有 $\alpha$、所有模型的到达率都是 1.0，且 off-target KL 最低。
- `causal_fixed`（定义见 P2）在 Gemma 上能到达，但比欧氏慢 2–4 倍（到达 0.9 的平均步数：gemma-1b 约 70 vs 38；gemma-4b 约 180 vs 49），KL 更高。
- 在 GPT-2 上，$\alpha_{rel}\le10^{-2}$ 时 `causal_fixed` 一个上下文都到不了，原因是 $S_0$ 近乎奇异（你们诊断出最小特征值约 1.65e-7）。
- 在 $\alpha$ 取你们扫描的范围内，`dual` 在 Gemma 上到达率为 0。

**不能说：**
- "Park 2026 的对偶 steering 没有优势" 或 "无法复现"。
- "Park 2024 的因果度量 steering 不如欧氏"。
- "失败是几何性质而非实现问题"（合成数据通过只能排除部分 bug，排除不了超参与设置差异）。

---

## 2. 问题详解与修改

### 2.1 P1：$\alpha$ 的量级与标定对象

**证据。** 我从各 run 的 `checks.json` 读出绝对 $\alpha$：

| 模型 | 你的 $\alpha$ | $\mathrm{tr}(S_0)/d$ | 相对 Park 的 $5\times10^{-3}$ |
|---|---|---|---|
| gemma-3-1b | 8.9e-7 ～ 8.9e-5 | 8.9e-4 | 约 1.8e-4 ～ 1.8e-2 倍 |
| gemma-3-4b | 3.6e-7、3.6e-6（已完成两个） | 3.6e-4 | 约 7e-5、7e-4 倍 |

Park 2026 附录 B.2 写明 LLM 与 CLIP 都用 $\alpha=5\times10^{-3}$。对 Gemma-3-4B，这相当于 `alpha_rel` 约 14，而你们的扫描最大只到 0.1。**注意：** 这个换算只在两者使用同类 checkpoint、同样的 unembedding 尺度时成立（论文没说是 pt 还是 it），所以请把它当作量级警告，而不是精确对应。

**为什么 $\alpha$ 太小会让 dual 失败。** 更新方向是 $v=(\Sigma_t+\alpha I)^{-1}\beta$。当上下文预测很集中时，$\Sigma_t$ 的大部分特征值接近 0。若 $\alpha$ 远小于这些特征值，$\beta$ 在近零特征方向上的分量被放大约 $1/\alpha$，方向被它们主导。这些方向主要改变罕见 token 的 logit，所以每一步走了，目标概率却几乎不变，分布熵上升。你们在 gemma-1b 上"cos 0.86 与欧氏接近，但 P1 只从 0.0097 升到 0.02"的观察与此一致。

**标定对象有误。** 我把 $\alpha$ 定义为相对 $\mathrm{tr}(S_0)/d$。但 $\Sigma_t$ 是 softmax 加权协方差，其尺度与均匀协方差 $S_0$ 没有固定关系。应当用 $\Sigma_t$ 起点处的谱来决定 $\alpha$ 的量级。

**修改（已在 `steer_compare_v2.py` 实现）：**

1. 新增 `--alpha_abs`，直接指定绝对 $\alpha$（优先于 `--alpha_rel`）。
2. 起点处的 $\Sigma_t$ 谱诊断：对前 5 个起始上下文计算 $\Sigma_t$ 的特征值，写入 `checks.json` 的 `sigma_t_diag`（`trace_mean`、`eig_max_mean`、`eig_p1/p10/p50_mean`、`frac_eig_above_alpha`），并在终端打印。
3. 判读：`frac_eig_above_alpha` 接近 0 说明 $\alpha$ 过大（dual 退化为欧氏）；若很大且 `eig_p50_mean` 远小于 $\alpha$ 以外的尺度，说明 $\alpha$ 偏小，近零方向被放大。

**要跑的扫描（gemma-3-1b，只跑必要方法、少量上下文）：**

```bash
for A in 1e-4 1e-3 5e-3 2e-2 1e-1; do
  python steer_compare_v2.py --data_dir data/gemma1b --backend torch --topk 20000 \
    --methods euclid,euclid_unemb,causal_unemb,dual \
    --alpha_abs $A --n_ctx 20 --seed 0 --out runs/gemma1b_v2/abs${A}
done
```

按你们 80 条上下文、三种方法约 30 分钟的运行时间估算，这个扫描主要耗时在 dual，约 30–40 分钟；请先用 `--n_ctx 5` 估时间。

**验收标准：** `final.csv` 与 `checks.json` 显示，在某个 $\alpha$ 区间 dual 的到达率明显大于 0。若在 $5\times10^{-3}$ 附近仍为 0，进入 §2.8 的逐步对照。

---

### 2.2 P2：`causal_fixed` 不是 Park 2024 的方法

**问题。** Park 2024 的干预向量是

$$\bar\lambda_W=\mathrm{Cov}(\gamma)^{-1}\bar\gamma_W,$$

其中 $\bar\gamma_W$ 由**词对的 unembedding 差**估计，即 $\overline{G[y^1]-G[y^0]}$。而原方案里的 `causal_fixed` 是

$$v=(S_0+\alpha I)^{-1}\beta,$$

$\beta$ 是**上下文嵌入的均值差**。这实际检验的是"把对偶 steering 的 Hessian 冻结在均匀分布，作用于上下文探针"，这是我提出的变体，不是 Park 2024 的原法。因此"causal-metric steering 输给欧氏"的说法目前没有依据。

**修改（已实现）：** 新增两个方法。

| 方法 | 方向 | 说明 |
|---|---|---|
| `euclid_unemb` | $\bar\gamma_W$ | unembedding 差的欧氏方向 |
| `causal_unemb` | $(S_0+\epsilon I)^{-1}\bar\gamma_W$ | Park 2024 原法；$\epsilon=$ `--ridge_rel` × $\mathrm{tr}(S_0)/d$，默认 1e-6，仅用于数值稳定 |

`--methods` 可选择运行哪些方法（默认五种全跑）。启动时会打印 `cos(beta, gbar)`（上下文探针与 unembedding 方向的一致程度）与 `cos(euclid_unemb, causal_unemb)`。

**解读提示：** 沿 $\bar\gamma_W$ 前进时，每个反事实对的 logit 差 $\lambda\cdot(\gamma(y^1_i)-\gamma(y^0_i))$ 会增加，所以 `euclid_unemb` 本身就是一个强基线。`causal_unemb` 要比较的是它能否进一步减少对非目标 token 的影响。请同时报告 `cos(beta, gbar)`，若很低，说明两种探针差异大，比较时要分开讨论。

**$\epsilon$ 的敏感性：** GPT-2 的 $S_0$ 近奇异（最小特征值约 1.65e-7），请在 `--ridge_rel` 取 1e-8、1e-6、1e-4 三个值各跑一次，确认结论不依赖它。

---

### 2.3 P3：上下文设置与 Park 不同

**差异。**

| | Park 2026 | 你们 |
|---|---|---|
| 来源 | C4 自然文本 | 手写模板（8 个主语 × 11 个副词 × 4 种前缀） |
| 过滤 | 前 3 个预测 token 都属于该概念组，且累计概率至少 0.7 | `cf mass ≥ 0.15`，且基线组 `P1 < 0.3` |
| 起点分布 | 集中在少数反事实 token 上 | 起始反事实质量从约 0.09 到 0.77 不等，更分散 |

起点分布的集中度会直接改变 $\Sigma_t$ 的秩和谱，从而影响 dual 的行为，也会改变 off-target KL 的数值。

**修改：**

1. 先不改数据，只收紧过滤：`--min_mass 0.5`（再试 0.7），并在 `checks.json` 里核对保留数量（`n_base_kept`）。若保留不足 20 条，说明模板太分散。
2. 增加模板多样性，**但保持两组的结构对称**：两组使用相同的句式框架，只让主语数不同。**不要**只给基线组换成"I don't want to"这类自然句式，否则探针会学到句式差异而不是动词形态（混杂）。
3. 在 `extract_embeddings.py` 的 `make_contexts` 里扩大列表（保持首字母大写的约定，`subject_of` 依赖它）：

```python
prefixes = ["", "Every day, ", "At work, ", "Honestly, ", "Today, ", "In this case, ",
            "Lately, ", "At home, ", "Over time, ", "Usually, "]
adv = ["usually","often","always","never","sometimes","rarely","really","also","just",
       "still","typically","generally","now",""]
base_s = ["I","You","We","They","People","Students","Many people","The workers",
          "Our customers","These kids","Most doctors","The engineers","Both of them",
          "Parents","Farmers","Voters"]
targ_s = ["He","She","It","The man","My sister","The teacher","This company","My brother",
          "Our customer","That kid","The doctor","The engineer","Her mother",
          "The farmer","The voter","Everyone"]
```

这些主语已加入 `steer_compare_v2.py` 的 `_SUBJ` 列表，用于聚类自助法。若你再加新主语，请同步加进去，否则它们会被归为 `"?"` 一类。

4. 修改后需要**重新运行 `extract_embeddings.py`**，因为 `E_base.npy`、`E_target.npy` 都要重算。

---

### 2.4 P4：上下文成簇，置信区间过窄

**证据。** 我对 gemma-1b、`alpha0.01` 的 80 条上下文按主语分组，euclid 在水平 0.9 的 off-target KL 为：

| 主语 | 条数 | KL 均值 |
|---|---|---|
| I | 10 | 2.23 |
| We | 8 | 1.28 |
| They | 12 | 1.10 |
| Many people | 13 | 1.09 |
| You | 10 | 1.00 |
| Students | 9 | 0.86 |
| The workers | 10 | 0.79 |
| People | 8 | 0.72 |

主语 "I" 的 KL 是 "People" 的 3 倍以上。同一主语下的上下文非常相似，彼此不独立。把 80 条当独立样本做自助法，会严重低估不确定性。

**修改（已实现）：** 新增聚类自助法，按主语重采样整簇。

- 默认开启（`--no_cluster_boot` 可关闭）。启动时会打印 `[ci] cluster bootstrap over N subjects`，`checks.json` 里 `ci_type` 为 `cluster` 或 `plain`。
- 若主语簇少于 3，自动退回普通自助法。
- **局限：** 只有 8 个主语时，聚类自助法的区间本身也很粗。扩展到 16 个主语（§2.3）后会更可靠。表述时请说明"区间按主语聚类计算，簇数为 N"。

---

### 2.5 P5：dual 到达率为 0 时缺少诊断

**问题。** 到达率为 0 只告诉你"没到"，不告诉你是"完全卡住"还是"只是太慢"，也不知道分布的熵发生了什么。

**修改（已实现）：** 每次运行新增 `final.csv`：

`ctx_id, method, step_end, P1_end, cf_end, kl_end, H_start, H_end`

- `H_start`、`H_end` 是起点与终点的分布熵。
- 判读：若 dual 的 `H_end` 远大于 `H_start` 且 `P1_end` 很低，对应 §2.1 的"熵上升、目标不动"；若 `P1_end` 缓慢上升，可以尝试提高 `--max_steps` 或 `--step_frac`。

---

### 2.6 P6：AGGREGATE.md 的措辞与列名

| 原文 | 问题 | 建议 |
|---|---|---|
| "Euclidean steering dominates everywhere in this pipeline" | 缺少适用范围 | 见下方替换文本 |
| 表中 "P=0.012" | 这是 `win_b_lower_kl` 列，即 causal_fixed 的 KL 更低的**上下文比例**，不是 p 值 | v2 已把列名改为 `frac_ctx_b_lower_kl`；汇总里写"胜率" |
| "mechanism diagnosed" | 只在一个 CPU 上下文上诊断过 | 标为"初步假设，待多上下文验证" |
| "confirming the real-model failures are geometric, not bugs" | 过度推断 | 删除 |
| gemma4b 的几行写"见 run" | 数据已有，可补全 | 补入下表 |
| "This does NOT reproduce an advantage…" | 见 §1 | 见下方替换文本 |

**gemma-4b 可直接补入的数据（水平 0.9）：**

| $\alpha_{rel}$ | euclid KL | causal_fixed KL | dual 到达率 |
|---|---|---|---|
| 1e-3 | 0.995 | 3.927 | 0 |
| 1e-2 | 0.995 | 3.820 | 0 |
| 1e-1 | 仓库中尚无 | | |

**建议替换 "Findings" 第 1、3、5 条的文本：**

> 1. 在本配置下（模板上下文、`alpha_rel ∈ [1e-3, 1e-1]`、上下文均值差探针），欧氏方向对所有模型的到达率为 1.0，且 off-target KL 最低。
> 3. 在同一配置下，自适应 dual 方向在 Gemma 上未能到达任何水平。我们的绝对 α（约 1e-7 ～ 1e-4）比 Park 2026 报告的 5e-3 小 2–4 个数量级，因此这一结果不构成对其方法的检验。机制假设（近零特征方向被放大、熵上升）尚待多上下文验证。
> 5. 本次实验没有测试 Park 2024 的原法（作用于 unembedding 差的 Cov⁻¹），也没有对齐 Park 2026 的 α 与上下文过滤。因此不能就两种方法的优劣下结论。

---

### 2.7 P7：运行预算、量化与完整性

1. **步长与步数。** `step_frac=0.01`、`max_steps=600` 是我随手设的。Park 的 η 与停止条件（目标概率到 0.9999）也不一定与此对应。请至少在一个 $\alpha$ 上做一次 `--step_frac 0.02 --max_steps 1200` 的对照，看 dual 的到达率是否变化。
2. **gemma-4b 的运行不完整。** 仓库里只有两个 $\alpha$，且每个约 1 小时。优先级低于 §2.1 的 gemma-1b 扫描。
3. **4-bit 量化。** 隐状态与 bf16 略有差异。分析基于保存的 $\lambda$ 与 $G$，内部自洽；但与 Park 的对照不是严格同一模型，请在所有汇报里注明。
4. **`n_ctx` 与 `min_mass`。** 修改过滤后，`n_base_kept` 变化会影响可用上下文数，请检查 `checks.json`。

---

### 2.8 P8：与作者实现逐步对照（判断"是实现问题还是现象"的唯一直接办法）

**做法：** 在同一个上下文 $\lambda_0$、同一个探针 $\beta$、同一个 $\alpha$、同一个 top-K 下，分别用你们的 `dual_dir` 与作者仓库 `KihoPark/dual-steering` 里的实现，各算第一步的方向 $v_0$，比较余弦；再各走 20 步，比较 P1 与熵的轨迹。

- 若方向余弦接近 1、轨迹一致：实现没问题，差异来自 $\alpha$、$\eta$ 或上下文，回到 §2.1、§2.3。
- 若方向不同：定位差异（归一化、top-K 取法、CG 的容差等）。

**我的限制：** 我没有读过该仓库的代码，不能替你判断它的接口，需要你把相关函数贴给我，或自己做这一步。

---

## 3. 修改清单（`steer_compare_v2.py` 相对你当前版本）

| 修改 | 位置 | 说明 |
|---|---|---|
| `--alpha_abs` | 参数、`main` | 绝对 $\alpha$ |
| `--ridge_rel` | 参数、`main` | `causal_unemb` 的岭系数 |
| `--methods` | 参数、`main` | 选择运行的方法，默认五种 |
| `euclid_unemb`、`causal_unemb` | `main` | Park 2024 原法 |
| `pair_diff_mean`、`entropy`、`sigma_spec` | 两个后端 | 新增算子 |
| $\Sigma_t$ 谱诊断 | `main`、`checks.json` | `sigma_t_diag` |
| 聚类自助法 | `cluster_boot_ci`、`subject_of` | 默认开启 |
| `final.csv` | 输出 | 每个上下文的终点状态与熵 |
| `frac_ctx_b_lower_kl` | `paired.csv` | 原 `win_b_lower_kl` 重命名 |
| 比较对 | `paired.csv` | 新增含 unemb 方法的比较 |

**测试状态：**
- numpy 后端：已在合成数据上做完整端到端测试，`--selftest` 通过。
- **torch 后端的三个新算子（`pair_diff_mean`、`entropy`、`sigma_spec`）没有测试过**，我的沙箱装不上 torch。请先运行：

```bash
python steer_compare_v2.py --selftest
python steer_compare_v2.py --synthetic --backend numpy --n_ctx 10 --max_steps 100 --topk 1500 --out runs/syn_np
python steer_compare_v2.py --synthetic --backend torch --n_ctx 10 --max_steps 100 --topk 1500 --out runs/syn_torch
```

然后比较 `runs/syn_np/summary.csv` 与 `runs/syn_torch/summary.csv`，两者应当数值相近。若 torch 版本报错，把报错贴给我。

---

## 4. 建议的执行顺序与决策

| 步骤 | 内容 | 预计成本 | 判断 |
|---|---|---|---|
| 1 | 跑三条合成数据的检验（上面三条命令） | 几分钟 | 确认 v2 在你的环境里正常 |
| 2 | gemma-1b 的绝对 $\alpha$ 扫描（§2.1），只跑 `euclid,euclid_unemb,causal_unemb,dual`，`--n_ctx 20` | 约 30–40 分钟 | 看 dual 在哪个 $\alpha$ 开始到达 |
| 3 | 看 `checks.json` 的 `sigma_t_diag` 与 `final.csv` | 几分钟 | 判断 $\alpha$ 与 $\Sigma_t$ 的相对尺度 |
| 4 | 若 dual 仍不到达：做 §2.8 的逐步对照 | 视情况 | 区分实现与现象 |
| 5 | 扩大主语列表、收紧过滤（§2.3），重新提取 | 取决于模型 | 更接近 Park 的上下文 |
| 6 | 对 `ridge_rel` 做敏感性（§2.2） | 几分钟 | 确认 `causal_unemb` 的结论稳健 |

**决策：**
- **dual 在合理 $\alpha$ 下开始到达，并显示 KL 优势：** 研究问题变成"固定度量能捕获多少"，按原计划推进，并加上 `euclid_unemb` 与 `causal_unemb` 的比较。
- **dual 仍不到达，且与作者实现的逐步对照一致：** 写成一份关于 $\alpha$ 敏感性的复现报告，并把差异点明确告诉作者。
- **逐步对照发现实现差异：** 修正后重跑，原有结论作废。

---

## 5. 给 Victor 的汇报框架（更新版）

1. **做了什么：** 三个模型上的三方向比较流程，护栏通过。
2. **看到什么：** 欧氏最稳；固定度量慢 2–4 倍；dual 在我们的 $\alpha$ 范围（比 5e-3 小 2–4 个数量级）下到不了。
3. **哪里没有测：** Park 2024 原法（作用于 unembedding 差）；与 Park 2026 对齐的 $\alpha$ 与上下文过滤。
4. **想请教：**
   - $\alpha=5\times10^{-3}$ 是绝对值吗？步长、最大步数、top-K 分别是多少？
   - 你们的上下文过滤是前 3 个 token 在组内且累计至少 0.7 吗？
   - 你们的 dual 在 4B 上是否稳定到达 0.9999？有没有观察到前几步熵上升的阶段？
   - 你们是否把 $\mathrm{Cov}(\gamma)^{-1}\bar\gamma$ 当作过基线？

---

## 6. 已知的不确定性

- $\alpha$ 的"相当于 alpha_rel 约 14"只是量级换算，依赖于 checkpoint 与尺度是否一致。
- "近零特征方向被放大"是机制假设，`sigma_t_diag` 与 `final.csv` 可以给出支持或反驳，但不是证明。
- 聚类自助法在簇数很少时区间本身不稳。
- 我没有读 Park 2026 作者仓库的代码，对其默认参数不做断言。
