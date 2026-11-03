# 01 · 基本面基础与买方研究流程（Module 1 + Module 2）

> 本文件覆盖 Fundamental Edge 买方培训课件 **Module 1: Fundamental Foundations**（111 页）与 **Module 2: Life on the Buy-Side**（116 页）。
> 引用格式：`[M1 p.97]` 表示 Module 1 第 97 页，`[M2 p.90]` 表示 Module 2 第 90 页。

---

## 0. 全局框架速览

### 0.1 两个模块的结构

| 模块 | 结构 | 核心命题 |
|---|---|---|
| **Module 1 · Fundamental Foundations** | 1. The Market Based-Economy & Fundamental Analysis；2. The Myth of Market Efficiency & The Messy Reality of Markets；3. Four Reasons The Markets Are Not Efficient；4. Alpha-Load & The Many Faces of Mispricing；5. A Three-Part Recipe For Well-Practiced Fundamental Analysis `[M1 p.3]` | 市场有效性只是神话；股价是"资本加权的共识"，价格本身就是一份 FCF 预测；基本面研究者的任务不是找到真相，而是找到**预期差**并建立**可重复的流程**去收割 alpha |
| **Module 2 · Life on the Buy-Side** | 1. The Limited Partner (LP)；2. Buy-Side Primer；3. The Role of the Analyst；4. Buy-Side Investment Process；5. Buy-Side Mentality `[M2 p.3, p.105]` | 买方是"在机构资本池上行使裁量权的生意"；alpha pool 是零和的，费用（2 & 20）把主动管理变成"小于零和"的博弈 |

### 0.2 三条贯穿性立场

1. **价格是 FCF 预测**（Price is a FCF forecast）：基本面分析实质是"对长期 FCF 流的分析" `[M1 p.28]`。
2. **市场有效性是情境化的，而非绝对的**：**"Market gets it right more often than not"** `[M1 p.57]`。
3. **流程与判断力是分层的**：FOUNDATIONAL SKILLS → RIGOROUS, REPEATABLE PROCESS → SOUND JUDGMENT → MASTERY `[M1 p.95]`。

### 0.3 关键概念索引（先看表，后看细节）

| 概念 | 一句话定义 | 出处 |
|---|---|---|
| **Expectations gap** | **市场观点 − 内部观点**（market view − internal view） | `[M1 p.91]` |
| **Alpha load** | 价格与价值之间的差（price vs. value gap） | `[M1 p.93]` |
| **Alpha** | 相对市场组合的超额回报（excess return relative to the market portfolio） | `[M1 p.85]` |
| **WACC** | Ke×E/V + Kd_after_tax×D/V | `[M1 p.10]` |
| **Equity duration** | 一只普通股票需要 **25-35 年** FCF 折现才能解释今日股价 | `[M1 p.16]` |
| **ETIK → KD → VB → EP** | Everything There Is To Know → Key Drivers → Value Belief → Entry Point | `[M1 p.59]` |
| **Voting machine / Weighing machine** | 短期市场是投票机，长期是称重机（Graham） | `[M1 p.101]` |
| **Net / Gross exposure** | Net = (LMV − SMV) / Investor Equity；Gross = (Equity + Leverage) / Investor Equity | `[M2 p.55]` |
| **Market move × net exposure** | = predicted fund performance | `[M2 p.75]` |

---

# PART A — MODULE 1 · FUNDAMENTAL FOUNDATIONS

## A1. 市场经济、价格信号与企业生命周期

### A1.1 市场经济框架

资本市场的有效性建立在 **4 个前提**上 `[M1 p.6]`：

1. A system that creates **price signals** to direct the flow of capital
2. **Educated & motivated** participants
3. **Incentives for success** within the system
4. Appropriate **regulatory authority**

价格信号的作用：把资本从"寻求回报者"导向"需要资本者"——从 savers 到 spenders，从 investors 到 enterprise。

### A1.2 企业生命周期与资本流向

| 阶段 | 特征 |
|---|---|
| **Young Business** | 需要融资才能达到规模与成熟；获取资本是"生死攸关"；资本来源：Private (VC)、IPO、Debt Markets；consumptive（消耗资本） |
| **Growing Business** | 变得盈利、无需增量融资，成为 capital self-sustaining；开始返还资本（股息、回购、还债）；**早期投资者回报的关键来源**；过度估值 → 过多资本流入行业；估值过低 → 资本流入不足；公允估值 → 合理流动 + 合理回报概率 `[M1 p.7]` |
| **Maturing Business** | （课件图示）`[M1 p.7]` |
| **Declining Business** | （课件图示）`[M1 p.7]` |

核心隐喻：**"CAPITAL IS GASOLINE FOR ENTERPRISE"** —— 没有投资者资本，年轻的/消耗型的企业可能永远不会存在。

### A1.3 股票 vs. 债券：两套定价框架

| 维度 | STOCKS (EQUITY) | BONDS (DEBT) |
|---|---|---|
| **FORMS** | Venture capital, private equity, public equity | Loans (bank loans, private loans), public debt, hybrid structures (converts) |
| **PAYOUT STRUCTURE** | Residual（股权拿剩下的） | Contractual coupon & par at maturity |
| **VALUATION FRAMEWORK** | Dividend equivalence, FCF discounting, equity multiples | Discount coupon & par value, adjust for interest rate & repayment risk |
| **CRITICAL QUESTION** | **What is the business worth?** | **Will I get paid back?** |

`[M1 p.14]`

### A1.4 股票的构成

股票 = **Fractional economic ownership** + **voting rights (board)** + **claim on cash flow** = 一小块饼（tiny slice of the pie）`[M1 p.18]`。

---

## A2. "一切都是 DCF"（Everything is a DCF）

### A2.1 三层推导

1. **Finance 101**：**The present value of any asset is the discounted value of its future cash flows.** `[M1 p.16]`
2. **DCF**：一个"simple, not easy"的框架（引 Mauboussin）`[M1 p.16]`
3. **结论**：**"A standard equity requires 25-35 years of FCF discounting to achieve today's share price"** `[M1 p.16]`

### A2.2 DCF 101 三步法 `[M1 p.9]`

1. Forecast **5 years of FCFs**
2. Apply a **terminal multiple to year 6**
3. Discount at **WACC**

### A2.3 Multiples 不是独立方法

**"Multiples are a shortcut to DCF"** `[M1 p.9]`。
投资过程恒为两条问题：
- **What drives free cash flows?**
- **What drives valuation (discount rate)?**

### A2.4 价格形成机制：学术定律 vs. 现实四步链条

**学术定律**：NPV of an equity = 折现后的 unlevered FCF − Net Debt。

**但现实中（p.44, p.52）：**

1. **Academic law**：NPV of an equity is the discounted value of unlevered FCF less Net Debt
2. **BUT VISIBILITY INTO THOSE CASH FLOWS IS HIGHLY LIMITED** —— **"Even the CFO likely only has 6-18 months of visibility"** `[M1 p.44]`
3. **GIVEN LIMITED VISIBILITY, COLLECTIVE LT VIEWS ARE INFLUENCED BY ST DATA POINTS**
4. **"Those incremental sales may be informed by a view of NPV, but often they are not. Forced or emotional sellers, non-fundamental sellers (ETF flows). Scared sellers."** `[M1 p.44]`

配套约束：**Company specific fundamentals 只解释近端股价波动的 <50%**；其余来自 interest rates、flows / sentiment / liquidity / macro / geopolitical `[M1 p.67]`。

### A2.5 两种机制

| 机制 | 内容 | 出处 |
|---|---|---|
| **Business momentum / "Observation mechanism"** | Extrapolation due to lack of visibility；Narrative, newsflow, positioning, revisions & catalysts；Risk reversals & regime rotations | `[M1 p.51]` |
| **Discounting mechanism（Buffett 的农场比喻）** | "The wise farmer buys below intrinsic value, sells above intrinsic value. Erratic." —— **"You would not cut the value of a good farm in half just because bad weather conditions caused a crop failure in a single year."**（PHIL FISHER） | `[M1 p.100]` |

Graham 的补充 `[M1 p.101]`：**"In the short run, the market is a voting machine but in the long run it is a weighing machine."**
目标拆解为三件事：
1. develop an **accurate weighing machine**（一个流程）
2. monitor the **voting machine** for aberrant behavior
3. invest when there is a **gap**（判断力）

### A2.6 市场机制与关键术语

- **The Market**（通常指 S&P 500）、Ticker、Stock Exchange、**Order Book**
- **Continuous Double Auction**、**Bid/Ask Spread**、**Last Sale**
- **关键洞见**：**A 20% "gap" up or down doesn't necessarily require big capital flow. Can be a "buyer's strike" or "seller's strike"** `[M1 p.20]`
- **Price: a function of "capital-weighted opinion"**；市价是买卖双方的 equilibrium point
- **Voting machine（order book / last sale）vs. Weighing machine（intrinsic value）** `[M1 p.31, p.101]`

### A2.7 三种定价方法（对照基本面）

| 方法 | 特征 |
|---|---|
| **QUANTITATIVE** | Repeating patterns；Super computers；Small quantitative edge |
| **TECHNICAL** | Recurrence of price patterns；Simple: support/resistance, momentum；Complex: MACD crossover, Fibonacci retracements |
| **INDEXATION ("no method, method")** | If stock meets index criteria, buy it |

`[M1 p.25-26]`

### A2.8 基本面分析的四个向量

- **BUSINESS ANALYSIS → VALUATION → DIFFERENTIATION → THESIS DEVELOPMENT → EXECUTION & MONITORING** `[M1 p.27, p.29, p.31]`
- Vectors：**COUNTRY → INDUSTRY → BUSINESS → STOCK** `[M1 p.29]`

课程定义 `[M1 p.28]`：

- Fundamental Analysis = "a method that attempts to determine a security's value by focusing on the underlying factors that affect a company's actual business & it's future prospects"
- Fundamental Investing = "ultimately, a view on FCF generation"
- Fundamental Analysis = "analysis of the myriad factors that impact the long-term FCF stream"

---

## A3. 资本成本与 WACC 构建

### A3.1 公式 `[M1 p.10]`

