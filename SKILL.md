---
name: fundamental-edge
description: "Fundamental Edge 买方基本面研究方法论（Brett Caughran 买方培训体系，15 模块）。用于按机构买方标准对个股做完整研究：生意本质 → 护城河/ROIC → 3 个关键驱动 → 财务模型 → 预期差与估值（DCF/倍数）→ 牛熊情景与风险回报 → 催化剂 → 论点与路演。触发词：买方研究、基本面分析、深度研究、投研流程、建模型、DCF、估值分析、预期差、reverse DCF、ROIC、牛熊情景、风险回报、论点、pitch、research process、fundamental analysis、buy-side、stock pitch、帮我把这只股票研究透、建个模型、算下预期差、值不值得买、目标价、安全边际、护城河打分、资本回报。本 skill 提供方法论骨架 + 可执行计算脚本（DCF / Reverse DCF / ROIC / 风险回报）+ 可复用 Excel 模型模板。不负责撰写最终成稿投研报告（那由 equity-research 负责），不负责数据抓取（走 Bloomberg MCP / financial-data）。"
agent_created: true
---

# Fundamental Edge —— 买方基本面研究方法论

> 来源：**Fundamental Edge** 买方培训课件（15 个模块 + 延伸阅读 + Excel 模型模板，作者 Brett Caughran，Scottsdale AZ）。
> 本仓库是方法论的结构化整理，不包含课件原始文件，也不复制原文整章。版权归原作者，仅供个人研究学习。

## 一句话立场

**价格是一份 FCF 预测（Price is a FCF forecast）。基本面研究不是找真相，是找预期差。**

市场在大多数时候是对的 `[M1 p.57]`。可重复的 alpha 来自三件事：
**扎实的底层技能 → 可重复的严谨流程 → 靠实战磨出的判断力** `[M1 p.95]`。

---

## 1. 主干流程（必须按序走）

### 1.1 六步投资流程 `[M1 p.97]`

| # | 步骤 | 交付物 |
|---|---|---|
| 1 | **机会评估**（这个标的有意思吗？） | 判断市场已price in什么；alpha load（价格 vs 价值缺口）有多大 |
| 2 | **生意分析与建模** | 自建财务模型：生意如何运转 → 用来给股票估值、判断 business momentum 与潜在盈利修正 |
| 3 | **关键驱动评估与深挖** | 锁定 **3 个关键驱动**，深挖差异化认识 |
| 4 | **情景构建与风险回报评估** | 搞清股价里已含什么 → 自建 bull/base/bear → 风险回报够不够 |
| 5 | **论点构建与表达** | 定性 + 定量 → 结构化论点 → pitch 给 PM/LP |
| 6 | **想法跟踪与催化剂评估** | 制定催化剂与财报跟踪计划 → 监控新闻流 → 判断论点是否 still on track |

**跳步 = 犯错。** 尤其不能在建模型前就验证结论，也不能在没算清风险回报前讲观点。

### 1.2 论点链条 ETIK → KD → VB → EP `[M1 p.59]`

```
ETIK (Everything There Is To Know)  全知：把公司彻底研究透
   ↓  关键转折：只保留能驱动价值的部分
KD (Key Drivers)                     3 个关键驱动：收入 / 利润率 / 资本强度（Focus Five 取其三）
   ↓  把驱动转成对公平价值的判断
VB (Value Belief)                    价值信念：这只股票贵还是便宜（公允值 = 每股价值）
   ↓  决定怎么下手
EP (Entry Point)                     入场点：价格 + 催化剂 + 交易计划
```

- ETIK → KD 的深挖流程见 `references/02-thesis-development.md`
- **HHT**：Hunch（直觉）→ Hypothesis（假设）→ Thesis（论点）`[M5]`
- **Gauntlet of Disqualifiers**：先列"一票否决项"，避免用长仓逻辑套短仓逻辑 `[M3]`

