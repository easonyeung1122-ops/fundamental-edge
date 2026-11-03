# fundamental-edge

> **语言**：[中文](README.md) · [English](README.en.md)

买方基本面研究方法论 skill —— 把「看一只股票」变成一条**可重复、可审计、可交接**的研究流水线。

配套 **4 个零依赖计算脚本**（DCF / Reverse DCF / ROIC / 风险回报）和 **12 份方法论 reference**（约 82 万字符，每条规则都带页码溯源）。

```
生意本质 → 行业 → 3 个关键驱动 → 财务模型 → 预期差 → 估值
   → 牛熊情景 / 风险回报 / 仓位 → 催化剂 → 论点 → 路演 → 跟踪
```

> 方法论整理，**不构成投资建议**。作者与原始课件无关，详见[来源与版权](#来源与版权)。

---

## 立场

**价格是一份 FCF 预测（Price is a FCF forecast）。基本面研究不是找真相，是找预期差。**

市场大多数时候是对的。可重复的 alpha 来自三件事的叠加：

```
扎实的底层技能  →  可重复的严谨流程  →  靠实战磨出的判断力
```

具体到操作层面，三句话概括这套方法：

| 立场 | 含义 | 反面 |
|---|---|---|
| **先写市场观点，再写自己的** | 用 reverse DCF 反推价格里已隐含什么 | 先有结论再找证据 |
| **风险先于回报** | "Take care of the risk case and the reward will take care of itself" | 只算上行空间 |
| **终值占 NPV < 25%** | 超过就说明结论是假设的函数，不是估值的产物 | 拿 30 年后的永续增长率当论据 |

---

## 安装

```bash
git clone https://github.com/easonyeung1122-ops/fundamental-edge.git \
  ~/.codebuddy/skills/fundamental-edge
```

或放到 `~/.workbuddy/skills/`（WorkBuddy 用户级）、`.codebuddy/skills/`（项目级）。

脚本**仅依赖 Python 标准库**，无 pip install。Windows 用 `py -3`，macOS/Linux 用 `python3`。

---

## 目录结构

```
fundamental-edge/
├── SKILL.md                              # 入口：主流程、脚本速查、硬性数字、边界
├── references/                           # 12 份方法论详解（按模块）
│   ├── 01-foundations-and-process.md     # M1 基础 + M2 买方流程
│   ├── 02-thesis-development.md          # M3 论点开发（ETIK→KD→VB→EP）
│   ├── 03-stock-drivers-and-ideas.md     # M4 股价驱动 + M5 想法生成
│   ├── 04-modeling.md                    # M6 建模（9 大预测框架）
│   ├── 05-business-analysis.md           # M7 生意分析（护城河 / ROIC / FCF）
│   ├── 06-industry-and-management.md     # M8 行业 + M9 管理层与资本配置
│   ├── 07-expectations.md                # M10 预期与 reverse DCF
│   ├── 08-valuation.md                   # M11 估值全套
│   ├── 09-short-selling.md               # M12 做空
│   ├── 10-earnings-and-pitch.md          # M13 财报季 + M14 路演
│   ├── 11-portfolio-and-risk.md          # M15 组合与风险
│   └── 12-supplemental-reading.md        # 延伸阅读（Mauboussin / Damodaran 等）
└── scripts/
    ├── dcf.py                            # DCF + 资本成本构建 + 敏感性
    ├── reverse_dcf.py                    # 市场隐含假设 + 预期差
    ├── roic.py                           # ROIC / 价值创造 / 再投资敏感性
    ├── riskreward.py                     # R/R / PSUC / 回报阶梯 / 仓位 / 敞口
    ├── extract_course_pdf.py             # 回查课件原文（需自备课件库）
    └── verify_skill.py                   # skill 完整性自检
```

---

## 快速开始

### 1. DCF + 资本成本构建

```bash
py -3 scripts/dcf.py --csv fcff.csv --build-wacc \
  --rf 0.045 --beta 1.0 --erp 0.05 --kd 0.06 --tax-rate 0.25 \
  --equity-weight 0.70 --debt-weight 0.30 \
  --terminal-growth 0.025 --net-debt 500 --shares 100 --eps 1.85 --price 18 --sensitivity
```

真实输出（截选）：

```
### 资本成本构建
| 股权成本 Ke        | 9.50% |
| 税后债务成本        | 4.50% |
| WACC              | 8.00% |

### 估值桥
| 显性期现值 (PV of FCF) |   527.00 |
| 终值现值               | 2,218.36 |
| 企业价值 EV            | 2,745.36 |
| 股权价值               | 2,245.36 |
| 每股价值               |   22.45 |
| 终值占 NPV 比重        | 80.80% (**超标**, 目标 <25%) |
```

终值占比超红线会主动告警 —— 这是最有价值的一条内置纪律。

### 2. 反推市场隐含假设

```bash
py -3 scripts/reverse_dcf.py --csv fcff.csv --price 22.45 --shares 100 \
  --net-debt 500 --solve all --wacc 0.08 --internal-value 30
```

```
| 市场隐含永续增长率 g  |  2.50% |
| 市场隐含 WACC        |  8.00% |
| 市场隐含终值倍数      | 18.63x |
```

配合 `--internal-value 30` 直接算出**预期差**：市场只给了 22.45，我认为值 30，缺口 34%。

`--solve margin` 可反推市场隐含的**稳态经营利润率**（给收入路径 + 目标 P/E 即可）。

### 3. ROIC 与价值创造

```bash
py -3 scripts/roic.py --ebit 500 --tax-rate 0.25 --nwc 100 --net-fixed-assets 800 \
  --wacc 0.08 --delta-nopat 60 --delta-ic 200 --growth 0.10 --reinvestment-sensitivity
```

输出 ROIC / 有形 ROIC / **ROIC−WACC 利差（bps）**、价值创造额、增量 ROIC、隐含再投资率，
以及可复现课程锚点的再投资率敏感性表。

### 4. 风险回报、仓位与 PSUC

```bash
py -3 scripts/riskreward.py --price 100 --target 140 --stop 85 \
  --ntm2-eps 8.5 --ntm2-pe 22 \
  --scenario "bull:150:0.30,base:110:0.50,bear:70:0.20" \
  --portfolio-value 1000000 --risk-pct 0.01
```

```
| 上行 Upside |  40.00% |
| 下行 Downside | 15.00% |
| R/R         |  2.67x |
| PSUC        | 72.73% |
| 裁定        | 可建仓 (门槛 ≥ 2.0x，≥ 3.0x = slam-dunk) |
```

**PSUC** = 上行 / (上行 + |下行|)，即「这笔下注有多像抛硬币」。锚点参照：抛硬币 50% / 并购套利 83.3% / 10:1 赔率生物科技 9.1%。

所有脚本支持 `--format md|tsv|both`，TSV 可直接粘进 Excel。

---

## 已验证的锚点

脚本不是凭感觉写的 —— 用课程公开的算例做过往返校验：

| 校验项 | 期望 | 实际 |
|---|---|---|
| WACC 构建 | Ke 9.5% × 70% + 税后 Kd 4.5% × 30% = **8.0%** | 一致 |
| Reverse DCF 往返 | 输入 g=2.5% / WACC=8% → 反解回 **2.50% / 8.00%** | 一致 |
| 隐含终值倍数 | DCF 正算 18.63x vs reverse 反解 18.63x | 一致 |
| 再投资率敏感性 | $10 起 3 年后 → **$17.28 / $13.31 / $11.58** | 一致 |
| 终值归零后的 P/E | **4.7x** | 一致 |

`scripts/verify_skill.py` 可一键自检：frontmatter、references 索引与磁盘一致、每份 reference 的页码引用、脚本可编译。

---

## 硬性数字（不得篡改）

这些是方法论的锚点，写报告时必须对齐：

| 数字 | 含义 |
|---|---|
| **25–35 年** | 普通股需 25–35 年 FCF 折现才能解释今日股价（股权久期） |
| **55x / 27x / 16x / 11x / 8x** | 股权成本 4% / 7% / 10% / 11% / 12% 对应的隐含 P/E |
| **< 25%** | 终值占 NPV 的上限 |
| **22–30x / 14–17x / 8–10x** | 8–10% 增长 / 4–6% 增长 / 零增长 对应的合理 P/E |
| **16x → 31x** | 增长从 5% 提到 10% 并持续 10 年，公允 P/E 的扩张 |
| **16x → 26x** | 利润率每年 +100bps 持续 5 年 |
| **16x → 21x** | Capex 从 3% 降到 1% 收入占比 |
| **4.7x** | 终值归零后 P/E 塌到的位置 |
| **65 小时** | 一个 idea 从零开始的尽调工时 |
| **300 → 30 → 3** | 想法漏斗 |
| **5–7%** | 首次指引的初始缓冲垫 |
| **26%** | 典型分析师 EPS 分歧度 |
| **75%** | 日收益中非个股特质部分的占比 |
| **3–5%** | 对冲 2&20 费率所需的 alpha |
| **≥ 2.0x / ≥ 3.0x** | R/R 建仓门槛 / slam-dunk 门槛 |
| **2.5–20%** | 做空借券费区间 |
| **≤ 50bps** | 单笔做空对组合的最大亏损容忍 |

---

## 主流程：六步

| # | 步骤 | 交付物 |
|---|---|---|
| 1 | 机会评估 | 市场已 price in 什么；alpha load 有多大 |
| 2 | 生意分析与建模 | 自建财务模型，判断 business momentum 与潜在修正 |
| 3 | 关键驱动评估与深挖 | 锁定 **3 个关键驱动**，建立差异化认识 |
| 4 | 情景构建与风险回报 | bull/base/bear + R/R 够不够 |
| 5 | 论点构建与表达 | 结构化论点 + pitch |
| 6 | 想法跟踪与催化剂 | 催化剂日历 + thesis 是否 still on track |

**跳步 = 犯错。** 尤其不能在建模型前就验证结论，也不能在算清风险回报前讲观点。

论点链条：`ETIK（全知）→ KD（3 个关键驱动）→ VB（价值信念）→ EP（入场点）`

任何论点最后必须回答三个问题：

1. **Get me up to speed** —— 3 分钟讲懂这门生意
2. **Where are we different & why** —— 分歧在哪，为什么我们对
3. **What is our path to getting paid** —— 靠什么兑现

答不上第 2、3 问的，不是论点，是故事。

---

## 常见失误自查

| 失误 | 后果 | 约束 |
|---|---|---|
| 先有观点再找证据 | 论点变成故事 | ETIK 在前，KD 在后 |
| 没算风险回报就讲观点 | 第一个问题就答不上 | 先做情景与 PSUC |
| 终值占 NPV 过高 | 结论由假设决定 | < 25% |
| 用错 EPS 口径 | P/E 可差 26%（17.5x vs 23.7x） | 同一处口径必须一致 |
| 只写多空逻辑不写否决项 | 拿着坏想法不放 | Gauntlet of Disqualifiers |
| 忽略催化剂路径 | 「被 paid」无从谈起 | 必须写兑现路径 |
| 模型与论点脱节 | 模型不驱动结论 | 模型是论点的骨干 |

---

## 来源与版权

方法论源自 **Fundamental Edge**（作者 Brett Caughran）的买方培训课件。

本仓库是**方法论的独立结构化整理与再表达**，性质如下：

- **不包含**课件原始 PDF、Excel 模型模板或任何原始文件
- **不复制**课件原文整章；引用的短句仅用于说明概念，均标注页码
- 12 份 reference 是把课件中的框架、判据、阈值重新组织成的可执行笔记，附带大量自行推导的计算示例与脚本实现
- 原始课件的全部权利归原作者所有。**如果你要系统学习，请购买原课程**

配套的 Excel 建模模板（规范 MOD 行序、DCF 情景表、NVDA/NFLX/WGO 成品模型）**刻意未纳入本仓库**，因为它们属于课件的原始分发文件。`SKILL.md` 第 4 节以文字形式完整记录了规范 MOD 行序与 `SUM` 页结构，可据此自行搭建。

延伸阅读部分（Mauboussin / Damodaran / Wolfe Research / Credit Suisse / PWC / Zion / Bear Stearns 等）同样是**论点摘要与公式整理**，不含原文，版权归各原作者。

## License

`scripts/` 下代码：**MIT**。
`references/` 与 `SKILL.md` 文档：仅供个人研究学习，不得转售或作为付费产品分发。

逐项第三方权利归属见 [NOTICE.md](NOTICE.md)。

---

> 方法论研究，**不构成投资建议**。所有计算示例均为演示，不对应任何真实标的的操作建议。