```
Cost of Equity = Risk free + Beta × ERP
WACC = Cost of Equity × E/V + Debt YTM After Tax × D/V
```

### A3.2 完整算例 `[M1 p.10]`

```
Cost of Equity = Risk free 4.5% + Beta 1.0x × ERP 5.0% = 9.5%
WACC = Cost Equity 9.5% × E/V 70.0% + Debt YTM After Tax 4.5% × D/V 30.0% = 8.0%
```
（利率 6.0%，税后 4.5%）

### A3.3 Cost of Equity ↔ WACC ↔ Implied P/E 对照表 `[M1 p.10]`

| Cost of Equity | WACC | Implied P/E |
|---|---|---|
| **4%** | 4% | **55.0x** |
| 7% | 6% | 27.0x |
| 10% | 8% | 16.0x |
| 11% | 10% | 11.0x |
| **12%** | 12% | **8.0x** |

**读法**：贴现率从 12% 降到 4%，隐含 P/E 从 8.0x 膨胀到 55.0x —— **同一份盈利在不同的资本成本下对应完全不同的"合理价"**。因此**资本成本是估值的第一性输入**，不是技术细节。

### A3.4 高低估值如何驱动资本形成 `[M1 p.11]`

| | High Valuation | Low Valuation |
|---|---|---|
| WACC | 4.0% | 12.0% |
| Cost of Equity | 4.0% | 12.0% |
| Implied P/E | 55.0x | 8.0x |
| Illustrative Net Income | $100 | $100 |
| Public Market Valuation | $5,500 | $800 |
| **Private Market Incentive** | **HIGH** | **LOW** |
| Private Mkt Valuation | $1,000 | $1,000 |
| **Return on Private Money** | **5.5x** | **0.8x** |

### A3.5 "Cure for Cancer" 案例：价格信号的反身性（reflexivity）`[M1 p.12-13]`

两个通过 Phase II 的肿瘤药，一个有希望一个没有：

| | Promising | Not Promising |
|---|---|---|
| Market Valuation, Post Phase II | $3,000 | $300 |
| Required Phase III Capital | $500 | $500 |
| Dilution Necessary | 16.7% | n.a. |
| Incremental Capital | $500 | $0 |
| % ownership | 16.7% | n.a. |
| Post Phase III Valuation | $9,000 | n.a. |
| Investor Returns | $1,500 | n.a. |
| **Investor Money Multiplier** | **3.0x** | n.a. |

结论：**POSSIBLE vs NOT POSSIBLE**。但课程明确指出 **"This capital allocation process is not benevolent in nature"** —— 增量资本要求回报，$500m 风险注入需要 expected return。

---

## A4. 市场有效性的神话与 messy reality

### A4.1 EMH 三形式 `[M1 p.33-43]`

| 形式 | 主张 |
|---|---|
| **Strong form** | 所有历史价格与回报都包含在价格中 |
| **Semi strong** | 所有公开信息都被价格反映 |
| **Weak form** | 所有信息（公开与私有）都被价格反映 |

### A4.2 三个 simplifying assumptions `[M1 p.36]`

1. **Equal diffusion of information**
2. **Equal skill in interpreting information**
3. **"Rational man" theory**

### A4.3 Jelly-bean jar 实验 `[M1 p.35]`

1987 年，罐中 **850 颗**糖豆；全班平均估计 **871**（**2.5% error**）；仅 **1/56** 人更准。
→ 结论：**crowd is smarter than the individual**（这正是 EMH 阵营最强的证据）。

延伸：现实中的 jelly-bean jar 是 **5 维的** `[M1 p.71]` —— value creation/destruction；market share battles；increasing/decreasing visibility；management deception；discount rates/macro/regime。

### A4.4 对 EMH 的挑战 `[M1 p.37-38]`

- **"A tenuous assertion"** —— 假设可被证伪；anomalies 太多；quant/industrial alpha；**pockets of consistent fundamental alpha**
- **"Because it's hard, markets are efficient" / "Poker is hard too…"**（循环论证）
- Pareto distribution
- **The Myth of Market Efficiency**：Factor harvesting（Citadel & Millennium）；observed price action / dispersion；persistent boom-bust、optimism-pessimism cycles

### A4.5 权益定价的挑战 `[M1 p.39]`

Equity duration；no contractual payout stream；high failure rate（many go to zero）；dynamic competition；unpredictable externalities。

### A4.6 Equity Duration 的量化 `[M1 p.40, p.45]`

以一只 **20x P/E** 股票的 DCF 价值构成为例：

| 期限段 | 占 DCF 价值比重 |
|---|---|
| 0-5 年 | **14%** |
| 5-15 年 | **26%** |
| 15 年及以后 | **60%** |

NFLX 实例：30 年后企业价值覆盖 **87%** `[M1 p.40]`。
标准股票需要 **25-35 年** FCF 折现 `[M1 p.16]`。

### A4.7 估值是观点 `[M1 p.42]`

**"Valuation is a point of view"** —— "As a small rotation of the kaleidoscope can change the image, a seemingly small change in current fundamentals can meaningfully impact the valuation point of view of the market."

### A4.8 情境化市场效率 `[M1 p.56-58]`

- **Price is a FCF forecast**；process & judgment；information & insight leads to better pricing；market incentives for enforcing efficiency（找出 underpriced 并推高 = alpha）；**mosaic approach to information**
- **"Remember equity duration. No hope of truth. Price simply a capital weighted consensus."** `[M1 p.56]`
- **"Situational Market Efficiency"** `[M1 p.57]`：Value trajectory vs. Market implied value；**"Quest for the 10%"**；Outliers；**"Market gets it right more often than not"**
- **A hubristic position** `[M1 p.58]`："I know and others don't know"；前提是 rigorous, repeatable process for idea generation / information gathering / insight generation / value belief formation；bar 很高，不会仅靠 "hunch" 反复发生

### A4.9 市场外推的四个实例 `[M1 p.46-50]`

| 案例 | 关键数字 | 结论 |
|---|---|---|
| **Sample Business DCF** | EV $1,270,312；Less Net Debt $444,609；Market Cap $825,703；Diluted Shares 58,000；Price $14.24；EPS $1.04；P/E 13.7x | **"CUT THE SAMPLE DCF BY 200BPS AND P/E CORRECTS 15%"** —— "Markets extrapolate because there is no better way to forecast years 2-40." |
| **NFLX** | TTM Net Adds 27,831 → 36,573 → 18,181 → 1,828；Revenue Growth 27.6% → 24.0% → 18.8% → 7.4%；Incremental Margin 24.8% → 41.1% → 34.0% → 4.5%；Avg P/E 70.6x → 59.6x → 48.3x → 24.9x | 增长质量决定倍数 |
| **TDOC** | "Was the telehealth acceleration during COVID a durable acceleration? **The market thought so!**" | 外推的错误定价 |
| **DPZ** | comp 3%+1% → 10-15x P/E；comp 5-8%+ → 25-30x P/E | P/E 与 SSS 的映射 |
| **一次性 EPS 资本化** | EPS 基线 $1，第 2 年一次性 +$1 → P/E 25x→35x，股价 $25→$70（**+180%**），第 3 年回到 $25（**−64.3%**） | 一次性盈利被错误资本化的后果 |

---

## A5. 四大"市场非有效"理由 + 理论 vs 实践对照

### A5.1 四条理由 `[M1 p.55]`

1. **INFORMATION IS DIFFUSED UNEVENLY**（Reason #1, `[M1 p.60]`）
2. **EQUITIES ARE DIFFICULT TO PRICE ACCURATELY**（Reason #2, `[M1 p.67]`）
3. **THE MYTH OF THE RATIONAL PERSON** — "INVESTORS HAVE BIG DIFFERENCES IN WIRING & SKILL"（Reason #3, `[M1 p.73]`）
4. **CAPITAL COMES WITH CONSTRAINTS**（Reason #4, `[M1 p.79]`）

### A5.2 理论 vs. 实践（10 组对照）`[M1 p.54]`

| ACADEMIC THEORY | MESSY REALITY |
|---|---|
| Information is diffused evenly | Information is diffused unevenly and requires effort & expense to gather |
| Information is immediately discounted in asset prices | 股票价格对信息的反映远慢于"立即折现" |
| Equities can be priced with simple formulas like CAPM | Equities are long-duration securities that are hard to price accurately |
| Investors are rational | I mean…come on |
| （无对应） | Investors have big differences in wiring & skill |
| Capital is constraint free & there are no limits to arbitrage | Capital comes with a mandate, "volatility is risk" and "style creep is death" |

### A5.3 Reason #1：信息扩散不均的三层作业体系 `[M1 p.60-66]`

**(a) Developing expertise（10 步）** `[M1 p.61]`

1. Read industry primers & background
2. "Sector 101" meetings with sell-side analysts
3. Subscribe to industry trade magazines
4. Seek out industry consultants
5. Study leading companies
6. Study past industry failures
7. **Create an industry aggregate P&L, BS & CF**
8. Attend sector conferences (non-sell-side)
9. Attend sector conferences (sell-side)
10. Create a network & be seen as an authority

**(b) Daily blocking & tackling** `[M1 p.62]`

flood of e-mails / sell-side notes / macro data-points → ① distillation → ② signal vs. noise → ③ contextualization and updating view of value creation trajectory & degree of misunderstanding；"A continuous conversation" with the company。

**(c) Information tools** `[M1 p.63]`

Expert networks（private competitors, supply chain）；Surveys；Alternative data；Management；Conferences；Sell-side engagement；"Connect the dots" with public peers。

**(d) Signal vs. noise**

老 PM 的话 —— **"the trick to this job is knowing when to panic and when not to"** `[M1 p.63]`。

**(e) Earnings day 标准流程** `[M1 p.65]`

| 时点 | 动作 |
|---|---|
| 6:30am | 读业绩新闻稿；check pre-market reaction；更新模型；读卖方首评；发团队初始 note（聚焦 3 个问题） |
| 8:30am | earnings call；写下当日 estimate trading range；发 follow-up note 含建议交易动作；读卖方 follow-up；约 IR 回访；读 10-Q 补完模型 |
| **3 个关键问题** | ① **3 key drivers 加速还是减速？** ② **beat 还是 miss consensus？** ③ **指引上调/下调/不变？** |

