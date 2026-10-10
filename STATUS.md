# STATUS（V5 最终版）— WP-7 整理后

- 生成：2026-10-11（WP-7 收尾整理员）；覆盖 P0 完成后的中期版（中期版"P1/P2 未运行"的表述在当时属实，已过时，见 `DEVIATIONS.md` V5.9）
- 仓库 HEAD（V5 全程执行基线，提交前记录）：`65d05830be19b7d7f0e944d5acd3823220138966`（V4 gates G4+G5）；V5 交付为在其后的一个提交 + 三个附注标签（`v5-g6`/`v5-g7`/`v5-final`，均指向该提交，见 `DEVIATIONS.md` V5.10）
- 依据任务书：`FINAL_EXPERIMENT_PROMPT_V5.md`；结论在 `CONCLUSIONS_V5.md`（经独立复核员逐数字核对），数据表在 `runs/AGGREGATE_V5.md`（脚本生成，27 run 全入表）
- 数字来源：逐表标注文件；§2 的自检为本轮（WP-7）**实际复跑**，命令与输出原样给出
- 全文提醒：`kl_park` 不是真正的 KL（带 5e-3 偏移，可为负），只作为 Park 度量的复现（任务书 §4、§8.1）

## 1. 工作包状态总览（最终）

| 工作包 | 状态 | 证据 |
|---|---|---|
| WP-0 环境与双后端对等（G6） | ✅ PASS（14 项标准全过） | `commands.log` WP-0 段 `WP0_PARITY: PASS`；汇总 §2b |
| WP-1 V4 回归（G6 硬门槛） | ✅ PASS（共有数值列 max abs diff = 0.0e+00） | 汇总 §2a；`DEVIATIONS.md` V5.2（首轮 reg_ 命名空过 + 修正） |
| 计时探测 | 已执行；输出目录按工作流脚本删除，数值未保留 | `DEVIATIONS.md` V5.5 |
| WP-2 **P0**（6 run） | ✅ 6/6 成功，失败 0 | §3 表；各 run `config.json`/`checks.json` |
| WP-2 **P1**（α=2e-2×6、GPT-2 区域 A×3、C4 大提取×3 + Cbig×3） | ✅ 12/12 成功，**失败 0 个 run** | §3 表；Cbig 目标侧 55/56、48/52、59/61（各 run `checks.json`），达到"≥40 条目标上下文"目标 |
| WP-2 **P2**（gemma-4b×1、ing×4） | ✅ 5/5 成功，**失败 0 个 run** | §3 表 |
| WP-3 分析 | ✅ 完成（`results_v5/p0` 早期版；`results_v5/full` 最终版 9 组） | `commands.log` WP-3 与 WP-5 段 |
| WP-4 自检（全量） | ✅ 0 FAIL / 31 WARN（本轮复跑，见 §2） | §2 |
| WP-5 汇总 | ✅ `runs/AGGREGATE_V5.md`（27 run、575 面板行、8 节齐全，22/22 抽查数通过） | `commands.log` WP-5 段 |
| WP-6 结论 | ✅ `CONCLUSIONS_V5.md`（K1/K2 均落入任务书 §8.2 第 1 行写法） | 该文件 §2 |
| WP-7 整理 | ✅ 本轮完成（本文件、`DEVIATIONS.md` V5 节、`commands.log` 补记、`data_manifest.json` +3 目录、`env.txt`、issue 草稿、提交+标签） | §6、`DEVIATIONS.md` V5 节 |

门槛：G6 通过（WP-0 + WP-1）；G7 通过（P0 全部 run + `results_v5/p0` + 自检无 FAIL + K1/K2 已报告，中期版即 G7 提交物）；G8 全部交付物齐备（本提交）。

## 2. 最终自检（WP-7 本轮实际复跑，只读）

命令（解释器 `/home/administrator/dev/ML/lrg_env/bin/python`）：

```
$ selfcheck_v5.py --runs "runs/*_v5/*"
  -> 25 runs checked, 0 FAIL, 31 WARN    （退出码 0）
```

31 条 WARN 全部为 F6（某方法 0.9 水平到达率 < 0.8），构成：