### 1.3 PM 的三个问题 `[M3 p.95]`

任何论点最后必须能回答：

1. **"Get me up to speed"** —— 让我 3 分钟搞懂这门生意
2. **"Where are we different & why"** —— 我们和市场的分歧在哪，为什么我们是对的
3. **"What is our path to getting paid"** —— 靠什么兑现，路径是什么

答不上第 2、3 问的，不是论点，是故事。

---

## 2. 执行清单（AI 执行时按此顺序调用）

```
① 生意本质      → 05-business-analysis.md      生意怎么赚钱、单位经济、护城河、ROIC
② 行业          → 06-industry-and-management.md 行业结构、周期位置、竞争格局
③ 关键驱动      → 03-stock-drivers-and-ideas.md Focus Five、3 个关键驱动
④ 建模          → 04-modeling.md                9 大预测框架、Excel 模板、Forecast Metrics
⑤ 预期差        → 07-expectations.md            reverse DCF、市场隐含假设
⑥ 估值          → 08-valuation.md               DCF / 倍数 / WACC / 常见错误
⑦ 情景与回报    → 11-portfolio-and-risk.md      bull/base/bear、PSUC、R/R、仓位
⑧ 管理层        → 06-industry-and-management.md 资本配置记录、回购/分红/并购纪律
⑨ 论点与路演    → 10-earnings-and-pitch.md      9 步论点流程、pitch 结构、bear case
⑩ 跟踪          → 10-earnings-and-pitch.md      催化剂日历、修正监控、thesis drift
```

**贯穿全程的三条纪律**

1. **先写市场观点，再写自己的观点**（`07-expectations.md`）。顺序反了会被锚定。
2. **风险先于回报**："Take care of the risk case and the reward will take care of itself" `[M3 p.103]`。
3. **TV 占比 < 25% NPV** `[M3 p.66]`。终值权重过高 = 结论是假设的函数。

---

## 3. 计算脚本（用，不要手搓）

全部位于 `scripts/`，纯标准库 + 无依赖，`python <abs path>/<script>.py --help`。
输出默认 **Markdown + TSV 双格式**（`--format md|tsv|both`）。

### 3.1 `dcf.py` —— DCF 估值 + 资本成本 + 敏感性

```bash
PY="C:/Users/ey/AppData/Local/Programs/Python/Python312/python.exe"

# 用 Rf/Beta/ERP/Kd/税率/权重 搭 WACC，再跑 DCF
$PY scripts/dcf.py --csv fcff.csv --build-wacc --rf 0.045 --beta 1.0 --erp 0.05 \
    --kd 0.06 --tax-rate 0.25 --equity-weight 0.70 --debt-weight 0.30 \
    --terminal-growth 0.025 --net-debt 500 --shares 100 --eps 1.85 --price 18 --sensitivity

# 直接给 WACC，用退出倍数做终值
$PY scripts/dcf.py --csv fcff.csv --wacc 0.08 --exit-multiple 10 --net-debt 500 --shares 100
```

自动输出：EV 桥、每股价值、**终值占 NPV 比重（超标告警）**、隐含终值倍数、隐含 P/E、
WACC × g 敏感性矩阵、**锚点校验**（对照 `[M1 p.10]` 的 WACC→隐含 P/E 表）。

### 3.2 `reverse_dcf.py` —— 市场隐含假设 + 预期差

```bash
# 反推市场隐含的 g / WACC / 终值倍数，并与内部价值比出预期差
$PY scripts/reverse_dcf.py --csv fcff.csv --price 18.37 --shares 100 --net-debt 500 \
    --solve all --wacc 0.08 --terminal-growth 0.025 --internal-value 25

# 反推市场隐含的稳态经营利润率（给收入路径 + 目标 P/E）
$PY scripts/reverse_dcf.py --csv revenue.csv --series-type revenue \
    --price 100 --shares 100 --target-pe 20 --solve margin
```