**Complicating factor**：同日还有 ABC/BDX/CAH/GH/MTD/QGEN/TECH/TEVA/XRAY/ZTS 等发布。

### A5.4 Reason #3：行为与买方心态 `[M1 p.73-78]`

**Impacts to human behavior** `[M1 p.76]`：Fear & greed；Rains in NYC；Overconfidence；The bonus cycle；Impatience & uncertainty；Drawdown limits；The 2-year rule。

**Human decision making in practice** `[M1 p.77]`：Keep my seat；Keep my LP happy；Make a big enough bonus to pay my bills；Don't underperform my competitors；Don't underperform the index。

### A5.5 Reason #4：资本约束与 LP 流程 `[M1 p.79-83]`

- **LP 侧关切**：LP expectations；volatility = bad；drawdowns & existential risk；drive for continuous positive P&L；**LPs are your most strategic asset**；hyper-specialization & risk of "mandate creep"
- **Institutional allocation process（3 步）** `[M2 p.12]`：
  - **STEP 1** Determine portfolio allocation（stocks vs. bonds, strategies）
  - **STEP 2** Allocate capital to managers that practice that strategy
  - **STEP 3** Ensure that those managers are performing & staying within the expected mandate
- **Prudent allocator policy（4 条）** `[M1 p.81]`：
  1. minimize risk of **permanent capital impairment**（teacher / firefighter retirements）
  2. create **diversification** to build an **all-weather portfolio**
  3. target a safe **6-8%** return（inflation-adjusted above withdrawal rate）
  4. **minimize expenses**
- **Endowment Policy 算例** `[M1 p.81]`：BOP $1,000；Target Return $80（**8.0%**）；Withdrawal Rate ($50)（**5.0%**）；EOP $1,030（**3.0%**）
- **Performance measurement（5 项）** `[M1 p.83]`：Sharpe；Sortino；Annual cycle；**2 & 20**；Peer relative

---

## A6. Alpha 的定义、来源与形态

### A6.1 定义 `[M1 p.85]`

**ALPHA: EXCESS RETURN RELATIVE TO THE MARKET PORTFOLIO**
- "Excess return" is the fundamental investors' reason for existence
- **no expectation of alpha generation → indexation is the logical response**

**Example 1 / 2 拆解** `[M1 p.85-86]`：Market +10.0%；Stock (beta 1x) 从 $92 涨到 $110 = +20.0%；% return − beta 10.0% = **alpha 10.0%**。

### A6.2 Alpha load 与核心命题 `[M1 p.87, p.93]`

- **"Our quest as active investors is to identify the stock priced to a prospective excess return, or an 'alpha load'"** `[M1 p.87]` —— gap 被市场纠正的过程即产生 alpha
- **ALPHA LOAD = PRICE vs. VALUE GAP** `[M1 p.93]`
- **EXPECTATIONS GAP = MARKET VIEW − INTERNAL VIEW** `[M1 p.91-92]`（source: Credit Suisse）

### A6.3 为什么股票会变便宜（7 条）`[M1 p.88]`

1. Decelerating fundamentals
2. Fears about terminal value
3. Complexity & muddiness
4. Miss & lower cycles
5. Sell-side down-grade cycles
6. Large owners exiting position
7. Fear & uncertainty, in all it's forms

### A6.4 Alpha Buckets（9 类）`[M1 p.89]`

1. Off menu to on menu（"beach ball"）
2. Compounders
3. Mispriced Catalysts
4. Extrapolation, meet inflection
5. Complexity to simplicity
6. Change agent
7. Growth acceleration
8. Cap deploy / cash abundance
9. Early insight innovation

### A6.5 赛马观（horse betting）`[M1 p.90]`

不是找最快的马或最好的骑师，而是：
1. **observing the odds**
2. **creating a process to analyze factors that determine probabilities**
3. **betting where the odds differ from internally expected outcomes**

### A6.6 成功公式：三层配方与投资金字塔

**Pyramid of Mastery** `[M1 p.95]`：

```
YEARS OF LEARNING & DOING
        ↓
DEVELOPING THE TOOLBOX
        ↓
APPLYING THAT TOOLBOX
FOUNDATIONAL SKILLS → RIGOROUS, REPEATABLE PROCESS → SOUND JUDGMENT → MASTERY
```

**A Recipe for Solid Fundamental Investing** `[M1 p.96]`：

1. **BUILD A STRONG BASE OF FOUNDATIONAL SKILLS** —— accounting, corporate finance, corporate strategy
2. **CONSTRUCT A RIGOROUS, REPEATABLE INVESTMENT PROCESS** —— curated to your investment strategy & organization
3. **DEVELOP STRONG INVESTMENT JUDGMENT** —— by learning through doing

### A6.7 6 步投资流程（Investment Process）`[M1 p.97]`

| # | 步骤 | 描述 |
|---|---|---|
| **1** | **Opportunity Assessment —— "Is this interesting?"** | 弄清股价里已经 priced-in 什么，是否有产生 differential view（"the alpha load"）的机会 |
| **2** | **Business Analysis & Model Construction** | 构建 bespoke financial model，用 model 作为 backbone 估值股票、评估 business momentum 与 potential earnings revisions |
| **3** | **Key Driver Assessment & Deep Dive Process** | 理解 **3 key drivers**，再做 deep-dive 找出在这些 driver 上的 differentiation |
| **4** | **Case Construction & Risk/Reward Assessment** | 做 bull / base / bear cases，判断风险收益吸引力 |
| **5** | **Thesis Development & Communication** | 结构化 thesis，pitch 给 PM（或 LP） |
| **6** | **Idea Monitoring & Catalyst Assessment** | 持续研究计划 + 监控 news flow，判断 idea 是否仍与初始 thesis 一致 |

> 同一 6 步在 Module 2 以 "First Principles" 形式复述 `[M2 p.99]`，并作为面试/LP 提问 "WHAT IS YOUR PROCESS?" 的标准答案 `[M2 p.102]`。

### A6.8 10% mindset `[M1 p.98]`

- 随机取 **10 只**股票，其中 **1 只**会是有趣的（天然命中率 10%）
- 学习把它筛到最有希望的 **2 只**
- 只要维持 **50% hit rate** 即可
- **seek exceptions**

### A6.9 Process & Judgment 的分层 `[M1 p.99]`

```
INFORMATION
   ↓
(INSIGHTS, PATTERN REC, DATA-DRIVEN DECISIONS, INTUITION/FEEL)
   ↓
PROCESS / JUDGMENT
   ↓
P&J creates VB  (Value Belief)
   ↓
trade execution & portfolio construction
```

### A6.10 Alpha pools `[M1 p.102, p.104]`

- **Successful fundamental investing** = **HARVESTING ALPHA POOLS**；goal: outperform on a risk-adjusted basis；identifying recurring mispricings repeatedly；buying mispriced securities `[M1 p.102]`
- **"Markets have pools of alpha that are repeatedly harvestable with a proper process & approach"** `[M1 p.104]`
- **"This is an apparent apprenticeship business that can take 5-10 years to learn. To learn it, find the right seat."** `[M1 p.104]`

### A6.11 Pareto 与扑克经济学

| 事实 | 数字 | 出处 |
|---|---|---|
| 主动管理人跑不赢指数的比例 | **75%** | `[M1 p.105]` |
| 100 个职业扑克玩家中产出全部奖金一半的人数 | **10** | `[M1 p.105]` |
| 扑克玩家在扣除 "rake" 后仍盈利的比例 | **30%** | `[M1 p.106]` |
| 终其职业生涯盈利的比例 | **<15%** | `[M1 p.106]` |

**What it takes to be in the 10%** `[M1 p.107]`：The right evolutionary wiring；top tier domain knowledge；intimate knowledge of market psychology；incredible discipline & work ethic；luck。

### A6.12 ETIK → KD → VB → EP 链条 `[M1 p.59]`

| 缩写 | 含义 |
|---|---|
| **ETIK** | Everything There Is To Know（我需要知道的一切）—— 流程 |
| **KD** | Key Drivers（关键驱动因子）—— 焦点 |
| **VB** | Value Belief（价值信念）—— "A determined Value Belief that the stock is cheap or expensive. Can be explicit or vague" |
| **EP** | Entry Point（入场点）—— "Entry Point of the trade. Execution from the investment team through trading desk, into order book" |

**流程顺序：ETIK → KD → VB → EP**

### A6.13 Process / Judgment / Execution 三分 `[M1 p.21, p.101]`

- **Investment Process** = "Rigorous, disciplined process applied the investment case"
- **Judgment** = "Judgment, pattern recognition & probabilistic thinking"
- **Execution** = 从投资团队 → trading desk → order book

---

# PART B — MODULE 2 · LIFE ON THE BUY-SIDE

## B1. GP / LP 与机构资本链条

### B1.1 角色定义 `[M2 p.5-8]`

- **GENERAL PARTNER (GP)** / **LIMITED PARTNER (LP)**：LP = "Allocators / Limited Partners"，collectively control trillions of capital on behalf of their beneficiaries

### B1.2 The Flow of Institutional Capital `[M2 p.7]`

```
FOUNDATIONS → ENDOWMENTS → PENSIONS → SOVEREIGN WEALTH → FO/HNW/RIA
        → (ALLOCATORS / LPs)
        → EQUITY INDEXES / ACTIVE EQUITY / BONDS / PRIVATE EQUITY / HEDGE FUNDS / BONDS-CREDIT
        → INSTITUTIONAL INVESTMENT PORTFOLIO
        (allocation process supported by boards & consultants)
```

### B1.3 规模数据 `[M2 p.7, p.34]`

| 指标 | 数值 |
|---|---|
| Global asset management | ≈ **$100tn** |
| US retirement market assets | **$40tn** |
| ├ State & Local DB | $6 |
| ├ Private Sector DB | $4 |
| ├ 401(k) & IRA | $22 |
| └ Other | $9 |
| Other assets | $60 |
| 开放式基金 | **$60-70tn** |
| active mutual fund industry | **$25tn+** |
| 全球受监管开放式基金 | **138k** 支 |