| 类别 | 条数 | 明细 |
|---|---|---|
| `frq_ctx` 到达率 0.00 | 23 | gemma-1b 全部 18 个带 `--with_freq` 的 run（A/C 各 6、Cbig 3、ing 3）+ gemma-4b 1 + GPT-2 4（A×3、ing×1）；与中期版 §6 第 1–6 条同一现象（600 步内 P1 几乎不上升，端点 NaN，不参与 0.9 水平配对），机制未分析 |
| GPT-2 `cau_ctx` 到达率 0.00 | 5 | `gpt2_v5/A_s{0,1,2}`、`gpt2_v5/ing_s0`、`gpt2_v5/s0_abs5e-3`（回归 run）；V4 同名 run 同为 0.0，V1–V4 既有属性，非 V5 新问题（中期版 §6 第 7 条） |
| GPT-2 `frq_unemb` 到达率 < 0.8 | 3 | `A_s0` 0.42、`A_s1` 0.65、`A_s2` 0.62（P1 新增 run；描述性记录，机制未分析） |

无 FAIL；两个 WP-1 回归 run（不带 `--with_freq`）无 frq 类 WARN，符合预期。

## 3. 运行清单（25 个真实模型 run；另 2 个 WP-0 合成 run，合计 27 全部入汇总 §1）

runtime_s 取自各 run `config.json`。区域 C 加 `--filter park --park_mass 0.7 --park_k 3`；除 WP-1 回归 run 与 α=2e-2 run 外均带 `--with_freq`；α=5e-3 的 run 另带 `--null_draws 3 --null_ctx 30`。

| 优先级 | run（`runs/` 下） | runtime_s |
|---|---|---|
| P0 | `gemma1b_v5/A_s{0,1,2}_abs5e-3` | 2652.6 / 1837.4 / 1809.0 |
| P0 | `gemma1b_v5/C_s{0,1,2}_abs5e-3` | 2980.6 / 2820.7 / 2890.0 |
| P1 | `gemma1b_v5/A_s{0,1,2}_abs2e-2` | 827.6 / 820.3 / 805.6 |
| P1 | `gemma1b_v5/C_s{0,1,2}_abs2e-2` | 1006.4 / 1003.3 / 1041.8 |
| P1 | `gpt2_v5/A_s{0,1,2}_abs5e-3` | 1253.8 / 1306.8 / 1256.0 |
| P1 | `gemma1b_v5/Cbig_s{0,1,2}_abs5e-3`（数据 `data/gemma1b_c4big_s{S}`，`--c4_docs 10000` 新提取） | 3034.8 / 2836.4 / 2789.7 |
| P2 | `gemma4b_v5/A_s0_abs5e-3` | 4079.3 |
| P2 | `gemma1b_v5/ing_s{0,1,2}_abs5e-3` | 2252.0 / 2358.1 / 2281.4 |
| P2 | `gpt2_v5/ing_s0_abs5e-3` | 1443.7 |
| WP-1 回归 | `gemma1b_v5/s0_abs5e-3`、`gpt2_v5/s0_abs5e-3`（与 V4 同参数，无 with_freq/null） | 772.0 / 397.4 |

**失败 run 清单：空**（P0 6/6、P1 12/12、P2 5/5）。门禁层面的两次"失败→修正→重跑"事件（非 run 失败）见 `DEVIATIONS.md` V5.2（WP-1 reg_ 命名）与 V5.4(b)（`results_v5/full` 在最后 5 个 P2 run 之前生成，WP-5 以同序 6 组 + 追加 3 组重跑，RNG 前缀逐行一致）。

GPT-2 的 P1/P2 run 用 `--topk 20000`（任务书 §5 统一参数），与 V4 的 GPT-2 惯例 `--topk 5000` 不同，回归 run 仍为 5000——配置差异记录于 `DEVIATIONS.md` V5.6。

## 4. K1/K2 最终结果（确认性比较；metric=`kl_park`，区域 C，gemma-1b，third，α=5e-3，每种子 n=60）

来源：`results_v5/full/metric_panel.csv`（本轮逐行核对）。`kl_park` 不是真正的 KL（可为负）。diff = a − b，> 0 即 `dua` 更好。