### 3.3 `roic.py` —— ROIC、价值创造、再投资敏感性

```bash
$PY scripts/roic.py --ebit 500 --tax-rate 0.25 --nwc 100 --net-fixed-assets 800 \
    --wacc 0.08 --delta-nopat 60 --delta-ic 200 --growth 0.10 --reinvestment-sensitivity
```

输出 ROIC / 有形 ROIC / **ROIC−WACC 利差（bps）**、价值创造额、增量 ROIC、
隐含再投资率、再投资率敏感性（可复现课件 `[M4 p.81]` 表：$10 → $17.28 / $13.31 / $11.58）。

### 3.4 `riskreward.py` —— 风险回报、PSUC、回报阶梯、仓位、组合敞口

```bash
$PY scripts/riskreward.py --price 100 --target 140 --stop 85 \
    --ntm2-eps 8.5 --ntm2-pe 22 --ntm-eps 4.2 \
    --scenario "bull:150:0.3,base:110:0.5,bear:70:0.2" \
    --portfolio-value 1000000 --risk-pct 0.01 --entry 100 --stop 85 \
    --positions "AAPL:0.05,MSFT:0.04,TSLA:-0.02"
```

输出：R/R、**PSUC**、12 个月目标价 = NTM2 EPS × NTM2 P/E、情景概率加权、
按止损定仓（**份数 + 金额 + 权重**）、组合 gross/net 敞口。

### 3.5 `extract_course_pdf.py` —— 回查课件原文

```bash
export FUNDAMENTAL_EDGE_ROOT="/path/to/course library"    # 或每次传 --root

$PY scripts/extract_course_pdf.py --list                       # 列出全部 PDF（自动跳过重复件）
$PY scripts/extract_course_pdf.py --module "Module 11" --out-dir ./course_text
$PY scripts/extract_course_pdf.py --grep "ROIC" --max-hits 40  # 全库正则检索
```

### 3.6 `verify_skill.py` —— skill 完整性自检

```bash
$PY scripts/verify_skill.py
```
校验 frontmatter、references 索引与磁盘一致、每份 reference 是否带页码引用、脚本可编译、Excel 可打开。

---

## 4. 资产（Excel 模板）

> **本仓库不含 `assets/`。** 那 6 份 xlsx 是课件原始分发文件（含 3 份完整成品模型），版权归原作者，
> 不在此处转载。下面记录其结构，可据此自行搭建；若你持有课件库，直接从对应 Module 目录取用即可。

| 文件（需自备） | 内容 |
|---|---|
| `model_template.xlsx` | **规范建模模板**（源自 `scratch_modeling_101.xlsx`）。Tab 架构：`SUM` / `1 - blank` / `2 - input 1` / `3 - operating data` / `4 - analysis rows` / `MOD`。新模型从这里复制 |
| `dcf_scenarios.xlsx` | 5 个 DCF 情景表：`MARKET DCF` / `FAST GROWTH DCF` / `MARGIN DCF` / `ROIC DCF` / `MUDDY TV DCF` |
| `sniff_screen.xlsx` | 想法筛选表：`SNIFF - FLAT` / `SNIFF - FACTSET PULL` / `SNIFF TEST FOCUS` / `PERF` / `NTM PULL` |
| `nvda_mod.xlsx` | 成品模型范例（NVDA）：含 `VAL` / `REVERSE PE` / `7YR MODEL` / `SELL-SIDE` / `NTM EPS` / `CAPITAL CYCLE` |
| `nflx_mod_send.xlsx` | 成品模型范例（NFLX）：含 4 张 DCF 情景表 / `MULTIPLE HISTORY` / `UNIT ECONOMICS` / `COST STRUCTURE` / `BIZ MOMENTUM` |
| `wgo_mod.xlsx` | 成品模型范例（WGO）：thesis development 配套模型 |

**规范 MOD 行序**（建模时按此顺序，缺行必被质疑）：