### B1.4 两类资金池 `[M2 p.7]`

- **Pools of small contributions**：school teacher & firefighter pensions、university endowments、RIAs
- **Pools of concentrated wealth**：sovereign wealth、philanthropic foundations、family offices、corporate treasuries / insurance float

### B1.5 The LP mindset `[M2 p.13]`

| 维度 | 立场 |
|---|---|
| **Serve beneficiaries** | goal = superior risk adjusted performance；set investment strategy at LP level |
| **"Volatility is risk"** | volatility targeting portfolios |
| **Best of breed** | allocates capital to manager；constraints applied on firm —— style drift, volatility, industry |
| **Align incentives** | "Alpha vs. beta"。**Beta is "cheap", alpha is "expensive"** |

### B1.6 Prudent Allocator Policy（4 条）`[M2 p.9]`

1. minimize risk of **permanent capital impairment**（teacher/firefighter retirements）
2. create **diversification** to build an **all-weather portfolio**
3. target **6-8%+** return，a safe inflation adjusted return above withdrawal rate
4. **minimize expenses**

**Endowment Policy 算例** `[M2 p.9]`：BOP $1,000 → Target Return $80（**8.0%**）→ Withdrawal Rate ($50)（**5.0%**）→ EOP $1,030（**3.0%**）。

---

## B2. 买方 vs. 卖方

### B2.1 角色结构 `[M2 p.15-18]`

- **BUY-SIDE: DISCRETION OVER A POOL OF INSTITUTIONAL CAPITAL**
- **LP/ALLOCATOR**：HAS CAPITAL, NEEDS RISK/ADJUSTED RETURN
- **MANAGER（Hedge Fund / PE / VC / Long Only）**：HAS EXPERTISE & HUMAN CAPITAL TO MAKE INVESTMENTS；MAKES INVESTMENTS & RECEIVES COMPENSATION

| | **BUY-SIDE** | **SELL-SIDE** |
|---|---|---|
| Revenue model | paid for investment performance | paid for advice & investment financing（lending & prime brokerage） |
| Areas | public: long-only (mutual fund), single manager hedge funds, multi-manager hedge funds；private: private equity, venture capital | investment banking, sell-side research |
| Orientation | generate risk-adjusted returns | serve the client by publishing helpful research & supporting transactions |

### B2.2 Sell-side as training ground `[M2 p.17]`

2014 Volcker Rule 禁止银行自营交易；卖方被当作 **talent filtering mechanism**；可学 modeling, corporate transactions, attention to detail。

### B2.3 Public vs Private `[M2 p.18]`

- **Public**：靠 public market cadence，hours & travel 更少；junior 协助 thesis development 流程，senior 驱动之，value lies in **idea generation & execution**
- **Private**：交易驱动的 deal identification, sourcing & asset improvement，更长工时与更多差旅

### B2.4 Institutional vs Retail `[M2 p.19]`

| | RETAIL | INSTITUTIONAL |
|---|---|---|
| Resources, dedication, skill | generally minimal | generally high |
| Approach | "chart chasers"（buying tops, selling bottoms），chasing excitement & driving bubble formation，受 psychology 与 fear/greed 驱动 | risk-adjusted & probabilistic thinkers，practice "second order" thinking，independent due diligence |
| Results | 极小比例的 retail accounts 长期跑赢 S&P 500（最好的账户往往被遗忘） | **75%+** 主动管理人跑输（但这是预期之中的），某些基金持续产生 superior risk-adjusted returns |

> **"In theory, barriers to entry in the public equity markets are low. But just because the can most often doesn't mean they should."** `[M2 p.19]`

---

## B3. 扑克类比与三种投资方法

### B3.1 扑克类比 `[M2 p.20]`

**INVESTING IS A SKILL GAME / A POKER ANALOGY**（Mike McDermott）：
- "What are they the luckiest guys in Vegas? It's a skill game, Jo."
- Poker = easy to learn, difficult to master
- Luck vs. skill = flop AA vs. consistent +EV
- **"SIMPLE, NOT EASY"**

**信息与判断的分工**：Information → **Process / due diligence**；Insight → **Judgment / wiring** `[M2 p.20]`。

### B3.2 三类投资方法 `[M2 p.21]`

| # | 方法 | 特征 | 代表 | 人才 |
|---|---|---|---|---|
| **01** | **INDEX INVESTING** | acceptance of average return at a very small net fee；"I'm not going to try, buy the basket"；不坐牌桌，零费用 | Vanguard, BlackRock | — |
| **02** | **QUANTITATIVE / SYSTEMATIC** | identify recurring anomalies；data, super-computers & advanced math；recurring patterns / super computers / behavioral mistakes & aberrations / factor harvesting | D.E. Shaw, Two Sigma, Renaissance | quantitative, technical PhD's |
| **03** | **FUNDAMENTAL** | apply analysis of company fundamentals to identify equity mispricing；dependent on a more accurate view / a bet against "wisdom of the crowds" | Tiger, Capital Group, Citadel/P72/Balyasny | fundamental financial analysts |

---

## B4. 三种投资形态（Three Flavors of Ice Cream）

### B4.1 对比表 `[M2 p.29, p.30]`

| | **LONG ONLY** | **SINGLE MANAGER** | **MULTI-MANAGER** |
|---|---|---|---|
| **持有期** | 一般 **1-5 年** | 一般 **6-24 个月**（有时更长/更短） | 一般每年换手 **4-12+ 次**（1-3 个月持有期） |
| **关注点** | 深度理解业务与行业，长期视角，"think like an owner"；长期 FCF/share 增长 —— **quality & duration of growth 是关键** | 结构性变化与 business momentum inflection；deep research / run towards misunderstanding；long book 可类似 LO，short 侧差异大 | Adaptive, some trading, some investing，"bet mix"；追求"steep part of the return curve"，目标是持续产生 P&L；earnings cycle 关键 |
| **其他** | 一般最小化关注 factor exposures；一般不用杠杆 | Risk/reward 视角，**long capital 的 IRR 门槛 20%+**；一般适度加杠杆 **150-250% gross** | Alpha isolation process（factor-based idio 有限风险模型）；**beta neutral、factor constrained wrapper**；高杠杆 **400-600%+ gross** |

### B4.2 理解三种形态的 6 个维度 `[M2 p.30]`

各玩家激励不同；**"Who owns the stock"**；**"Incremental price setter"**；结构不同；index measurement（net, gross, leverage, alpha, beta, volatility）；career purposes。

**Investors vs Traders 的区分维度** `[M2 p.31]`：Time horizon / duration；Net exposures；Use of leverage。

### B4.3 风险 / 敞口包络（Risk Envelope）

**风险包络表** `[M2 p.74]`：

| | Equity | Leverage | Gross | Gross % | Longs | Shorts | Net | Net % |
|---|---|---|---|---|---|---|---|---|
| Long Only | $100 | $0 | $100 | 100% | $100 | $0 | $100 | 100% |
| 50% Net | $100 | $150 | $250 | 250% | $150 | $100 | $50 | 50% |
| Mkt Neutral | $100 | $300 | $400 | 400% | $200 | $200 | $0 | 0% |

**市场下跌 20% 时的表现** `[M2 p.75]`：

| | Gross 损失 | Equity 影响 |
|---|---|---|
| Long Only（$20） | (20%) | **(20%)** |
| 50% Net（$30，$20 shorts） | (4%) | **(10%)** |
| Market Neutral（$40，$40 shorts） | 0% | **0%** |

> **"Market move × net exposure = predicted fund performance"** `[M2 p.75]`
> hedge funds 在牛市中传统上跑输 S&P 500。

### B4.4 Long-Short spread 是核心 `[M2 p.76-78]`

Longs 10.0%、Shorts 5.0%、**Spread 5.0%** → Return on Gross 2.5% → Return on Equity：

| Gross | Return on Equity |
|---|---|
| 200 gross | 5.0% |
| 300 gross | 7.5% |
| 400 gross | 10.0% |
| 500 gross | 12.5% |

> **"Dirty secret: real P&L generation on the short side is difficult. It's more a spread game, with real P&L generated on longs."** `[M2 p.76]`

**Portfolio wedge** `[M2 p.77]`：Longs P/E 15.0x、EPS Growth 15.0%、**IRR Potential 20.0%**；Shorts P/E 25.0x、EPS Growth 5.0%、**IRR Potential 5.0%**；**Portfolio Spread 15.0%**。
> "Use this to think: what sort of stock/company can IRR 20%+? What short of short can IRR 5%? Assuming baseline 10% market growth."

**三种形态的收益分解** `[M2 p.78]`：Longs 10.0% / Shorts 5.0% → LO $10/$0/$10（10.0%、10.0%）；50% Net $15/($5)/$10（4.0%、10.0%）；Market Neutral $20/($10)/$10（2.0%、10.0%）。

**Sharpe 对照** `[M2 p.59, p.79]`：

| | Return | Risk | Sharpe |
|---|---|---|---|
| Long Only | 10.0% | 20.0% | **0.5x** |
| 50% Net | 10.0% | 10.0% | **1.0x** |
| Market Neutral | 10.0% | 5.0% | **2.0x** |

**Sharpe ratio = return / risk (standard deviation)** `[M2 p.10]`。

### B4.5 典型 Single Manager 组合构建 `[M2 p.55]`

| 项目 | 金额 | 比例 |
|---|---|---|
| Investor Capital (Equity) | $1,000 | |
| Leverage | $1,500 | |
| **Gross Exposure** | $2,500 | **250%** |
| LMV | $1,500 | |
| SMV | ($1,000) | |
| **Net Exposure** | $500 | **50%** |
| Return on LMV | $210 | 14.0% |
| Return on SMV | ($60) | 6.0% |
| Net P&L | $150 | 8.0% |
| **% return on gross** | | **6.0%** |
| **% return on equity** | | **15.0%** |

**定义**：
- **GROSS EXPOSURE = Equity Plus Leverage expressed over Investor Equity**
- **NET EXPOSURE = LMV less SMV expressed over Investor Equity**

### B4.6 杠杆的本质 `[M2 p.56-57]`