| 比较 | 种子 | diff（kl_park） | 95% 区间 | 来源 |
|---|---|---|---|---|
| K1 `euc_dmd − dua_dmd` | s0 | +0.64183 | [0.47437, 0.80292] | `metric_panel.csv` 行 77 |
| K1 | s1 | +0.72134 | [0.54881, 0.90244] | 行 82 |
| K1 | s2 | +0.87684 | [0.69456, 1.07415] | 行 87 |
| K2 `cau_unemb − dua_unemb` | s0 | +0.14836 | [0.07745, 0.22895] | 行 92 |
| K2 | s1 | +0.13129 | [0.05863, 0.20703] | 行 97 |
| K2 | s2 | +0.29078 | [0.18734, 0.40834] | 行 102 |

判定（任务书 §8.2）：K1、K2 均 3 种子区间下界 > 0 且无种子显著反向 → 第 1 行写法（"在 Park 的 KL 下，区域 C 的反向消失……我们的 KL 下的反向是度量造成的"）。四指标并列方向与其余结论见 `CONCLUSIONS_V5.md` §2–§3（`kl`/`kl_neu` 上 `dua` 更差、`kl_park`/`rd`/`cf_dev` 上更好——"是否更好"取决于指标）。

## 5. 成本（计时）

以各 run `config.json` `runtime_s` 为准（§3 表；计时探测输出已删、数值不引用，`DEVIATIONS.md` V5.5）。组内一致性良好，唯一异常：`A_s0_abs5e-3` 2652.6 s 高于同组 1837.4/1809.0 s 约 44%（首个 P0 run；中期版 §5 已如实记录"未查原因"，本轮维持该记录，未做归因推断）。

## 6. WP-7 交付物清单

| 项 | 状态 | 位置 |
|---|---|---|
| `DEVIATIONS.md` V5 节 | ✅ 11 条（含 GPU 独占检查方式、失败重跑、计时异常、P1/P2 失败清单=空、修复员无改码的验证方式与限度） | `DEVIATIONS.md` ## V5 |
| `commands.log` 补记 | ✅ P1/P2 实际命令行（逐字取自各 run `config.json` args，注明补记性质）+ `git rev-parse HEAD` 输出 + WP-7 本轮命令 | `commands.log` 末两段 |
| `data_manifest.json` | ✅ 追加 `gemma1b_c4big_s{0,1,2}`（sha256/shape/dtype/meta/corpus；`docs_scanned: 10001` 为推导值，`DEVIATIONS.md` V5.7）；对旧条目纯追加、零改动（git diff 147 insertions, 0 deletions） | `data_manifest.json` |
| `env.txt` | ✅ 重生成 pip freeze + 版本块；较旧版新增 `datasets==5.1.0` 及其 11 个依赖（V4 装 `datasets` 做 C4 流式提取后一直未更新，本轮补上）；python 3.12.3 / torch 2.6.0+cu124 / transformers 5.19.0 / numpy 2.5.3 不变 | `env.txt` |
| issue 草稿 | ✅ 已起草、未提交（"not sent" 状态不变） | `repro_check.md` V5 WP-7 addendum |
| git 提交与标签 | ✅ 一个提交（V5 全部交付）+ 附注标签 `v5-g6`/`v5-g7`/`v5-final`（均指向该提交，`DEVIATIONS.md` V5.10）；未 push | `git log`/`git tag` |
| 本文件（最终版） | ✅ 覆盖中期版 | `STATUS.md` |

## 7. 未检验（任务书 §1 规则 7：不得推断或估计）

- `frq_ctx` 在全部 gemma-1b run 与 gemma-4b、GPT-2 run 的 0.9 水平到达率 0.00 的机制（端点 NaN，不参与配对；`CONCLUSIONS_V5.md` §8.12）。
- GPT-2 `cau_ctx` 到达率 0.00 的机制（V1–V4 既有属性）。
- GPT-2 / gemma-4b 的区域 C：从未运行。
- `kl_park` 与作者代码的数值对照：仅公式层核对（任务书 §10 局限 4）。
- ±0.05 等价边际未经 Victor 确认（任务书 §10 局限 9）。
- 多重比较未校正（任务书 §10 局限 10）。