```
产出与交付量 → 单位经济（单价/单耗/单毛利） → 收入分项（% yoy / % 2 yoy / % qoq）
→ 成本分项（% of sales / bps yoy） → 毛利 + INCREMENTAL MARGIN
→ 费用（R&D / SG&A，均带 % of sales + bps yoy） → 营业利润 + 增量利润率
→ 非经常项 → 税率 → 净利 → 非 GAAP 桥 → 摊薄股数 → EPS
→ EBITDA → 资产负债表 → 杠杆 → ROIC 块（NOPAT/IC/ROIC/增量ROIC/有形ROIC）
→ 现金流量表 → FCF 块（OCF / Capex / ΔWC / FCF / FCF yield） → CHECK 行
```

`SUM` 页必须有的输出区：Ticker / Action / Last Updated / Cap Table（Price、Shares、MC、Debt、Cash、Net Debt、NCI、EV）、
估值倍数（EV/Sales、EV/EBITDA、P/E、Street 对照、FCF Yield）、
牛熊目标价、**Tactical R/R 价格阶梯**（Reward / Risk / R/R / % move）。

---

## 5. 参考文件索引

| 文件 | 覆盖 | 何时读 |
|---|---|---|
| `references/01-foundations-and-process.md` | M1 基础 + M2 买方流程 | 任何研究的起点；市场有效性、WACC 搭建、六步流程、敞口框架 |
| `references/02-thesis-development.md` | M3 论点开发 | 建论点、ETIK→KD、9 步流程、Gauntlet、PM 三问 |
| `references/03-stock-drivers-and-ideas.md` | M4 股价驱动 + M5 想法生成 | 找 idea（10% 心态、FEV、Sniff Test）、Focus Five、3R 拆解 |
| `references/04-modeling.md` | M6 建模 | 建模规范、9 大预测框架、Forecast Metrics、指引与共识处理 |
| `references/05-business-analysis.md` | M7 生意分析 | 单位经济、护城河、ROIC、FCF、财务质量 |
| `references/06-industry-and-management.md` | M8 行业 + M9 管理层 | 行业结构与 primer 方法、管理层评估、资本配置纪律、SBC |
| `references/07-expectations.md` | M10 预期 | 反推市场隐含假设、写市场观点、算预期差 |
| `references/08-valuation.md` | M11 估值 | DCF 全套、资本成本、终值方法、倍数与其失效场景、常见错误 |
| `references/09-short-selling.md` | M12 做空 | 空头论点、借券、逼空风险、风控清单 |
| `references/10-earnings-and-pitch.md` | M13 财报季 + M14 路演 | 共识与修正、财报日流程、pitch 结构与幻灯片规范 |
| `references/11-portfolio-and-risk.md` | M15 收官 | 组合排序、仓位、风险、跟踪节奏 |
| `references/12-supplemental-reading.md` | 延伸阅读（Mauboussin / Damodaran 等） | 需要公式原文与判断依据时；含 ~110 篇行业 primer 索引 |

---

## 6. 硬性数字（不得篡改）

这些数字是课件的锚点，写报告时必须一致：