许多底层策略只产出 tepid mid-single-digit returns（低波动）；**8% long/short spread** 虽是非常好的 alpha，但只产生 **6% on gross**；**用 thoughtful leverage deployment，8% long-short spread 变成 15% return to investor equity**。

**房贷类比**：20% appreciation in 80% LTV home = 100% return to equity；杠杆双向放大（leverage cuts both ways）。

### B4.7 Alpha vs Beta `[M2 p.58]`

Market Return 10.0%；Hedge Fund Net 50.0% → Hedge Fund Return, Beta 5.0%；若 Hedge Fund Return 10.0% → **Hedge Fund Alpha 5.0%**。
Beta 是 market exposure 解释的收益（"free"）；Alpha 高度值钱。

### B4.8 Factors & Idio `[M2 p.60]`

**约 3/4 的个股当日波动并非 idiosyncratic**；bulk 由 factors 驱动（beta, value, growth, leverage, size, SI, momentum）；factors 常成为 hidden macro bets。

### B4.9 Long tail `[M2 p.61]`

Total HF AUM $4,534,000；Number of HFs 12,000；Average HF AUM $378；top 100 主导行业，但存在 **$50-$250m 的长尾**，可作为好生意与好雇主。

### B4.10 Institutional vs Boutique `[M2 p.62]`

Industrial vs artisanal；**12,000+ in US alone**；"More HF than burger kings"；barriers to entry very low。

### B4.11 商业模式与费用

**Single manager 利润池** `[M2 p.63]`：model 可 scale 很好；business 对业绩脆弱，但 **nearly infinite incremental ROIC**。
$250m AUM、20% return → $50 return → 20% carry = $10 → PM share 50% = $5、Team Pool $5；$2.5bn AUM → PM Comp $50、Team Pool $50。

**2 & 20 Model** `[M2 p.25, p.54]`：

```
Equity Invested                      $1,000
Investment Performance                $100   (gross 10.0%)
Management Fee                        ($20)  2.0%
Performance Fee                       ($20)  20.0%
Gross Result                         $1,100  (10.0%)
Net Result                           $1,060  (net 6.0%)
Effective Fee Load                              4.0%
```
> **"Hedge fund is a compensation structure"**

**LO: A Simple Model** `[M2 p.25, p.38]`：Pool of Capital $10,000；Management Fee 0.75% = $75；Post Fee Capital $9,925；**Return to Match 10% Market = 10.83%**。

**MM 的费用结构** `[M2 p.69]`：Pods 是极高费率的载体（**4-5% of capital**），所有 research expenses 及 PM payouts 直接 pass through 给 LP。

**Multi-Manager 典型结构** `[M2 p.64, p.66]`：Investor Capital $3,000；Leverage $12,000；Gross Capital $15,000（**500%**）；Beta-Adjusted LMV $7,500；Beta-Adj SMV ($7,500)；**Net Exposure $0**。

**10 个 pod 分配表** `[M2 p.66]`：

| Pods | Gross | % Sizing | % Vol | $ Vol |
|---|---|---|---|---|
| Pod 1 | $3,000 | 20.0% | 2.8% | $85 |
| Pod 2-3 | $2,250 | 15.0% | 3.1% | $70 |
| Pod 4-5 | $1,500 | 10.0% | 3.3% | $50 |
| Pod 6-7 | $1,125 | 7.5% | 3.1% | $35 |
| Pod 8-10 | $750 | 5.0% | 3.3% | $25 |
| **合计** | **$15,000** | | **3.1%** | **$470** |

MM 费用与净 P&L `[M2 p.69]`：Target Sharpe on Gross 1.0x；Volatility Deployed $470；Gross P&L $470；Pass Through Expenses, Net $135（4.5%）；**Net P&L Generated $335；% return to equity 11.2%**。

**MM 收益算例** `[M2 p.70]`：GMV $1,500；Beta-Adj LMV $750；Beta-Adj SMV ($750)；Net $0；Long Book P&L $75（10.0%）；Short Book P&L ($15)（2.0%）；Total P&L $60；**Long-Short Spread (~Alpha) 8.0%；Return on Gross 4.0%；Return on Underlying Equity 20.0%**。
> **"4% return on gross in this example is actually 8% long-short spread (~alpha) which is DIFFICULT and IMPRESSIVE"**
> Individual PMs target LSD/MSD、有时 HSD；MSD returns 加上杠杆可变成 20%+。

### B4.12 MM 的崛起与市场影响 `[M2 p.71-73]`

- 2022 年 MM firms up **5-30%** 而 SM firms down
- MM funds 从 **$92bn 增至 $311bn（2010-2022）**；$350bn vs $45tn US equity market
- Multi-PMs 持有 **27% of US hedge fund equities**，HF AUM **<10%** of US equity market cap
- MM 多空持仓 ≈ **3-4%** of US equity market cap；但因高杠杆与高换手，MM 可能驱动 **15-25% 的日成交量**
- Illustrative：$45,000bn 市值、$350bn AUM、$1,750bn gross at 5x、$1,225bn 估计权益敞口；1.2x 全市场换手 vs **8.0x MM 换手**；$54,000bn 全市场换手 vs $9,800bn MM 换手 = **18.1% MM stock impact**

### B4.13 下行保护 `[M2 p.82]`

YTD '22 Returns：S&P 500 (25.0%)；Tiger Global (50.0%)；Citadel 29.0%。

### B4.14 费用去了哪里 `[M2 p.83-84]`

**"5% ALPHA, WHERE DOES IT END UP?"**
- Cao, Chen study 显示 HFs 是 good stock pickers
- Goldman Sachs VIP vs high short interest 显示 alpha（though increasingly "crashy"）
- **但 4-5% 的高费载意味着 outperformance 归 GP 而非 LP**
- **Hedge Fund Mirage (Lack)** 显示大部分 alpha 归 GP
- 净基础：hedge funds 交付 subdued (NET) alpha，但为渴望 8% 回报的 LP 提供 high-Sharpe 产品

### B4.15 零和 alpha pool 与扑克经济学 `[M2 p.11]`

8 人各 buy-in $500，共 $4,000：

| Player | Buy-In | Result | Result |
|---|---|---|---|
| 1 | $500 | $1,500 | $2,000 |
| 2 | $500 | $750 | $1,250 |
| 3 | $500 | $250 | $750 |
| 4-8 | $500 | ($500) | $0 |
| **Total** | **$4,000** | **$0** | **$4,000** |

- **Beta is not zero-sum**（集体股票长期回报约 **~10%**）
- **像 poker "rake"，费用把主动管理变成 less than a zero-sum game**
- Hedge fund 行业成熟化已创造一个 **"zero sum" alpha pool**

### B4.16 风格与大师业绩 `[M2 p.27-28]`

| 风格 | 描述 | 追踪记录 |
|---|---|---|
| Robertson / Tiger | Growth at a reasonable price；Winners vs. losers | Julian Robertson, Tiger Management **31.7%** |
| Cohen | Active trader；Catalyst & events | Steve Cohen, SAC / Point 72 **30.0%** |
| Druckenmiller | Directional & concentrated；Macro-influenced | Stan Druckenmiller, Various **30.0%** |
| Lynch | Growth & multi-baggers；Secular themes | Peter Lynch, Fidelity Magellan **29.2%** |
| Buffett | Business quality & durability；Growth at a reasonable price | Warren Buffett, Berkshire Hathaway **20.8%** |
| | | **Average 28.3%** |

> **"Many ways to skin the cat. No one specific style has been the most successful"**

**Style Investing 4 要素**：Investment Style；Investment Focus；Commonalities Amongst All；以及 **"Think for yourself: if you agree with everything I show you, you aren't thinking critically enough"**

**警示** `[M2 p.28]`：**"My job is not to say 'this is how to invest'… Take what fits for you, leave what doesn't"**

---

## B5. Long Only 101 `[M2 p.32-45]`

| 维度 | 要点 |
|---|---|
| **Capital source** | primarily defined benefit (pension) 或 defined contribution (401k)；retail capital via mutual fund complex；institutional capital via direct allocation |
| **Business model** | typically a simple revenue model: % fee on AUM；larger firms 覆盖多资产类别与多策略 |
| **Investment approach** | style-box oriented；因 position sizes 与 retirement mandate 通常 duration 更长 |
| **Team structures** | 多个组合、按 style 划分；**较大的基金倾向 specialist**（sector coverage approach，"sell-side" 式覆盖常见）；**较小的基金倾向 generalist**（style funds 如 Value）`[M2 p.37]` |
| **Challenges** | Indexes are hard to beat given concentration of a handful of winners；**"75bps is not an immaterial fee hurdle"** `[M2 p.38]` |
| **结构性问题** | rise of indexation；near zero cost index；fee compression |
| **Career path** | Pros：longer development curve、stable capital、steadier compensation；Cons：structural headwinds、can be **10 甚至 15 年**才到 PM seat、less pay for performance `[M2 p.43]` |
| **其他形态** | RIA、Internal Sovereign Wealth、Internal Pension、Internal Family Office、Smaller long-only firms `[M2 p.44]` |
| **Summary** | some difficult structural headwinds；but a wonderful business for top decile performers（sticky capital, pro-cyclical with performance；long-term, more "academic" environment）`[M2 p.45]` |

**TROW vs BEN 作为一门生意** `[M2 p.42]`：

| 指标 | TROW | BEN |
|---|---|---|
| MCAP | $14,070 | $24,521 |
| Enterprise Value | $22,623 | $23,387 |
| NTM P/E | 10.1x | 14.7x |
| Trailing 10yr S&P Avg | (15.3%) | (5.1%) |
| Total Revenue | $6,474 | $6,488 |
| T5Y Revenue CAGR | (0.1%) | 1.9% |
| T5Y EBITDA Margin | 35.4% | 44.1% |
| T5Y FCF Margin | 17.8% | 32.3% |
| T5Y EBITDA ROIC | 7.9% | 28.7% |

画像：large enterprises ($20b+)、highly profitable、capital efficient、minimal/no top-line growth、low multiple (low growth)、stocks have underperformed。

---

## B6. Hedge Fund 101 `[M2 p.46-84]`

| 维度 | 要点 |
|---|---|
| **两种形态** | **SINGLE MANAGER (SM)** = Tiger Cub / Tiger style、Activist / Event、Value focused、Sector focused、Other (credit, macro, short only) `[M2 p.49]`；**MULTI-MANAGER (MM)** = multi-strat, platform, multi-PM, "pod" `[M2 p.47, p.50]` |
| **Capital trends** | AUM 自 2007 翻倍；增量增长来自 MM 端 `[M2 p.51]` |
| **Performance** | lower net exposures → hedge funds rarely keep up with a bull market，但通常在下跌市更好地保护资本 `[M2 p.52]` |
| **Legal structures** | GP、LP、performance fee、strategy flexibility（use of leverage；flexible net exposures）`[M2 p.53]` |
| **MM 的崛起** | 2022 年 MM firms up 5-30% 而 SM firms down；MM funds $92bn → $311bn（2010-2022）`[M2 p.71-73]` |

---

## B7. 研究流程纪律：PM 的一天、责任栈与工时基准

### B7.1 A Day in the Life of a PM `[M2 p.86]`

| 时段 | 动作 |
|---|---|
| 6:00am | 起床（在恐慌中） |
| 6:00-6:15 | sift through **~500 e-mails** looking for signal（pain triage） |
| 6:15-6:45 | treadmill / meditation / coffee |
| 7:30-8:30 | digest overnight news（视 "season" 而定；真安静就做 "actual work"） |
| 8:30-9:00 | morning team huddle |
| 9:30-10:00 | watch the open、set VWAPs |
| 10:00-12:00 / 12:30-3:30 / 4:30-6:00 | do "actual work"（research, calls w/ companies, calls w/ sell-side, model reviews w/ analysts） |
| 12:00 | lunch（1-2x/week NDR 或 sell-side lunch） |
| 3:30-4:00 | watch the close |
| 6:45-7:30 | family |
| 7:30-9:00 | read on iPad |

**时间账** `[M2 p.86]`：**6.5 Actual Research Work - Best Case Scenario；2.5 Reading News / Checking E-mail**。
> "Often a PM has surprisingly minimal time for focused, intentional thesis work"
> **"Best case" 5-7 小时/天，通常 1-3 小时更常见**；难以应对**需要 40-60 小时专注工作的严谨 thesis**。

### B7.2 PM responsibility stack `[M2 p.87]`

Raising capital / communicating with investors；Finance & operations；Legal & compliance；**Running the business!**

### B7.3 工时基准：Thesis Development Work Stack — Standing Start `[M2 p.90]`

**从零开始（standing start）的尽调工时表：**

| 项目 | 小时 |
|---|---|
| Read Public Filings | 2 |
| Read Earnings Transcripts | 4 |
| Read Conference Transcripts | 2 |
| Investor Conference Transcript & Deck | 2 |
| Read Sell-Side Research | 5 |
| **Sample Reading Stack** | **15** |
| Build Baseline Financial Model | 8 |
| **Standard: Baseload Due Diligence** | **23** |
| Run Targeted Analytics on Key Drivers | 8 |
| Conduct Expectations Work | 3 |
| Conduct Valuation Work | 3 |
| Conduct Industry Due Diligence Calls | 12 |
| Conduct Calls w/ Sell-Side | 4 |
| Identify & Understand Narrative | 2 |
| Prep & Call w/ Management | 3 |
| Develop Bull & Base Cases | 2 |
| Construct Written Thesis for Presentation | 5 |
| **Custom: Thesis Development Work** | **42** |
| Standard: Baseload Due Diligence | 23 |
| Custom: Thesis Development Work | 42 |
| **Sample From Scratch Due Diligence** | **65** |

**三档基准**：
- **Baseload（标准底座）= 23 小时**
- **Thesis Development（定制论点工作）= 42 小时**
- **From Scratch Total（从零起步）= 65 小时**

**Deep dive（结构化深挖）总时长 = 60-90 小时，即 4-6 个工作日** `[M3 p.60]`（14 步清单见 `02-thesis-development.md`）。
换算关系：23h baseload + 42h thesis = **65h standing start**；把 reading stack 换成带时效要求的 targeted analytics 后，deep dive 落在 **60-90 小时 / 4-6 天**区间。

### B7.4 覆盖能力上限（Coverage Capacity）

| 覆盖模式 | 覆盖只数 | 说明 |
|---|---|---|
| Generalist / No Coverage | — | 分散 idea 方式，多行业；无 "power alleys"；minimal process installed base `[M2 p.90]` |
| Specialist / Loose Coverage | **100-150 names** | 覆盖深度不一；常见于 $500m-$10bn 公司、投资团队 >10 人、Tiger Cubs `[M3 p.9]` |
| Specialist / Tight Coverage | **30-60 stocks** | "almost in a 'sell-side' approach"；names "chamber ready"；highest installed base `[M3 p.9]` |

> 覆盖能力的本质约束：**installed base** —— "The more stones you turn over, the larger your rolodex of ideas becomes"；**"Every idea isn't coming from a standing start"** `[M3 p.30]`。

**Idea rolodex 与 idea 节奏** `[M3 p.13]`：

| 团队 | 计算 | Ideas 总量 | Team | Per Person | Per Month |
|---|---|---|---|---|---|
| **Tiger 团队** | Long 15 × 1.5x = 23；Shorts 30 × 2.5x = 75 | **98** | 5 | **20** | **2** |
| **Pod 团队** | Long 50 × 2.5x = 125；Shorts 100 × 4.5x = 450 | **575** | 8 | **72** | **6** |

> "To be successful, your idea cadence must meet the needs of the portfolio"

### B7.5 Crafting Your Process `[M2 p.102-104]`

**Common interview (or LP question)**: "WHAT IS YOUR PROCESS?"
→ **"I HAVE A 6-STEP PROCESS FOR LOOKING AT AN IDEA"**（逐条：initial analysis & opportunity assessment；business analysis & model construction；key driver assessment & deep dive process；case construction & risk/reward assessment；thesis development & communication；idea monitoring & catalyst assessment）

交付形式：word document 或 PowerPoint 都可。

> **"if this person can't articulate a process clearly, there is no process!!!"** `[M2 p.103]`

---

## B8. 分析师的角色、能力与工具

### B8.1 Role of the Analyst `[M2 p.88]`

**"EXTRA SET OF HANDS"**；IDEA PROCESSOR；IDEA GENERATOR；COVERAGE LEAD；RESIDENT INDUSTRY EXPERT；RESIDENT COMPANY EXPERT。

### B8.2 团队结构与覆盖 `[M2 p.89]`

multi-manager (pod) firms 同样以 sector 划分覆盖；very people intensive；artisanal process。
示例：Sr. Analyst: Pharma & LC Biotech / Medtech & Tools 覆盖清单（表列 **40 只**，含 Ticker、Name、$MCAP、$ADV、Subsector）：JNJ $386,604/$344/Pharma、MRK $199,379/$257/Pharma、AMGN $144,163/$248/Biotech、VRTX $72,442/$148/Biotech…

**Generalist / no coverage** `[M2 p.90]`：scattershot idea approach；common in smaller firms 或 style-based investors（如 value investors）；early-career analyst 无 "power alleys"；minimal process installed base 可供 leverage。

### B8.3 Pitching a stock：房间里需要什么 `[M2 p.91]`

| 类别 | 内容 |
|---|---|
| **SKILLS** | foundational skills: accounting, valuation, business analysis；buy-side skills: communication, language, concepts |
| **EXPERTISE** | industry & company；exhaustive knowledge to answer any question posed |
| **INFORMATION** | baseline information；key information collected |
| **INSIGHT** | what the market has wrong & what will resolve the misunderstanding；view as to why this opportunity is compelling |

### B8.4 工具箱 `[M2 p.92]`

| 类别 | 工具 |
|---|---|
| **ANALYST TOOLS** | Accounting & Excel、Corporate Finance、**7th Grade Math**、Buy-Side Frameworks、Thesis Development Tools |
| **EXTERNAL TOOLS** | Bloomberg / FactSet、Sell-Side、Alt Data、Corporate Relationship、Experts & Consultants |
| **MINDSET TOOLS** | Hunger & Passion To Win、Journalistic Disposition、Comfort With Uncertainty、Can Deal With Being Wrong、Humility & Adaptation |

### B8.5 专长的三个维度 `[M2 p.93]`

| 维度 | 内容 |
|---|---|
| **FRAMEWORKS & TOOLS** | Foundations: accounting, corporate finance, equity markets；Buy-side concepts & frameworks: equity stub, incremental margin, buyback yield, unit economics 等；Knowledge of other buy-side players |
| **INDUSTRY** | Growth drivers；Competitive dynamics；Technological trends；Secular & cyclical trends；Supply chains；Capital cycles |
| **COMPANIES** | Business models；Business quality；Business strategy；Management quality；Key drivers；Product quality |

### B8.6 必备的 8 项能力 `[M2 p.94]`

1. Ability to analyze a business
2. Ability to grasp a stock's key drivers
3. Ability to understand what is discounted in stock
4. Ability to develop a differentiated view
5. Ability to accurately assess value
6. Ability to see investment opportunities clearly
7. Ability to compellingly communicate a thesis
8. Ability to dispassionately monitor & adjust

### B8.7 Universal tools `[M2 p.95]`

Analyze businesses；Build (or at least use) models；Research key drivers；Value stocks；Face earnings season；Analyze management；Generate ideas；Communicate your ideas；Monitor catalysts。

### B8.8 Pattern recognition idea 模板 `[M2 p.108]`

| Potential Longs | Potential Shorts | High Odds of Mispricing |
|---|---|---|
| Growth durability bets in secular winner | Persistent pricing pressure in biz model | Recent or broken IPOs |
| Incremental margins well above base margins | Leaky bucket business model / bolt-ons to fill hole | Corporate structure change - divestitures, spins, etc |
| New mgmt team with margin expansion plan | "Where's the cash" accounting games | Post-bankruptcy organization |
| Organic growth acceleration ahead | Secular threat from technology | Imminent regulatory change |
| M&A target in consolidating industries | New competitor in slow growing market | New product launch - too much hope or not enough? |
| Dislocation, potential over-reaction to small issue | Consensus long with risk of earnings miss | Less liquid stocks / under $5m a day |
| "Toll both trade" - hold through temporary weakness | Stock with past "freak outs", but current waters calm | Recent major M&A |