| 数字 | 含义 | 出处 |
|---|---|---|
| **25–35 年** | 一只普通股需 25–35 年 FCF 折现才能解释今日股价（股权久期） | `[M1 p.16]` |
| 4% / 7% / 10% / 11% / 12% 股权成本 → **55x / 27x / 16x / 11x / 8x** 隐含 P/E | 估值与资本成本的对应关系 | `[M1 p.10]` |
| **TV < 25% NPV** | 终值占比红线 | `[M3 p.66]` |
| 8–10% 增长 → **22–30x**；4–6% 增长 → **14–17x**；零增长 → **8–10x** | 增长对应的合理 P/E 区间 | `[M4 p.78]` |
| 增长 5%→10% 持续 10 年，公允 P/E **16x → 31x** | Focus Five #1 | `[M4 p.77]` |
| 利润率每年 +100bps × 5 年，公允 P/E **16x → 26x** | Focus Five #2 | `[M4 p.79]` |
| Capex 从 3% 降到 1% 收入占比，公允 P/E **16x → 21x** | Focus Five #3 | `[M4 p.80]` |
| 再投资率 20% / 10% / 5%，$10 起 3 年后 → **$17.28 / $13.31 / $11.58** | Focus Five #4 | `[M4 p.81]` |
| 终值归零后 P/E 塌到 **4.7x** | Focus Five #5 | `[M4 p.83]` |
| **65 小时** | 一个 idea 从零开始的尽调工时 | `[M5]` |
| 300 → 30 → 3 | 想法漏斗（300 个筛成 30 个，30 个里成 3 个） | `[M3]` |
| **5–7%** | 首次指引的初始缓冲垫 | `[M6]` |
| **26%** | 分析师 EPS 分歧度 | `[M6]` |
| **75%** | 日收益中非个股特质部分的占比 | `[M4]` |
| **3–5%** | 对冲 2&20 所需的 alpha | `[M2]` |
| **PSUC 50% / 83.3% / 9.1%** | 抛硬币 / 并购套利 / 10:1 赔率生物科技 | `[M3]` |
| **R/R ≥ 2.0x** 可建仓，**≥ 3.0x** = slam-dunk | 建仓门槛 | `[M3]` |
| 15–35% | 正常化倍数上限（常态 12–20x） | `[M3]` |
| 短仓：借券费 **2.5–20%**，单笔仓位 **2.0–2.5%**，单笔亏损 ≤ 组合 **50bps** | 做空风控 | `[M12]` |

---

## 7. 边界（不要越界做）

- **不写最终投研报告成稿**。用户要成稿 → 交给 `equity-research`（8 段式报告）；本 skill 提供骨架与计算。
- **不抓数据**。财务与行情数据走 Bloomberg MCP（`financial-data`），本 skill 只管方法。
- **不替代做空流程**。要做空完整意见 → 先读 `references/09-short-selling.md`。
- **不编造数字**。模型输入必须来自真实披露；估计值要标注来源与置信度。
- **不给投资建议**。输出是研究框架与计算，不是买卖指令。

---

## 8. 常见失误（自查）

| 失误 | 后果 | 约束 |
|---|---|---|
| 先有观点再找证据 | 论点变成故事 | ETIK 在前，KD 在后 |
| 没算风险回报就讲观点 | PM 第一个问题就答不上 | 先做情景与 PSUC |
| 终值占 NPV 过高 | 结论由假设决定 | < 25% |
| 用错 EPS 口径 | P/E 差 26%（17.5x vs 23.7x） | 同一处必须口径一致 |
| 只写多空逻辑不写否决项 | 拿着坏想法不放 | Gauntlet of Disqualifiers |
| 忽略催化剂路径 | "被 paid" 无从谈起 | 必须写兑现路径 |
| 模型与论点脱节 | 模型不驱动结论 | 模型是论点的骨干 |
| 综述冗长 | IC 会上没人听 | 60 秒讲完 + 45 分钟深聊 |

---

## 9. 附录：引用标记与回查

`references/` 里每条规则后面都带 `[M<模块号> p.<页码>]` 标记（延伸阅读部分用 `（*文献名*, p.N）`），
指向原课件/原文献的页码。摘要不足以支撑某个细节时，用 `scripts/extract_course_pdf.py` 回原文取原话：

```bash
export FUNDAMENTAL_EDGE_ROOT="/path/to/course library"   # 或每次传 --root
$PY scripts/extract_course_pdf.py --grep "ROIC" --max-hits 40
```

课件库结构参考：`Module 1-Fundamental Foundations` … `Module 15-Wrapping Up`，
延伸阅读在 `Module N/Supplemental Readings/` 与 `Module 8-Industry Coverage/Industry Primers/`（约 110 份行业 primer）。