### B8.9 A+ Analyst 的解剖 `[M2 p.115]`

Analytics；Communication；Creativity；Tenacity；Self-containment；Common sense；Passion & work ethic；**X-factor (nose for money, intuition)**。

---

## B9. 买方心态（Buy-Side Mentality）

### B9.1 八条原则 `[M2 p.106]`

| 原则 | 第一性陈述 |
|---|---|
| **JOURNALISTIC DISPOSITION** | "I will practice objective, dispassionate, rigorous due diligence" |
| **CREATIVITY & PATTERN RECOGNITION** | "I will think differently & creatively to identify investment opportunities" |
| **ESSENTIAL THINKING** | "I focus on what matters and won't miss the forest for the trees" |
| **PROBABILISTIC THINKING** | "I don't know for sure, so I am seeking asymmetry & expected value" |
| **HUMILITY, PARANOIA & SKEPTICISM** | "I know bad things can happen to equities, so I am constantly on the lookout for what can go wrong" |
| **ADAPTIVE CONVICTION** | "I will shift my conviction as the fact pattern shifts" |
| **SECOND ORDER THINKING** | "I am seeking a variant perception, focused on a differentiated viewpoint" |
| **EARNED CONFIDENCE** | "I have faith in a winning blueprint despite near-term results" |

### B9.2 十二条买方心法 `[M1 p.78]`

1. **Emotional detachment**
2. **Start with what can go wrong** —— "First be comfortable with the downside case, and if that is modest, the upside case is free"
3. **Keep it simple**（2-3 key points）
4. **Develop conviction but make it data-dependent**
5. **Don't compound your mistakes** —— "The best sale can be the first one"；thesis creep is a killer
6. **Be aware of biases**（Thinking Fast & Slow, Kahneman）
7. **Embrace a wide range of outcomes**
8. **Earnestly seek out contradictory views**
9. **Seek today's opportunity – do not live in the past**
10. **Have faith in a winning blueprint**
11. **Become a master of the detail**
12. **Know how to distill it down to what matters most**

### B9.3 概率思维与 EV `[M2 p.111]`

**EV Example**：Stock Price $100；Reward Case $140（+40.0%）；Risk Case $80（−20.0%）；Reward Probability 50%；Risk Probability 50%；**Probability Adjusted Price $110；Expected Value $10**。

> "Best traders right 52% of the time"；Blackjack house edge：by the book 2% negative edge，counting cards 1% positive edge；**Positive expected value multiple many times**

### B9.4 三条心态细则 `[M2 p.112-114]`

**HUMILITY, PARANOIA & SKEPTICISM 5 条** `[M2 p.112]`：
1. Start with what can go wrong
2. Don't compound your mistakes（thesis creep is a killer）
3. Be aware of biases - others' and your own
4. Embrace a wide range of outcomes
5. Earnestly seek out contradictory views

**ADAPTIVE CONVICTION** `[M2 p.113]`：**"Develop your conviction based on research nuggets. If these nuggets turn, change your mind"**

**EARNED CONFIDENCE** `[M2 p.114]`：**"Keep chopping wood. You can do everything right on the input and still get the wrong outcome. Do not let that deter you from a disciplined process"**

---

# 规则与阈值（可测试的硬数字）

## R1. 估值与资本成本

| 规则 | 数字 | 出处 |
|---|---|---|
| DCF 101 | 预测 5 年 FCF → 对第 6 年套 terminal multiple → 按 WACC 折现 | `[M1 p.9]` |
| Cost of Equity | **Rf + Beta × ERP** | `[M1 p.10]` |
| WACC | **Ke × E/V + Kd_after_tax × D/V** | `[M1 p.10]` |
| 敏感性 | **Discount rate 每变动 200bps → Implied P/E 修正约 15%** | `[M1 p.46]` |
| Implied P/E 反查 | 4%→**55.0x**；7%→27.0x；10%→16.0x；11%→11.0x；12%→**8.0x** | `[M1 p.10]` |
| Equity duration | 20x P/E 股票 DCF 价值：**0-5 年 14%、5-15 年 26%、15 年以后 60%** | `[M1 p.40]` |
| 标准股票折现年限 | **25-35 年** | `[M1 p.16]` |
| NFLX 型外推风险 | 增量利润率 41.1% → 4.5%，Avg P/E 59.6x → 24.9x | `[M1 p.47]` |

## R2. 市场结构与判断阈值

| 规则 | 数字 | 出处 |
|---|---|---|
| 跳空与资金流 | 20% 跳空不必然需要大额资金流；可能是 buyer's strike / seller's strike | `[M1 p.20]` |
| 基本面解释力 | Company-specific fundamentals 只解释近端波动的 **<50%** | `[M1 p.67]` |
| CFO 可见度 | FCF 可见度只有 **6-18 个月** | `[M1 p.44]` |
| Jelly-bean 实验 | 850 颗 → 全班估计 871（**2.5% error**），仅 **1/56** 人更准 | `[M1 p.35]` |
| 一次性 EPS 资本化 | $25 → $70（**+180%**）→ $25（**−64.3%**） | `[M1 p.50]` |

## R3. Alpha 定义与度量

| 规则 | 数字 | 出处 |
|---|---|---|
| Alpha | 总回报 − beta 回报 | `[M1 p.85-87]` |
| Expectations gap | **MARKET VIEW − INTERNAL VIEW** | `[M1 p.91]` |
| Alpha load | **PRICE vs VALUE GAP** | `[M1 p.93]` |
| Idea 命中率 | 10 → 1 的天然命中率；过滤到 2 只需维持 **50% hit rate** | `[M1 p.98]` |
| 完整投资流程 | **6 步** | `[M1 p.97]` |
| 每个 idea 必须确定 | **3 key drivers** | `[M1 p.97]` |
| Pareto 基准 | **75%** 主动管理人跑输指数；扑克 rake 后仅 **30%** 盈利，终生 **<15%** 盈利 | `[M1 p.105-106]` |

## R4. LP / 资本约束

| 规则 | 数字 | 出处 |
|---|---|---|
| Prudent allocator 目标 | **6-8%** 回报（通胀调整后高于提取率） | `[M1 p.81]` |
| Endowment 算例 | BOP $1,000 → +$80 (8.0%) − $50 withdrawal (5.0%) = EOP $1,030 (3.0%) | `[M1 p.81]` |
| 机构配置流程 | **3 步** | `[M2 p.12]` |

## R5. 买方经济学与敞口

| 规则 | 数字 | 出处 |
|---|---|---|
| 集体股票长期回报 | **~10%**（beta 不是零和） | `[M2 p.11]` |
| Alpha pool | **零和**；费用（rake）把主动管理变成小于零和的博弈 | `[M2 p.11, p.84]` |
| 2 & 20 的有效费率 | 2% 管理费 + 20% carry，在 10% gross 回报年份 → **约 4%** effective fee load | `[M2 p.54]` |
| MM pod 层面费率 | **4-5% of capital** | `[M2 p.69]` |
| 净结果 | $1,000 → $1,060（**net 6.0%**），effective fee load **4.0%** | `[M2 p.25, p.54]` |
| LO 追平市场的门槛 | 0.75% 费率后需 **10.83%** 回报才能匹配 10% 市场 | `[M2 p.38]` |
| **Market move × net exposure** | = **predicted fund performance** | `[M2 p.75]` |
| Gross / Net 定义 | Gross = (Equity + Leverage) / Investor Equity；Net = (LMV − SMV) / Investor Equity | `[M2 p.55]` |
| SM 典型 | **250% gross / 50% net** → 8% long-short spread → 6% on gross → **15% on equity** | `[M2 p.56]` |
| MM 典型 | **500% gross / 0% net**；10 pods；目标 Sharpe on gross **1.0x**；net P&L $335 → **11.2% return to equity** | `[M2 p.66, p.69]` |
| Long-short spread 放大 | spread 5% → 200 gross **5.0%** / 300 gross **7.5%** / 400 gross **10.0%** / 500 gross **12.5%** | `[M2 p.76]` |
| Portfolio wedge IRR | longs **20%**、shorts **5%**，spread **15%** | `[M2 p.77]` |
| Sharpe | LO **0.5x** / 50% Net **1.0x** / Market Neutral **2.0x** | `[M2 p.59, p.79]` |
| MM 市场影响 | 持 US hedge fund equities **27%**；HF AUM **<10%** US equity market cap；持仓 ≈ **3-4%** 市值但驱动 **15-25%** 日成交量；illustrative **18.1%** | `[M2 p.73]` |
| 形态阈值 | SM long capital IRR 门槛 **20%+**；SM 杠杆 **150-250% gross**；MM **400-600%+ gross**；MM 年换手 **4-12+ 次** | `[M2 p.29]` |

## R6. 工时与流程纪律

| 规则 | 数字 | 出处 |
|---|---|---|
| Baseload 尽调 | **23 小时** | `[M2 p.90]` |
| Thesis Development 工作 | **42 小时** | `[M2 p.90]` |
| 从零起步总尽调 | **65 小时** | `[M2 p.90]` |
| PM 实际工作时间 | "Best case" **5-7 小时/天**，通常 **1-3 小时**；严谨 thesis 需 **40-60 小时**专注 | `[M2 p.86]` |
| 流程表达 | 6 步；说不出 process = 没有 process | `[M2 p.99, p.103]` |
| 概率思维 | EV = 概率加权价格 − 现价；例 $110 − $100 = **$10 EV** | `[M2 p.111]` |

---

# Checklists & 模板

## C1. Reading stack（阅读清单）`[M1 p.56, p.61]` `[M2 p.90]`

- SEC Filings：**10-K, 10-Q, 8-K/PRs, prospectus, proxy**
- Earnings calls
- Sell-side research
- Investor conference events（presentation & transcript）
- Investor days（presentation & transcript）

## C2. 每日信息处理三步 `[M1 p.62]`

1. **distillation**
2. **signal vs. noise**
3. **contextualization & updating view** of value creation trajectory & degree of misunderstanding

## C3. Earnings-day 3 关键问题 `[M1 p.65]`

1. **3 key drivers 加速还是减速？**
2. **beat 还是 miss consensus？**
3. **指引上调 / 下调 / 不变？**

## C4. 行业专精 10 步 `[M1 p.61]` `[M2 p.25]`

见 A5.3(a)：读行业 primer → "Sector 101" → 行业杂志 → 行业顾问 → 龙头公司 → 历史失败案例 → **行业 aggregate P&L/BS/CF** → 非卖方会议 → 卖方会议 → 建立网络与权威地位。

## C5. 优势来源清单 `[M1 p.55]`

- Information & insight leads to better pricing
- Market incentives for enforcing efficiency
- Mosaic approach to information

## C6. Alpha buckets 9 类 `[M1 p.89]`

见 A6.4。

## C7. 股票变便宜的 7 个原因 `[M1 p.88]`

见 A6.3。

## C8. 投资流程 6 步 checklist `[M1 p.97]` `[M2 p.99, p.102]`

见 A6.7。

## C9. Buy-side mindset 12 条 `[M1 p.78]`

见 B9.2。

## C10. Performance measurement 五项 `[M1 p.83]`

Sharpe；Sortino；Annual cycle；**2 & 20**；Peer relative。

## C11. 示例模型结构 `[M1 p.46]`（Sample Business）

Revenue → % yoy → Operating Profit → % margin → bps yoy → % yoy → Tax Rate → NOPAT → Interest Expense → Pre-Tax Income → Tax Expense → Net Income → Diluted Shares → Diluted EPS → % yoy

**顶部**：EV → Less Net Debt → Market Cap → Diluted Shares → Price → EPS → P/E

## C12. 分析师 8 项能力自检 `[M2 p.94]`

见 B8.6。

---

# Common mistakes / pitfalls

| # | 错误 | 纠正 | 出处 |
|---|---|---|---|
| 1 | **把市场当作有效（efficient）** | EMH 只是 tenuous assertion；"Because it's hard, markets are efficient" 是循环论证 | `[M1 p.37]` |
| 2 | **只看第一层信息** | 信息扩散不均且需要 effort & expense；投资者在 wiring 与 skill 上差异巨大；资本带 mandate，"volatility is risk"，"style creep is death" | `[M1 p.54]` |
| 3 | **把市值波动等同于基本面** | short-term 波动常由 forced/emotional/non-fundamental sellers（ETF flows）、scared sellers 造成；不可用单年结果给好生意减值 | `[M1 p.20, p.44-45]` |
| 4 | **把短期外推当基本面** | 市场外推是因为 no better way to forecast years 2-40；一次性 EPS 会被错误资本化；COVID 类加速是否 durable 未经验证 | `[M1 p.46-50]` |
| 5 | **无流程依赖 "hunch"** | hubristic position 依赖 rigorous, repeatable process；bar 极高 | `[M1 p.58]` |
| 6 | **忽视 CapTable / 稀释** | allocation is not benevolent，$500m 增量资本需要 expected return | `[M1 p.12-13]` |
| 7 | **Thesis creep** | "The best sale can be the first one"；Quickly admitting "we got it wrong" 可以是最好的决策 | `[M1 p.78]` |
| 8 | **复合自己的错误 / 只谈上行不谈下行** | "First be comfortable with the downside case" | `[M1 p.78]` |
| 9 | **追逐噪音与共识** | retail "chart chasers"；忽略 contrary views | `[M1 p.76-78]` |
| 10 | **忽视资本约束** | 忘记 LP expectations 会限制可承受的风险 | `[M1 p.79-80]` |
| 11 | **把倍数当成独立于 DCF 的方法** | multiples are a shortcut to DCF | `[M1 p.9, p.17]` |
| 12 | **忽略 equity duration** | "No hope of truth"；只做 5 年 DCF 会严重误判 | `[M1 p.16, p.56]` |
| 13 | **把 beta 当 alpha 目标** | Beta is "cheap", alpha is "expensive"；beta 不是零和（~10%），alpha pool 才是零和 | `[M2 p.11, p.13]` |
| 14 | **忽视费用对 alpha 的侵蚀** | 4-5% fee load 使 HF 集体选股能力（Hedge Fund Mirage, Lack）大部分归 GP 而非 LP；net alpha subdued | `[M2 p.83-84]` |
| 15 | **用错风险包络** | net exposure 低 → 牛市跑输；gross 高但 net 低 → 收益被摊薄 | `[M2 p.75, p.76]` |
| 16 | **把规模当作优势** | Gain assets 可以是回报的敌人 | `[M2 p.25]` |
| 17 | **忽视 pro-cyclical capital flow** | 投资者倾向配置给近期表现好的管理人 | `[M2 p.25]` |
| 18 | **误判 alpha 来源** | 把 gross return 当 alpha，忽略 8% long-short spread 才是真正难产生的部分 | `[M2 p.70]` |
| 19 | **择时与杠杆双刃** | leverage cuts both ways；8% spread 不加杠杆只产 6% on gross | `[M2 p.56-57]` |
| 20 | **把"能"当"应"** | just because the can most often doesn't mean they should | `[M2 p.19]` |
| 21 | **照搬别人的 process 而不自省** | thesis format / process 应 reverse engineer 自家体系 | `[M2 p.28, p.103]` |
| 22 | **Process creep / mandate creep** | style drift、volatility、industry 约束是 LP 施加的 | `[M2 p.13, p.79]` |
| 23 | **PM 时间被 triage 吞掉** | actual work 仅 1-3 小时/天，难支撑 40-60 小时的严谨 thesis | `[M2 p.86]` |
| 24 | **对下行不做功课** | 先接受 downside case | `[M2 p.112]` |

---

# Key vocabulary（必须精确使用的术语）

**市场与定价**：market-based economy；price signal；capital-weighted consensus；voting machine / weighing machine；order book；continuous double auction；bid/ask spread；last sale；buyer's strike / seller's strike；equity duration；unlevered FCF；NPV；WACC；cost of equity；ERP；beta；terminal multiple；marginal cost of capital；cumulative FCF；business momentum；market momentum；value trajectory；market implied value。

**Alpha 与预期**：alpha load；excess return；beta-adjusted alpha；expectations gap（= market view − internal view）；mispricing；alpha buckets；mosaic approach；situational market efficiency；differential view / variant perception；insider buy；consensus long。

**流程与判断**：key drivers；Value Belief (VB)；Entry Point (EP)；ETIK；KD；process & judgment；fundamental work / expectations work / valuation work；Pareto distribution；rake；"Gauntlet of Disqualifiers"。

**买方组织**：General Partner (GP)；Limited Partner (LP)；allocator；single manager hedge fund；multi-manager hedge fund；pod；2 & 20；management fee；performance fee / carry；pass-through fees；effective fee load；net exposure；gross exposure；long market value (LMV)；short market value (SMV)；beta-adjusted net exposure；alpha；idiosyncratic；factor exposure；Sharpe ratio；Sortino；pro-cyclical capital flow；alpha pool；zero-sum；mandate alignment；mandate creep / style drift；volatility targeting；permanent capital impairment；all-weather portfolio；withdrawal rate。

**买方思维**：equity stub；incremental margin；buyback yield；unit economics；second order thinking；journalistic disposition；dispassionate due diligence；essential thinking；probabilistic thinking / expected value (EV)；adaptive conviction；earned confidence；long-short spread；portfolio wedge；shareholder return decomposition（roll-forward / re-rating / revisions）。

---

# Quotes（verbatim, with page）

1. `[M1 p.28]` "FUNDAMENTAL ANALYSIS IS A METHOD THAT ATTEMPTS TO DETERMINE A SECURITY'S VALUE BY FOCUSING ON THE UNDERLYING FACTORS THAT AFFECT A COMPANY'S ACTUAL BUSINESS & IT'S FUTURE PROSPECTS."
2. `[M1 p.16]` "DCF: A 'simple, not easy' framework for pricing assets… A standard equity requires 25-35 years of FCF discounting to achieve today's share price."
3. `[M1 p.44]` "Even the CFO likely only has 6-18 months of visibility."
4. `[M1 p.44]` "Those incremental sales may be informed by a view of NPV, but often they are not. Forced or emotional sellers, non-fundamental sellers (ETF flows). Scared sellers."
5. `[M1 p.100, PHIL FISHER]` "You would not cut the value of a good farm in half just because bad weather conditions caused a crop failure in a single year."
6. `[M1 p.101, GRAHAM]` "In the short run, the market is a voting machine but in the long run it is a weighing machine."
7. `[M1 p.56]` "Remember equity duration. No hope of truth. Price simply a capital weighted consensus."
8. `[M1 p.37]` "'Because it's hard, markets are efficient' … 'Poker is hard too…'"
9. `[M2 p.11]` "Beta is not zero-sum, i.e. collective equity returns over time have approximated ~10%. Like a poker 'rake', fees turn active management into less than a zero-sum game."
10. `[M2 p.19]` "In theory, barriers to entry in the public equity markets are low. But just because the can most often doesn't mean they should."
11. `[M2 p.20, Mike McDermott]` "Why do you think the same five guys make it to the final table at the WSOP every single year? … It's a skill game, Jo."
12. `[M2 p.84]` "Hedge Fund Mirage (Lack) shows most of that alpha accrues to GP."
13. `[M2 p.70]` "4% return on gross in this example is actually 8% long-short spread (~alpha) which is DIFFICULT and IMPRESSIVE."
14. `[M2 p.76]` "Real P&L generation on the short side is difficult. It's more a spread game, with real P&L generated on longs."
15. `[M2 p.86]` "Often a PM has surprisingly minimal time for focused, intentional thesis work… 'Best case' 5-7 hours a day, but usually dealing with triage and 1-3 hours is more standard."
16. `[M2 p.103]` "As an interviewer, my thought: if this person can't articulate a process clearly, there is no process!!!"

---

> 来源：Fundamental Edge 买方培训课件 Module 1（Brett Caughran）。方法论引用，不构成投资建议。
