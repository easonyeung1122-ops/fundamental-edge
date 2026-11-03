# 延伸阅读方法论摘要（Supplemental Readings）

本文件汇总 Fundamental Edge 课件配套延伸阅读的核心框架、公式、数字阈值与作者警告，逐篇对应 `references/` 中的方法论。

---

## ROIC：投入资本回报率与 ROIC 估值框架

**来源**：*Calculate ROIC, 2022*（Mauboussin & Callahan, Morgan Stanley Counterpoint Global, 2022-10-06）；*Primer on the ROIC Valuation Framework*（Bear Stearns, 2004-08）

### 核心论点

作者主张用 **ROIC**（Return on Invested Capital）衡量企业创造价值的能力，而非 EPS 或账面价值。核心判断标准是"一美元测试"（one dollar test）：投资一美元产生的现金流现值必须大于一美元，否则增长只是"跑步机上调档"。Bear Stearns 版进一步把 ROIC 升级为估值框架（ROIC Valuation Framework），用**四个杠杆**（Four Levers Drive Value）把 ROIC 与价值创造连接起来。

### 公式与 worked numbers

**Mauboussin 版：**

- `ROIC = NOPAT / Invested Capital`
- `NOPAT = EBITA – cash taxes`；近似式 `NOPAT ≈ EBITA × (1 − cash tax rate)`
- Invested Capital **经营法**（operating approach）：`Net Working Capital + Net PP&E + Operating lease ROU assets + Goodwill + Intangibles, net + Other long-term assets`
  - `Net Working Capital = Current assets – NIBCLs`（无息流动负债）
- Invested Capital **融资法**（financing approach）：`Short-term debt + Long-term debt + Other long-term liabilities + Preferred stock + Common equity`
- `Economic profit = (ROIC − WACC) × Invested capital = NOPAT – (Invested capital × WACC)`
- `FCF = NOPAT – Investment`；`Growth = ROIC × (1 – payout ratio)`
- `ROIIC = (Year1 NOPAT – Year0 NOPAT) / (Year0 invested capital – Year-1 invested capital)`
- 杜邦式分解：`ROIC = (NOPAT/Sales) × (Sales/Invested Capital)`——零售商 `3% × 6x = 18%`，奢侈品 `18% × 1x = 18%`

**Microsoft 案例（FY2022）**：EBITA $87B，cash taxes $17B → NOPAT $70B；invested capital $165B，平均 invested capital $143B（$120B 与 $165B 的均值）→ **ROIC 49%**。资本化无形资产后：NOPAT $80B，invested capital $260B（平均 $233B）→ **ROIC 34%**；资本化无形投资 $41B、摊销 $31B、净额 $10B，资本化无形净额 $95B，invested capital 增加 58%。

**Bear Stearns 版：**

- `ROIC = NOPAT / Total Invested Capital`；`NOPAT = EBITA – Unlevered Cash Taxes`
- 三个口径求同：**经营法**（看资产负债表左侧：NWC + Net PP&E + Net Non-Goodwill Intangibles + Other Long-Term Assets）、**融资法**（Total Debt + Preferred Equity + Minority Interest + Shareholders' Equity）、**财务法**（自 EBITA 起算 NOPAT，再减去未合并投资、少数股东权益等非经营性资产）。经营法与融资法应得出相同的 Total Invested Capital
- 示范资产负债表（Operating Approach, $B）：Cash $100.0、Non-Cash Current Assets 158.5、Unconsolidated Investments 19.1、Net PP&E 372.5、Net Goodwill 13.7、Other Net Intangibles 10.0、Other Long-Term Assets 107.0 → **Total Assets $780.8**；Current Liabilities $253.1、Total Debt 300.0、Deferred Taxes 127.7、Other Long-Term Liabilities 0.0、Minority Interest 0.0、Preferred Equity 0.0、Shareholders' Equity 100.0
- Total Invested Capital 对照：经营法 `Non-Cash Current Assets 158.5 − Current Liabilities 253.1 = Net Working Capital (94.6)`；`+ Net PP&E 372.5 + Net Non-Goodwill Intangibles 10.0 + Other Long-Term Assets 107.0`；融资法 `Total Debt 300.0 + Deferred Taxes 127.7 + Shareholders' Equity 100.0 − Cash 100.0 − Unconsolidated Investments 19.1 − Goodwill 13.7`；两者均收敛到 **Total Invested Capital $394.9**

### 决策规则与阈值

- **必备现金**：公司进入稳态后，按经验法则保留约收入的 **2%** 作为必要现金；可预测性差、成长性高的公司现金/收入可至 **5%**。Microsoft FY2022：按 2% 计为 $4B，若计入全部 $105B 现金，invested capital 从 $165B 升至 $266B，ROIC 从 49% 降至 29%
- **现金税率**：现金税率通常略低于名义税率（成长型企业）；Damodaran 估计 2021 年现金税约为报税的 **95%**
- **ROIC 分布基准**（Russell 3000, 2021）：众数落在 **5–10%**；近 **30%** 的公司 ROIC ≤ −20% 或 ≥ 30%；30 年 aggregate ROIC 从 7.6% 升至 11.4%
- **Economic profit 分布**（2017–2021）：top decile +$675B，bottom decile −$220B，中间 80% 合计仅 +$70B；Apple + Microsoft + Alphabet 合计约 $120B（约占 1/5）
- Bear Stearns **四个杠杆**（Four Levers Drive Value）：Excess Return（ROIC > WACC）、Reinvestment Opportunities、Duration of Competitive Advantage、Risk（降低感知商业风险即降低 WACC）
- **Interplay of Levers**：Business 1（20 年 CAP，高超额回报）与 Business 2（40 年 CAP，中等超额回报）可创造等量价值——**久期可以替代幅度**
- **增长假设必须与 ROIC 联立检验**：支持 0.5% 永续增长，Company 1 必须 (i) **未来 40 年赚取 14.5% ROIC**，其后 WACC 9.0%；(ii) 每年再投资 **12.5% 的 NOPAT**；Company 1 预测 2006 年 ROIC 约 **14.8%**。若要支撑 **2.5%** 永续增长，多变量模型要求 **50 年内维持 30.8% ROIC**，平均再投资率 12.5%——Company 1 的预测显示这些假设"probably unrealistic"
- **终值倍数区间 4.5x–6.5x**（EBITDA）在当时"看似可辩"（Might Seem Justifiable Based on Current Trading Multiples）。Company 1 每股权益价值矩阵（WACC 8.0%–10.0% × EBITDA 终值倍数 4.5x–6.5x）：WACC 8.0% 时 $29.68 / $34.23 / $38.74 / $43.24 / $47.63；WACC 9.0% 时 $27.38 / $31.73 / $36.06 / $40.36 / $44.64；WACC 10.0% 时 $25.20 / $29.35 / $33.51 / $37.63 / $41.73。对应"标准化 FCF 隐含永续增长率"（同一矩阵）：WACC 8.0% 时 (0.1%) / 0.7% / 1.3% / 1.8% / 2.3%；WACC 9.0% 时 0.8% / 1.6% / 2.2% / 2.7% / 3.2%；WACC 10.0% 时 1.7% / 2.5% / 3.2% / 3.7% / 4.2%
- **预测期长度**：Company 1 需五年显性预测期（'02E–'06E），并在此基础上做终值倍数敏感性

### 常见错误与陷阱

- **只算 EPS 或 P/B 而不算 ROIC**：ROIC 是检验盈利质量的锚
- **用融资法单算 invested capital**：若剥离多余现金，必须**同时**从资产端与负债端调整，否则口径不一致
- **把商誉当作真实投资**：多数分析师认为商誉不反映投资；也有观点认为商誉减值应从 invested capital 中扣除
- **Total Debt 应排除在 NOPAT 生成资产之外**（不贡献 NOPAT 的资本应剔除）
- **未合并投资（Unconsolidated Investments）不应计入 ROIC 分母**
- **R&D 与 Human Capital 漏算**：GAAP 要求多数技术公司费用化 R&D；新产品开发与前置营销费用、人力资本均未反映在历史 ROIC 中——这会使历史 ROIC **高估**真实经济回报
- **现金税率低估的税务风险**：TCJA 的 30% EBIT 利息抵扣上限影响 Russell 3000 中约 **25%** 正 EBIT 公司
- **ROIIC 的偏差**：当 ROIC 高于 WACC 时 ROIIC 高估经济回报，低于 WACC 时低估；作者提示更优指标是 **MEROI**
- **ROIC 不能用于金融企业**（应改用 ROE）；**不能用 ROIC 评估 M&A**（应做 NPV）

### 逐字引文

> "A company creates value when the present value of the cash flows from its investments are greater than the cost of the investments."（*Calculate ROIC*, p.1）

> "Growth is like the speed setting on a treadmill. You can turn it up or down but you are going nowhere."（*Calculate ROIC*, p.1）

> "Value is created by earning returns (ROIC) in excess of cost of capital (WACC).”（Bear Stearns, *Four Levers Drive Value*, p.1）

> "Businesses with moderate excess returns but long periods of competitive advantage can generate as much value as businesses with higher excess returns but shorter periods of competitive advantage."（Bear Stearns, *Interplay of Levers*, p.2）

---

## Moat：护城河的度量（Measuring the Moat）

**来源**：*Measuring the Moat*（Credit Suisse GFS, 2016-11-01；Mauboussin, Callahan, Majd）

### 核心论点

护城河（moat）不是品牌知名度，而是**可持续价值创造**（sustainable value creation）——即 ROIC 与资本成本（WACC）之间的正利差能维持多久。作者将其拆为两个维度：**利差幅度**（magnitude of the spread）与**持续时长**（fade rate / 竞争优势期 CAP / 价值增长持续期 T）。护城河分析必须落到"利润池"（profit pool）与行业结构上，而非笼统的品牌叙事。

### 公式与关键数字

- `Value created = willingness-to-pay – opportunity cost`
- **四种创造价值的路径**：(1) 提高自身客户的支付意愿；(2) 降低竞争对手客户的支付意愿；(3) 降低供应商的机会成本；(4) 提高竞争对手供应商的机会成本
- `CFROI = CFROI Margin × Asset Turnover`——等 CFROI 6% 的等值曲线；Nike（margin 14、turns 1.2）与 Alphabet（margin 43、turns 0.4）CFROI 均为 **17%**
- **McGahan & Porter 1981–1994、约 58,000 firm-year** 的分解：Industry 因素对 High Performers 贡献 emergence **37%**、sustainability **44%**；Segment-Specific **43%** / **34%**；Corporate-Parent **18%** / **19%**；Year **2%** / **3%**。Low Performers 则 Segment-Specific 高达 **90%** / **99%**，Industry 仅 **13%** / **12%**
- **利润池示例**：$200M 投入资本 × 5pp 利差 = $10M economic profit；航空业 2004–11 周期**平均每年毁灭 $17B 股东资本**
- **行业稳定性阈值**：5 年绝对平均市场份额变化 **≤ 2.0** 视为稳定行业——汽车 1%、PC 3%、手机 7%、智能手机 14%
- **HHI**：`HHI = 10,000 × Σ(份额²)`（前 50 大）；**> 1,800** 视为竞争减弱。示例 40/30/20/10% → **3,000**
- **学习曲线**：中位企业累计产量翻倍 → 单位成本下降约 **20%**
- **DRS（进入/退出）研究**：假设 2016 年 100 家、每家 $1M 销售，5 年内 **30–45 家**新进入、合计销售 $15–20M；同期 **30–40 家**退出（合计 $15–20M）；行业 turnover **30–45%**，进出方占行业销量 **15–20%**；新进入者规模约为在位者的**三分之一**；到 2026 年约 **80%** 的进入者会退出
- **生存率**（Credit Suisse HOLT）：不到 **50%** 的上市公司存活超过十年；一年生存率约 **80%**，五年约 **50%**
- **品牌实证**：10 家最具价值品牌公司中有**两家**勉强赚回资本成本；品牌与经济回报弱相关
- **回归速度表**（25 个行业，one-year correlation coefficient / long-term avg CFROI）：Food, Beverage & Tobacco 0.95 / 8.6；Household & Personal 0.95 / 12.3；Food & Staples Retailing 0.93 / 8.2；Consumer Services 0.92 / 8.0；Commercial & Professional Services 0.91 / 11.1；Capital Goods 0.89 / 6.7；Health Care Equipment & Services 0.89 / 11.7；Pharma/Biotech/Life Sciences 0.89 / 8.1；Media 0.88 / 9.9；Transportation 0.87 / 5.2；Consumer Durables & Apparel 0.87 / 8.5；Retailing 0.87 / 8.7；Regulated Utilities 0.86 / 3.2；Software & Services 0.85 / 12.3；Automobiles & Components 0.83 / 5.2；Telecom Services 0.83 / 6.1；Tech Hardware & Equipment 0.82 / 6.8；Utilities 0.82 / 4.1；Insurance 0.81 / 8.5；Energy 0.78 / 5.7；Materials 0.78 / 4.9；Semiconductors & Equipment 0.77 / 6.6；Real Estate 0.77 / 4.6；Banks 0.76 / 9.3；Diversified Financials 0.73 / 9.0
- **最小有效规模**：Intel 第一颗 Xeon 成本超 **$10B**

### 决策规则与阈值

- **预期投资三步法**：(1) 估算价格隐含的预期（price-implied expectations）；(2) 识别预期差（expectations opportunities）；(3) 买入/卖出/持有
- **辨别真优秀企业的两条规则**：**"Better before cheaper"**（先做更好的产品，而非先降价）与 **"Revenue before cost"**（优先做收入，再降成本）
- Raynor & Ahmed 研究 1966–2010 年 25,000+ 家公司，筛出 **344 家**真正卓越者；19 本畅销书中的 699 家里仅 **12%** 符合标准
- **行业稳定性判据**：5 年绝对平均市场份额变化 **≤ 2.0** 为稳定（可支撑长 CAP）；> 2.0 说明份额仍在剧烈波动，护城河脆弱
- **HHI > 1,800** 表示竞争减弱，可支撑更长的竞争优势期

### 常见错误与陷阱

- **用品牌或份额代替利润池分析**：份额稳定不等于创造价值，航空业份额曾长期稳定却年年毁灭价值
- **忽视 segment 层面的竞争**：高绩效者的可持续性有 34% 来自 segment-specific 因素，纯行业分析会错估
- **假设利差永续**：无竞争优势时回报趋向回归 WACC；fade rate 必须显式建模
- **低估行业 churn**：五十年生存率不足 50%，DRS 数据显示大量进入者在 5–10 年内退出
- **把高 FCROI 等同高经济回报**：turnover 与 margin 可能互相抵消，Nike 与 Alphabet 就是同 CFROI 不同路径

### 逐字引文

> "Sustainable value creation has two dimensions: the magnitude of the spread between a company's return on invested capital and the cost of capital and how long it can maintain a positive spread."（*Measuring the Moat*, p.3）

> "Value created = willingness-to-pay – opportunity cost"（*Measuring the Moat*, p.32）

> "Better before cheaper: compete on differentiators other than price."（*Measuring the Moat*, p.49）

---

## Free Cash Flow：自由现金流入门（A Primer on FCF）

**来源**：*A Primer on Free Cash Flow*（Damodaran, 2022-10-25）

### 核心论点

Damodaran 认为自由现金流是金融中最容易被扭曲的概念，必须先定义"现金流归属于谁"。**FCFE**（Free Cash Flow to Equity）归属股东，**FCFF**（Free Cash Flow to the Firm）归属全部资本提供者，两者都以税后、再投资后的现金流为基础。FCF 的价值在于它是**真实的经济剩余**，而会计利润可以通过多种方法粉饰。

### 公式与 worked numbers

- `FCFE = 净利润 + 折旧摊销 + 非现金收益 − 非现金营运资本变动 − 资本支出 − 债务发行 + 债务偿还`
- `FCFF = EBIT × (1 − tax rate) + 折旧摊销 − 资本支出 − 营运资本变动`
- **Microsoft FY2021 worked example**：reinvestment $19,370M；FCFE before debt $41,901M；偿还债务 $5,504M → **FCFE after debt $36,397M**；EBIT $69,916M，有效税率 13.83% → **FCFF $40,879M**
- **非现金营运资本正常化**：2012–21 历史均值 **−10.18% of revenues**，据此 base-year 变动为 −$2,552M（现金流入），而非实际的 −$1,086M（流出）。FCFF 口径下改用 2017–2021 平均有效税率 **22%** 替代 13.83%
- **R&D 资本化的净效应为零**：Microsoft FY2021 R&D $20,716M 资本化 → 净利润 **+$3.7B**，D&A **+$17B**，capex **+$20.7B**，对 FCFE 净效应为 0（但显著改变利润与再投资规模）
- **全股票收购**：Nuance Communications $19.76B 全股票对价应计入 reinvestment，而非"无现金流"

### 决策规则与阈值

- **FCFE 用于股权定价倍数时**：Price/FCFE 仅能在 **63%** 的全球上市公司算出（PE 损失近一半公司）；EV/FCFF 因负 FCFF 损失约 **55%** 公司；EV/EBITDA 损失约 **42%**。25 家同业样本用 Price/FCFE 可能只剩 10 家或更少
- **SBC 不得加回**：加回 SBC 等于宣称可以停止以股权支付员工薪酬，或可以无限让渡股权——两种说法都不成立
- **企业生命周期判断**：最年轻 decile 中 **超过 73%** 亏损、**超过 3/4** FCFE 为负；生命周期中段的公司 FCFE/market cap 最高
- **股东现金回报的构成**：2021 年股东现金回报中 **超过 2/3** 来自回购
- **正常化优先于精确**：intrinsic valuation 中对未来现金流有较大裁量权；Microsoft 案例显示做五项调整后 FCFE 形态明显不同

### 常见错误与陷阱

- **把"加回折旧"当作自由现金流**：这是中间步骤，不是 FCF
- **按报告数字直接取营运资本变动**：不区分正常化水平，会得出错误结论
- **加回股票薪酬（SBC）**：Damodaran 明确拒绝
- **用 FCF 倍数替代传统倍数做定价**：因负值剔除与波动性，反而降低样本质量
- **用 FCFE 与 FCFF 混用折现率**：股权现金流必须用 cost of equity，企业现金流用 WACC
- **生命周期误判**：把年轻亏损公司当成熟现金牛，或反之

### 逐字引文

> "Free cash flow is one of the most dangerous terms in finance, and I am astonished by how it can be bent to mean whatever investors or managers want it to"（*A Primer on FCF*, p.1）

> "I do not add back stock-based compensation, and will provide a rationale for why in the next section"（*A Primer on FCF*, p.2）

> "the companies in the middle of the corporate life cycle, deliver the highest FCFE as a percent of market capitalization"（*A Primer on FCF*, p.6）

---

## Cost of Capital：资本成本实操指南

**来源**：*A Practical Guide to Assessing Cost of Capital*（Mauboussin & Callahan, Morgan Stanley Counterpoint Global, 2023-02-15）

### 核心论点

资本成本（WACC）是连接公司金融与投资的枢纽。作者强调资本成本只是"入场券"，真正重要的是理解业务本身与其可持续竞争优势；实务中资本成本的估计需要一致性与判断的平衡。框架上，资本成本由企业风险（business risk + financial risk）经债务与股权两条腿传导至加权平均。

### 公式与 worked numbers

- `Corporate risk = business risk + financial risk`
- `After-tax cost of debt = pre-tax cost of debt × (1 – marginal tax rate)`
- `Cost of debt = promised yield spread – lost yield due to default`
- **M&M 不变式示例**（$100 operating profit）：
  - A 无债：cost of equity 10%，equity $1,000，firm value $1,000
  - B 债 $200 @5%：cash flow for equity 90，cost of equity 11.25%，equity $800，firm value $1,000
  - C 债 $400 @6.25%：cash flow for equity 75，cost of equity 12.5%，equity $600，firm value $1,000
- **预期违约损失率**：投资级（BBB− 及以上）10 年约 **2%**；投机级（BB+ 及以下）约 **23%**
- **Merton/Cooper-Davydenko 信用溢价分解**：debt-to-total capital 20%、credit spread 100bp over AAA、ERP 6%、equity volatility 30% → **13bp**（spread 的 13%）；70% 杠杆、400bp spread、ERP 6%、volatility 50% → 近 **250bp**（spread 的 **62%**）
- **信用溢价历史**：BBB spread 峰值 7.8pp（2008-12），谷值 1.1pp（2021-06）；高收益 spread 峰值 19.9pp（2008-11），谷值 3.0pp（2021-06）
- `Expected return = Risk-free rate + β(Market return – Risk-free rate)`
- **Beta 示例**（Nike，60 个月月度 vs S&P 500）= **1.09**，R² 49%，回归式 `y = 1.09x + 0.50`；四基准对比：S&P 500 1.09 / Russell 1000 1.07 / Dow Jones 1.07 / MSCI ACWI 1.25
- **Beta 时间窗敏感性**：3 年 1.10 (R² 49%)、5 年 1.09 (49%)、7 年 1.06 (43%)、10 年 1.00 (37%)
- **Beta 频率敏感性**（Nike）：Daily 1.07 (SE 0.03)、Weekly 1.09 (0.07)、Monthly 1.09 (0.15)、Quarterly 1.28 (0.26)、Yearly 1.03 (0.45)
- **Amazon**：60 月 raw beta 1.22、R² 44%、SE 0.18 → 95% 置信区间 0.86–1.58；`Adjusted beta = Raw beta (0.67) + 1.0 (0.33)` → **1.15**
- `WACC = (cost of debt × weighting of debt) + (cost of equity × weighting of equity)`；示例 **5% × 20% + 10% × 80% = 9.0%**
- **Russell 3000 WACC 1985–2022**：全期均值 **7.9%**，2022 年末 **8.8%**；2022 年 debt-to-total capital **18%**（全期均值 30%）
- **10 年美债对 S&P 500 的 beta = 0.03**（60 个月月度，2018–2022）
- **ERP 证据**：150 本教材给出 **3%–10%** 区间，三分之一书内使用不同 ERP；2001 年会议估计 0%–7%，均值略低于 4%；其后 10 年实现 ERP **−4.1%**；Damodaran ERP 1961–2022 区间 **2.1%（1999）– 6.5%（1979）**；2008–2022 平均 5.5%（高 7.7% 于 2009-02，低 3.9% 于 2021-07）；Expected return 峰 10.7%（2009-02）、谷 5.1%（2020-12）；2022 年初 5.8% → 年末 9.8%；ERP/risk-free 比率 1961–2000 约 0.6，2022 约 1.5
- **算术 vs 几何平均**：美国股票减债券 1928–2022 算术 **6.6%**、几何 **5.1%**（差 1.5pp）；S&P 500 自 1928 标准差略低于 20%，标准误约 **2.0%**（0.02 = 0.197 ÷ 94^0.5）；样本少于 20 年时标准误 ≥ ERP
- **ERP vs credit spread**：历史上 ERP 约为 credit spread 的 **2.0 倍**；2022 年末为 **3.0 倍**
- **Amazon 2022 净债务**：lease liabilities $73.0B（$11.4B capital + $61.6B operating）+ total debt $70.1B = $143.1B；cash+securities $70.0B；sales $514B，2% 运营现金 → excess cash $59.7B；net debt $83.4B；equity value $860B（$84.00 × 10.2B shares）
- **Fama-French 三因子**：`Return = α + β1(Rm – Rf) + β2(RS – RB) + β3(RH – RL) + ε`
- **APV 示例**：sales $15,000（Y1），growth 5%，EBITA margin 15%，nwc growth 15% of incremental sales，fc growth 20%，tax 25% → FCF Y1 $2,000；unlevered cost of equity 10% → Σ PV CF **$14,880**；cost of debt 6% → Σ PV tax shield **$606**；**APV = $15,486**（96% 来自经营、4% 来自税盾）

### 决策规则与阈值

- **估算清单**（Checklist for Estimating the Cost of Capital）：Debt 端——YTM / credit spread / OAS / 税盾 / NOL 与税收抵免；Equity 端——risk-free rate / 当前 ERP / industry beta / multi-factor / relever / 与 cost of debt 及隐含波动率交叉验证 / continuing value 的 beta 接近 1.0；Other——preferred 与 convertible；资本结构——target debt-to-capital 用市场值，**若资本结构将变化则改用 APV**
- **Beta 估计优先用 adjusted beta**（向 1.0 回归），因为纯历史 beta 对窗口与频率极度敏感
- **ERP 取值**：作者在 2006 年 DCF 一文中建议 **3–4pp**（隐含市场回报约 8%），mid-March 2006 risk-free rate 4.7%
- **实践者**：FCFF 模型使用频率约为 FCFE 的两倍

### 常见错误与陷阱

- **把 10 年期国债当无风险资产却用 1.03 的 beta**——国债对 S&P 500 的 beta 应接近 0（实测 0.03）
- **在 beta 上做无根据的精确化**：2006-03 GM 的 beta 报 1.3、Yahoo! 超过 1.6，这类估计不可靠
- **用算术平均 ERP 而非几何平均**：长期超额回报应取几何平均（5.1% vs 6.6%）
- **忽略 default 损失**：promised yield 与 expected yield 之差在高收益债中高达 23%
- **信用溢价被高估**：高杠杆 + 低评级组合下，spread 中仅约 62% 来自真正的信用风险
- **忽略租赁负债**：Amazon 的 $73.0B lease liabilities 必须计入债务
- **资本结构变化时仍用静态 WACC**：应改用 APV
- **忽略税盾价值**：APV 中税盾贡献虽小（约 4%），但在高杠杆时显著放大

### 逐字引文

> "The cost of capital is based on the economic principle of substitution. An investor will not invest in an asset if a"（*A Practical Guide to Assessing Cost of Capital*, p.5）

> "Corporate risk = business risk + financial risk"（*A Practical Guide to Assessing Cost of Capital*, p.6）

> "Deriving a practical cost of capital is essential but not as important as understanding a business and its prospects."（*A Practical Guide to Assessing Cost of Capital*, p.36）

---

## DCF Errors：DCF 模型的常见错误

**来源**：*Common Errors in DCF Models*（Legg Mason Capital Management, Mauboussin, 2006-03-16）

### 核心论点

DCF 几乎被普遍使用，但多数模型在八个环节上犯系统性错误，导致结果不可用。作者的核心洞察是：DCF 与倍数不是对立的两种方法——**倍数只是 DCF 的速记形式**（shorthand），把同样的假设打包进一个数字，反而丧失透明度。

### 八大错误

1. **预测期过短**（forecast horizon too short）
2. **不经济的 continuing value**（uneconomic continuing value）
3. **cost of capital 不合理**
4. **假设投资与盈利增长不匹配**
5. **未恰当反映其他负债**（ESO 员工股票期权、养老金）
6. **对 private market value 打折**（public market discount）
7. **双重计算**（double counting）
8. **只有单一情景**（insufficient scenario analysis）

### 公式与 worked numbers

- **Appendix A 价值恒等式**：`Value = [NOPAT(CAP+1) × (1 − growth/ROIIC)] / (WACC − g)`，等价于 `Value = FCF(CAP+1) / (WACC − g)`
  - 示例：NOPAT $100，growth 5%，ROIIC 12%，WACC 9% → `58.33 / 4% = 1,458.3`；`Investment = 5/12% = 41.67`；`FCF = 58.33`
  - 对照：当 ROIIC = WACC = 9% → `44.44 / 4% = 1,111.1`，与直接 perpetuity `100 / 9% = 1,111.1` 一致
- **continuing value 的经济约束**：13.0× EBITDA 的终值隐含 **6%** 的盈利增长与 **150% return on incremental capital in perpetuity**（假设 depreciation = EBITA 的 20%、税率 35%）
- **Equity risk premium 的几何平均**：1982–2005 为 **1.9pp**、1962–2005 为 **3.7pp**、1926–2005 为 **6.2pp**

### 决策规则与阈值

- **显性预测期至少 5 年**（explicit forecast periods of no less than five years），许多公司需要 **超过 10 年** 才能支撑其股价
- **显性期应捕捉公司价值的至少 1/3**（at least one-third of corporate value）
- **continuing value 通常占公司价值的 60–70%**
- **public market discount 取 20–25%**（惯例值，电信业最普遍）
- **ERP 建议 3–4pp**（隐含市场回报约 8%），mid-March 2006 risk-free rate 4.7%
- **市场历史 P/E 在 mid-to-high teens**

### 常见错误与陷阱

- **预测期过短 + continuing value 过重**：两者叠加后"both parts of the model—the forecast period and continuing value estimate—next to useless"
- **不经济的 continuing value**：用 EBITDA 倍数倒推终值会隐含永续 150% 的增量资本回报——"no company in the history of mankind has achieved such financial performance"
- **双重计算的具体形态**：(a) 先对现金流估值，又用同一现金流减少股数（回购）；(b) 利息收入计入现金流，同时把现金加进企业价值
- **ESO 处理不当**：应作为或有负债、采用基本股数、把未来授予作为费用
- **public market discount 缺乏透明度**：因混淆 base 与 synergy cash flows 而不透明
- **情景分析只调 discount rate / growth / terminal value**：应基于 value drivers（sales、margins、investment needs）构建情景，并考虑 value drivers 之间的交互性
- **用倍数逃避假设**：倍数把 DCF 的同样假设打包，盲点与偏见相同

### 逐字引文

> "We recommend explicit forecast periods of no less than five years, and note many companies require over ten years of value-creating cash flows to justify their stock prices."（*Common Errors in DCF Models*, p.2）

> "Models should not count a dollar of value (or liability) more than once."（*Common Errors in DCF Models*, p.7）

> "no company in the history of mankind has achieved such financial performance"（*Common Errors in DCF Models*, p.3）

---

## Multiples：P/E 倍数到底意味着什么

**来源**：*What Does a Price-Earnings Multiple Mean?*（Credit Suisse GFS, 2014-01-29；Mauboussin & Callahan）；*The Trouble with Earnings and Price/Earnings Multiples*（Rappaport & Mauboussin, Copyright 2001）

### 核心论点

P/E 倍数不是外生给定的价格除以盈利，而是一个**内生求解的结果**：把公司价值分解为"稳态价值 + 未来价值创造"。Rappaport & Mauboussin 进一步指出，盈利与股东价值之间存在三重差异，因此 P/E 分析在逻辑上是循环的——它不是估值的捷径，而是估值过程本身。

### 公式与 worked numbers

- `Value of the firm = steady-state value + future value creation`
- `Steady-state value = NOPAT (normalized) / Cost of capital + excess cash`
- `Future value creation = Investment × (return on capital – cost of capital) × competitive advantage period / [Cost of capital × (1 + cost of capital)]`
- `Equity value = steady state + future value creation + excess cash – debt`
- `Steady-state P/E = 1 / Cost of equity`
- **2014 年初** Damodaran 美国 cost of equity **8%** → **12.5×** 稳态 P/E
- **1961–2013** 稳态 P/E 平均 **10.4×**，标准差 **2.7**；1981 年低点略高于 **5×**
- **稳态 vs 预期**：自 1961 年稳态价值平均解释约 **2/3** 市值，预期价值创造约 **1/3**
- **S&P 500 实例**：截至 2013-09-30 的四季度盈利 $102.20，cost of equity 8% → 稳态价值 1,277.50；指数收于 1,681.55 → 稳态占 **74%**，预期价值创造占 **24%**；2014 年该比率在 15–20%
- **下滑期修正**：`Modified steady-state value = NOPAT × (1 + growth) / (Cost of capital – growth)`；示例 NOPAT $100、WACC 10%、永续下滑 10% → `$100(.90)/.20 = $450` → 稳态 P/E **4.5×**
- `ROIIC = (NOPAT₁ – NOPAT₀) / Investment₀`；示例投资 $50 使 NOPAT 增 $10 → ROIIC 20%；投资 $100 → 10%
- **Exhibit 5 矩阵**（all-equity，8% WACC，15 年预测期；行=增长，列=ROIIC 4%/8%/16%/24%）：增长 4% 行 7.1x / 12.5x / 15.2x / 16.1x；6% 行 3.3 / 12.5 / 17.1 / 18.6；8% 行 NM / 12.5 / 19.4 / 21.8；10% 行 NM / 12.5 / 22.4 / 25.7
- **Appendix A 杠杆验证**：firm $1,000 = equity $750 + debt $250；EBIT $107.7；cost of equity 8%；pretax cost of debt 6.15%；tax 35% → WACC = (750/1,000)(8%) + (250/1,000)(6.15%)(1−0.35) = **7%**；firm value = 107.7(.65)/.07 = $1,000；net income = (107.7 − 15.4)(.65) = $60；equity = 60/.08 = $750
- **市场隐含 CAP**（Olsen, 1976–2007）：平均约 **8 年**，极竞争行业约 **5 年**，稳定行业约 **15 年**；slow fade 行业为消费必需品与医疗保健，fast fade 为信息技术与能源
- **三个 15.0× P/E 的实现路径**：高增长低价差（growth 12.0%、ROIIC 8.8%）；中等（6.0%、11.0%）；低增长高价差（3.0%、23.0%）

### The Trouble with P/E（Rappaport & Mauboussin）的数字

- **市场隐含预测期**：Dow Jones 未来五年预期股利仅解释股价 **10–15%**；美国股票 market-implied forecast period 聚集在 **10–15 年**，具备强竞争优势者可**超过 20 年**
- **股利收益率对比**：2001-07 平均股利收益率约 **1%**，30 年期国债约 **6%**；S&P 500 长期股利增长率约 6%，因此约需 **30 年**股票股利收益率才追上债券收益率
- **基金平均持有期**：mid-1960s 前约 7 年 → 现今略超 **1 年**
- **盈利意外**：约 **20%** 的 S&P 500 公司在典型季度仅超预期 **1 美分**；绝大多数盈利意外为正
- **会计选择案例**：Microstrategy 2000-03-20 宣布将 $12.8M 利润重述为约三倍亏损，市值单日蒸发超 **60%**；Priceline 全价法 vs travel agent 佣金法收入相差约 **6–7 倍**；IBM 1995 年收购 Lotus（$3.2B）时将超过一半计入 purchased in-process R&D
- **Big bath**：$4B 重组费用预提，实际成本仅约 $3B，留下 **$1B "cookie jar"** 储备
- **EG, Inc. 案例**：Sales $100、OpEx 85、pre-tax operating profit 15、tax 40% → NOPAT $9；cost of equity 12% → value $75M。投资 $7.5M 使 sales +10%、pre-tax margin 维持 15% → Sales $110、NOPAT $9.90 → value $82.5M − $7.5M = **$75M（不变）**。投资 $15M、sales +20%、增量 pre-tax margin 10% → Sales $120、NOPAT $10.20（earnings +13.33%）→ value ($10.20/12%) − $15 = **$70M（减少 $5M）**
- **EG vs Beta**：EPS 均 $9.00；EG P/E 8.3（cost of capital 12%）、Beta P/E 10（cost of capital 10%）；股价 $75 与 $90 均合理
- **三家 P/E 均 8.3 的公司**：成长增值者价值 $90（低估 $15）、毁灭者价值 $63（高估 $12）
- **ROE 时代变化**：mid-1990s 前很少有公司达到 20% ROE；1994 年以来 S&P Industrials 平均 ROE 超过 20%，此前三十年为低两位数
- **PEG 零增长特例**：EPS $10 永续、cost of capital 10%、零通胀 → 价值 $100、P/E 10；无限高 PEG 意味着无吸引力

### 决策规则与阈值

- **稳态 P/E = 1 / cost of equity**：只要给定股权成本，稳态倍数就被锁定，无需主观设定
- **倍数必须用 ROIIC 与 CAP 解释**：任何 P/E 都应对应一组（增长、ROIIC、CAP）组合；若无法反解，说明倍数脱离基本面
- **eCAP（extended competitive advantage period）判定标准**：足够高的初始 CFROI、slow fade、low CFROI volatility、asset growth 保持受控
- **市场长期性判据**：如果市场只用未来五年预期解释股价，说明倍数定价是短视的；**具备强竞争优势的公司值得超过 20 年的隐含预测期**
- **调查**：>99% 分析师使用某种倍数，<13% 使用 DCF；150 本教材的 ERP 区间为 3%–10%

### 常见错误与陷阱

- **循环论证**：用 `shareholder value per share = EPS × P/E` 求价值——"to estimate value we require an estimate of value"
- **把 P/E 当外生倍数**："the price-earnings multiple does not determine value; rather, it derives value. P/E analysis is not an analytic shortcut. It is an economic cul-de-sac."
- **盈利与股东价值的三重差异**：未扣资本成本、未扣支持增长所需的营运与固定资本投资、可用多种可接受的会计方法计算
- **三类盈利必须区分**：permanent（永久性）/ transitory（暂时性）/ value-irrelevant（与价值无关）——倍数对后两类毫无信息含量
- **高增长公司未必贵**：同一 15.0× P/E 可能来自三条完全不同的路径
- **EV/EBITDA 同样受单期盈利缺陷困扰**
- **忽略倍数的"覆盖损失"**：负盈利、负 FCF 公司会被剔除，样本选择偏差改变结论

### 逐字引文

> "Value of the firm = steady-state value + future value creation"（*What Does a PE Multiple Mean*, p.3）

> "Since 1961, the steady-state value has explained about two-thirds of the market's value, on average"（*What Does a PE Multiple Mean*, p.5）

> "This flawed logic underscores the fundamental point: the price-earnings multiple does not determine value; rather, it derives value."（*The Trouble with Earnings and Price/Earnings Multiples*, p.13）

---

## Capital Deployment：资本配置（股利、回购、并购与现金生命周期）

**来源**：*Thoughts on Dividends and Buybacks*（Credit Suisse GFS, 2016-05-03）；*Stock Buybacks Add or Destroy Value*（Credit Suisse Research, 2012-06-18；Zion, Varshney, Burnap）；*To Buy or Not To Buy: A Checklist for Assessing M&A*（Credit Suisse GFS, 2017-02-27）；*Cash & The Corporate Lifecycle*（Credit Suisse HOLT, 2010-09-24）

### 核心论点

**第一篇（股利与回购）**：股东回报的唯一决定因素是公司价值是否被正确理解——存在**价值守恒原则**（Value Conservation Principle）：无论股价高估还是低估，回购的买卖双方盈亏必然抵消，因此回购本身不创造价值，除非公司用低估的股票换回了更有价值的资产。

**第二篇（回购增值与否）**：回购是否创造价值，**完全取决于回购价格与内在价值的关系**；EPS 增厚（accretion）与价值创造（value creation）是两回事。**黄金法则**（Golden Rule of Share Buybacks）是判断标准。

**第三篇（并购清单）**：并购对买方的价值取决于 `协同效应现值 − 溢价`；溢价越高，买方承担的股东价值风险（SVAR）越大。作者提供可操作的 SVAR、premium at risk 与交易类型成功率清单。

**第四篇（现金与生命周期）**：现金的价值高度依赖公司所处的生命周期阶段；**代理成本**（agency costs）随盈余现金超出投资机会的程度上升。增长期把现金投进更高 CFROI 的项目创造价值，成熟期投进更低 CFROI 的项目毁灭价值。

### 公式与 worked numbers

**股利与回购：**

- `Total shareholder return = g + (1 + g)d`（g=7%、d=3% → TSR **10.21%**；对应一年 equity rate of return 10%）
- 股息只对价除权日价格：`Pb – Pa = D(1 – t_o) / (1 – t_cg)`
- **S&P 500 2015**：buyback yield 平均 **3.2%**，支出 **$572B**；dividend yield **2.1%**，支出 **$382B**；合并 payout 接近 **$1 万亿**；500 家中仅 **20 家**零收益率，众数总收益率 3–5%，近 **50 家**超过 10%
- **1982–2015 总股东收益率均值**：股利 **2.6%**、回购 **2.1%**、合计 **4.7%**；2015 年 5.3%（高于 10 年美债约 2%）
- **十年中九年回购额超过股利**（例外：2004Q4、2008Q4 及 2009 全年）

**回购增值与否（Zion）：**

- `Golden Rule`："A company should repurchase its shares only when its stock is trading below its expected value and when no better investment opportunities are available."
- **Goldilocks Inc. 示例**：cash $200 + PV of future CF $800 = intrinsic value $1,000；100 shares → $10/share
  - 股价 $8：用 $200 全额回购 → 买回 25 股，剩 75 股，每股内在价值 **$10.67（增值）**
  - 股价 $12.50 → 买回 16 股，剩 84 股，每股 **$9.52（毁损）**
  - 股价 $10 → 买回 20 股，剩 80 股，每股 **$10.00（中性）**
- **规模数据**：2004–2011 S&P 500 回购总额 **$2.7 万亿**（vs 股利 $1.8 万亿、capex $3.7 万亿）；估算产生 **$449B** 利润（含 **$231B** 股利）
- **回报分布**（460 家有回购公司）：306 家（**61%**）正回报，154 家（**31%**）负回报，40 家无回购；相对 **7%** cost of equity 基准仅 180 家（**36%**）跑赢；仅 98 家跑赢简单美元成本平均
- **评分卡基准**：月度高回报 4.1%（S&P 500 annualized return），10 年期国债收益率 1.6%
- **极端案例**：128 家公司年化回报 >10%；154 家负回报；AIG (51.7%)、Citigroup (33.9%)、Sprint (31.1%)、Bank of America (22.5%) 为最差；最佳 Dollar Tree 34.0%、CF Industries 32.6%、Visa 32.4%
- **IBM vs HP**：IBM 花 **$90B** 买 **8.10 亿股** → 年化 **+15.3%**；HP 花 **$61B** 买 **16.5 亿股** → 年化 **−11.3%**
- **集中度**：前 10 大买家占总额 **27%**（$730B），前 50 家占 **58%**（$1.6T）；IT 板块占 **23%**
- **管理层 vs 市场**：按月度均价买入为基准，管理层中位超额仅 **6 个基点**（胜 283 / 负 147）；按美元成本平均为基准，仅 **98 胜 332 负**
- **谨慎期**（月度占比最低十分位）中位回报 **5.9%**、标准差 17%；最高十分位中位 **4.8%**、标准差 9.1%
- **2007-05 与 2007-08** 各创纪录 **$66B** 单月回购，超过 2009 全年 $131B

**并购清单：**

- `Net present value of the deal for the buyer = present value of the synergies – premium`
- **SVAR（Shareholder Value at Risk）**：现金交易 = premium / 买方 equity market cap；换股交易 = premium / (买方 + 卖方合并市值，含溢价)。示例：买方 $2,000、卖方 $800，现金报价 $1,000（premium $200 = 25%）→ SVAR = **10%**；换股 → SVAR = $200/$3,000 = **6.7%**
- **Premium at risk**：现金交易为 **0**；换股交易示例为 **33.3%**（卖方仅实现 $133.33/$200 = 66.7% 溢价）
- **样本 126 笔**（2015–2016，买方市值 ≥$500M）：平均 SVAR **5.5%**、中位 **3.2%**，区间 −1.1% 至 27.6%；平均 premium at risk **16.1%**、中位 **9.3%**
- **协同折现**：tax $100 @ 30% → after-tax $70；@ 7% WACC → PV = **$1,000**
- **当前平均溢价 43%**（接近长期均值）
- **历史基准**：1995 年以来 M&A 规模平均为股票市值的 **8%**，2016 年同比下降 **17%**；Deal value added（McKinsey）过去 20 年平均约 **6%**，2016 年 **8%**，金融危机后均值近 **12%**；为买方创造价值的交易比例过去 20 年平均 **42%**（1997–2009 年 38%，2010–2016 年 50%）
- **Sirower & Sahni 300+ 笔交易**：初始正面 **103/302**；一年 TSR 初始正面组 **4.9%**、初始负面组 **−9.0%**
- **EPS 增厚无用**：样本中 86% 的交易 EPS 增厚；仅 **27%** 的增厚交易创造价值，**60%** 的摊薄交易中性或为正；NPV 公式准确率 **39%**
- **融资方式信号**：44% 现金、21% 股票、35% 组合；现金交易 51% 概率正 abnormal return，5 日平均 +0.7%；股票交易 70% 概率负异常收益，平均 **−3.9%**；组合交易 70% 负，平均 **−4.1%**
- **Clark & Mills 交易类型成功率**：Opportunistic **87–92%**；Operational bolt-on **80–85%**；Operational line extension **65–70%**；Transitional consolidation–mature **55–60%**；Operational multiple core-related **40–45%**；Transitional consolidation–emerging **37–42%**；Operational single core-related **30–35%**；Transformational lynchpin **20–25%**；Transformational speculative **15–20%**
- **案例 Expedia/Orbitz**：premium $360M，买方市值 $8,895M → SVAR 4.0%；premium at risk 0%；税后协同 $60M @ 6.4% → $943M；synergies − premium = **$583M**；实际 1 日异常收益 13.7%、3 日 12.0%、5 日 15.5%
- **案例 Centene/Health Net**：premium $1,039M，买方市值 $9,620M，卖方 $5,005M → SVAR 7.7%，premium at risk **28.7%**；税后协同 $86M @ 7.4% → $1,004M；synergies − premium = **−$36M**；实际 Centene 1 日 −8.0%、3 日 −13.4%、5 日 −11.3%

**现金与生命周期（Credit Suisse HOLT）：**

- **五阶段**：A Startup、B Growth、C Fade、D Mature、E Restructure
- **HOLT Life Cycle Framework 表**：Startup（CFROI below cost of capital、asset growth High、leverage Low、valuation High Premium）；Growth（CFROI Improving、asset growth High、leverage Low、valuation High Premium）；Fade（CFROI High、asset growth Slowing、leverage Relatively Low、valuation Declining Premium）；Mature（CFROI Around cost of capital、asset growth Low、leverage Increasing、valuation Average）；Restructure（CFROI Below cost of capital、asset growth Negative、leverage Typically high、valuation Discount）
- **决策树**：Stage C/D? → No: Grow；Yes: High Embedded Agency Costs? → Yes: Return Capital；No: Keep Agency Costs Low
- **市场给现金的定价**（Pinkowitz & Williamson, 2002）：$1.00 公司现金的市场价值在 **$1.19–$1.25** 之间，公司间差异从 **$0.26 到 $2.38**
- `Agency Costs ∝ Cash Surplus / (1 / Reinvestment Opportunities)`
- `PV_Suboptimal = Σ_{t=1}^{n} Cash Flow_t / [1 + (WACC + Agency Risk Premium)]^t`
- **三类再投资**：(1) 提高未来 CFROI 的再投资；(2) 带来更高整体未来 CFROI 的分拆投资；(3) 带来较低未来 CFROI 的再投资。市场回报最高者为 (1)，最差者为 (3)
- **实证**：宣布回购后短期股价正向影响 **−2/3%**（Grullon & Michaely 2002；Chou & Lin 2004）

### 决策规则与阈值

- **回购黄金法则**：仅当**股价低于内在价值**且**没有更好的投资机会**时才回购
- **"Doing nothing is doing something"**：不卖即提高持股比例
- **价值守恒原则**：公司价值 $1,000 派发 $200 后为 $800；高估回购使持续股东受损、低估回购使持续股东受益，卖方与买方盈亏抵消
- **三种回购动机学派**：fair value school、intrinsic value school、impure motives school（做高会计数字 / 抵消薪酬摊薄）。研究显示 repurchase intensity（净利润增速与 EPS 增速之差）与 TSR **无相关性**
- **事件类型信号**：资产扩张类事件（并购、增发、举债、银行贷款）后异常低回报；资产收缩类事件（分拆、回购、提前还债、启动分红）后异常高回报；同样适用于美国以外 **40 个市场**
- **M&A 判断顺序**：先定战略类别（Clark & Mills 表）→ 再算 SVAR 与 premium at risk → 再算协同现值 → 最后用 `synergies − premium` 判定；**EPS 增厚不构成理由**
- **现金分配可驱动股价的两个条件**：(1) 股价已隐含 agency risk premium；(2) 市场视分配为管理层将降低 agency costs 的可信信号
- **投资者四项考量**：(1) 公司生命周期阶段；(2) 投资者预期；(3) 管理层资本计划；(4) 可信度

### 常见错误与陷阱

- **把回购当成价值创造**："doing nothing is doing something"——不回购本身就是一种决策
- **用 EPS 增厚证明回购有效**：61% 正面回报，但相对 7% 股权成本基准只有 36% 跑赢
- **用美元成本平均评价回购**：只有 98 家胜 332 负；管理层相对月度均价的超额仅 6 个基点
- **在高估价位回购**：Goldilocks 案例中 $12.50 买入直接毁损每股价值至 $9.52
- **忽略溢价规模**：Centene/Health Net 案例中 premium at risk 达 28.7%，协同现值反而不足以覆盖溢价（−$36M）
- **以 EPS 增厚作为并购理由**：86% 交易增厚，仅 27% 创造价值，NPV 公式准确率仅 39%
- **忽视股票对价的市场信号**：股票交易 70% 概率负异常收益、平均 −3.9%
- **在成熟期过度投资**：Mature 阶段再投资于较低 CFROI 项目显著毁损价值
- **忽视代理成本随盈余现金上升**：现金越多、投资机会越少，agency risk premium 越高，股价折价越大
- **债券持有人视角被忽略**：Pinkowitz & Williamson (2002) 将股东/债券人冲突视为现金折价的重要决定因素；Jensen 控制假说中的"债务创造"（debt creation without retention of proceeds）

### 逐字引文

> "There is a value conservation principle associated with buybacks."（*Thoughts on Dividends and Buybacks*, p.1）

> "A company should repurchase its shares only when its stock is trading below its expected value and when no better investment opportunities are available."（*Stock Buybacks Add or Destroy Value*, p.7）

> "Net present value of the deal for the buyer = present value of the synergies – premium"（*M&A Assessment Checklist*, p.9）

> "The market rewards reinvestment into higher CFROI projects and punishes investment into lower CFROI projects."（*Cash & The Corporate Lifecycle*, p.5）

---

## SBC：股票薪酬会计（PWC 指南）

**来源**：*PWC on Stock Based Compensation*（PWC 股票薪酬会计指引，部分内容 2022-01 更新，共 269 页）

### 核心论点

本篇是**会计与准则层面的操作手册**，而非投资观点。核心是 ASC 718 的计量与归集规则：所有类型的 SBC 均按授予日（grant date）公允价值计量，费用在归属期内系统化归集；归属条件（vesting conditions）、绩效条件（performance conditions）、市场条件（market conditions）的处理各不相同；奖励修改（modification）会触发不同的会计处理类型。

### 框架与数字

- **计量基础**：ASC 718 要求 **fair-value-based method**；计量对象（measurement objective）是**授予日公允价值**，假设员工满足归属条件并保留奖励。多数奖励成本在授予日计量一次，之后不因公允价值变化调整
- **三步估值法**：
  - Step 1：可观察的相同工具市场价格
  - Step 2：可观察的类似工具市场价格
  - Step 3：若无相同/类似工具，则使用**期权定价模型**（Black-Scholes、lattice/binomial），且须符合 ASC 718 计量目标、基于成熟经济理论、被专家普遍认可、能反映除 ASC 718 明确排除项（如 reload features）之外的全部实质特征
- **受限股票 / RSU**：公允价值一般按授予日股价；若员工在归属前不得收取股利，则按适当无风险利率折现归属期内预期股利以减少公允价值；归属期内已付或累积支付的不减少
- **Graded vesting（ASC 718-10-35-8）二选一**：**graded vesting (accelerated) method** 或 **straight-line method**。straight-line 下的 **"floor"** 要求：截至任一报告日已确认费用**不得低于已归属部分的 grant-date fair value**。含市场条件或业绩条件时**必须**使用 graded vesting 方法；仅含服务条件时可用 straight-line
- **示例**：4 年服务期 straight-line 每年确认 25%；例中 100 份期权、25% 法定归属，某时点 straight-line 已确认少于 floor
- **Performance conditions**：按 **probable** 确认费用；每个报告期重估归属概率并作 **cumulative catch-up adjustment**（ASC 718-10-55-78/55-79）；多个可能结果时分别计算各结果的 grant-date fair value，按 probable 结果确认
- **Forfeiture rate**：采用历史 forfeiture rate（示例 SC Corporation 估计 **5%** 年度 forfeiture rate）；实际未归属 55% 时须作 true-up；可按员工群体分组并平均历史年度 forfeiture rate
- **Modification（ASC 718-20-35-2A）**：仅当 (1) 公允价值、(2) 归属条件、或 (3) 权益/负债分类发生变化时适用修改会计
- **权益分类奖励修改四步**：(1) 计算增量公允价值（修改后 vs 修改前）；(2) 对已归属部分立即确认增量价值；(3) 在剩余必要服务期内**前瞻性**确认增量成本 + 尚未确认的原奖励成本；(4) 修改后确认的 total compensation cost 最低**不低于**原奖励的 grant-date fair value
- **Type I（probable-to-probable）**：累计确认 = 原 grant-date fair value + 增量公允价值；原 grant-date fair value 为 "floor"
- **Type II（probable-to-improbable）**：在修改条件下归属变为 probable 前不确认增量公允价值；若原归属条件满足则确认原 grant-date fair value
- **Type III**：仅归属条件实质未变而仅估值方法改变（如从 Black-Scholes 改为 lattice），不产生增量费用确认
- **负债分类奖励修改**：每期按公允价值重测，**无 "floor"**，总费用等于结算日公允价值
- **SAB 120（2021-11）**：spring-loaded awards 需考虑是否调整可观察股价与预期波动率

### 决策规则与阈值

- **归属条件判断**：仅服务条件 → 可用 straight-line；含市场/业绩条件 → 必须 graded vesting
- **floor 检验**：straight-line 下的累计已确认费用在任一报告日不得低于"已归属部分 × grant-date fair value"
- **probable 门槛**：业绩条件按 probable（而非 expected）确认，并在后续报告期重估
- **forfeiture rate 更新**：实际 forfeiture 与估计偏离时必须 true-up

### 常见错误与陷阱

- **在授予日之后按公允价值调整费用**——ASC 718 明确多数奖励成本在授予日一次性计量
- **在 straight-line 方法下忽略 floor**：可能少计费用
- **对含市场条件或业绩条件的奖励误用 straight-line**
- **混淆 Type I / II / III**：Type II 下过早确认增量公允价值会虚增费用
- **负债分类奖励误用 floor 概念**：负债分类按公允价值逐期重测，不设下限
- **对无合理估值的情形擅自切换方法**：即使后来可估计，也须持续使用内在价值法直至结算
- **忽略 performance condition 概率的逐期重估**：不做 cumulative catch-up adjustment 会导致费用错配

### 逐字引文

> "ASC 718 principally requires the use of the “fair-value-based method” for measuring the value of stock-based compensation."（*PWC on Stock Based Comp*, p.19）

> "companies use an option-pricing model adjusted to accommodate the unique characteristics of employee stock options"（*PWC on Stock Based Comp*, p.19）

> "for awards with graded vesting features, companies will use either a graded vesting (accelerated) or straight-line attribution approach to recognize compensation cost over the vesting period"（*PWC on Stock Based Comp*, p.55）

---

## 10-K Navigation：10-K 财报导航（Wolfe Research）

**来源**：*10-K Navigation Guide*（Wolfe Research, 2020-02-25；Senyek, Calingasan, Miller，共 229 页）

### 核心论点

这是一份**自下而上的财报排雷手册**，覆盖 40+ 项 10-K 披露，重点关注六项：Reverse Factoring（反向保理）、M&A Accounting（并购会计）、Leases（租赁）、Taxes（税务）、Revenue Recognition（收入确认）、Cash Flow（现金流）。配套一个经验预测力很强的 **EQ Score**（Earnings Quality Score）七指标模型，用于识别盈利质量差的公司（跑输或做空候选）。

### 框架与数字

- **申报截止**：Large Accelerated Filers（public float ≥$700M）年末后 **60 天**（2020 日历年公司为 3 月 2 日）；Accelerated Filers（$75M–$700M）**75 天**；Non-accelerated（<$75M 或当年 IPO）**90 天**；SEC rule 12b-25 允许 **15 个日历日**延期（Form 8-K 或 NT-10-K）
- **Reverse factoring（RF / supply chain finance）机制**：公司作为买方把应付供应商账款转给银行；银行通常 **10 天内**付供应商并取得早付折扣，公司对银行的付款期限 **180 天甚至 364 天**。示例：$100 采购、正常 60 天付款周期 → 180 天 RF 下应付余额变为 **$300**，即 **$200 的"超额"现金流实为融资**。银行端若期限 ≤ 364 天 RWA 也低
- **RF 的经济合理场景**：公司信用等级 **A 级及以上**且供应商信用较差；期限 364 天及以下时银行 RWA 较低
- **成本资本化检查阈值**：其他流动资产 > 总流动资产 **5%**、其他非流动资产 > 总资产 **5%**、递延成本 > 总资产 **5%** 需年报披露；`Average Asset Depr. Life = Gross PP&E / Depreciation Expense`；`Sales to PP&E Ratio = Total Sales / Gross PP&E`。作者偏好**摊销期 < 3 年**的资本化成本
- **准备金（cookie jar / big bath）三查**：1) 准备金余额的"机会"（数量与深度，与收入及 A/R 比较）；2) 是否有准备金冲回计为收益；3) 是否少提准备金以虚增当期利润
- **资产负债表 10 项检查**：现金因一次性汇回税高估、JV/权益法表外风险、表外担保、短期租赁低估租赁负债、商誉/无形高估、LIFO vs FIFO、应收账款证券化表外融资、reverse factoring 表外融资、递延税资产高估、递延所得税负债相当于权益
- **现金流 16 项检查**：推迟 A/P 支付（即 reverse factoring）、高现金流期预付费用、递延收入一次性拉高应收、应收账款证券化、成本资本化与分类、新资本租赁绕过现金流、低现金税率、股票薪酬、并购后营运资本收益、准备金冲回形成非现金收益、连续并购者 M&A ~ capex、少数股东对经营现金流的索取权、用公司股票缴养老金、应计 capex 绕过现金流、与 IFRS 公司的分类差异
- **现金税率两种算法**：(1) `Cash taxes paid / GAAP income before taxes`；(2) `Current income tax provision / GAAP income before taxes`（作者在现金税异常高低时更偏好第二种）。**Skyworks 案例**：cash taxes paid $163M/$136M/$124M，EBT $1,257M/$1,332M/$961M → 13%/10%/13%；current tax expense $240M/$379M/$109M → 19%/28%/11%
- **低现金税率的可疑来源**：SBC "excess" tax benefits（股价不涨会反转）、100% bonus depreciation "boomerang"、利息抵扣上限（**2022 年由 EBITDA 的 30% 改为 EBIT 的 30%**）、BEAT 从 5% 升至 **10%**（2019）、TCJA 限制高管薪酬抵扣、**2022 年起 R&D 需资本化摊销**、汇回税分 8 年缴纳（偏后）、2018 年大额养老金缴款仍享 35% 税盾
- **Bonus depreciation**：TCJA 允许 100% capex expensing 至 **2022 年**，之后每年递减 **20%**
- **EQ Score 七指标**（均以 LTM 计算，↑ 多数代表盈利质量下降）：
  1. `Current Accruals = (NI − CFFO) / LTM Revenue`
  2. `Change in Working Capital = 现金流量表营运资本科目变动 / LTM Revenue`
  3. `Total Accruals = (NI − CFFO − CFFI) / LTM Revenue`
  4. `Tax Rate = Taxes paid / Earnings Before Taxes`
  5. `Other Asset Growth = Change in Other Total Assets / LTM Revenue`
  6. `Operating vs. GAAP Earnings = 过去 12 个季度中 Non-GAAP "Operating" EPS 至少高出 GAAP 10% 的季度数`
  7. `High Cap-Ex = LTM Cap-Ex / PP&E`
- **附加负面信号**：Industry Group Specific Quality Risk（1 最低–5 最高，按历史预测力打分）；`M&A Risk = (goodwill + intangibles 同比最大增幅) / 当前市值`（**top 20%** 为负面）；Non-GAAP/Pro Forma Earnings（连续 12 季度中超过 10 个季度调整项抬高 GAAP 盈利至少 **10%**）；CFO Changes；Sales & Earnings Growth Acceleration/Deceleration；Working Capital Changes；WR Governance Grade（Staggered Board / Poison Pill / Dual CEO-Chairperson / 低独立董事比例 / 较大董事会 / Clawback Provision）
- **EQ Score 计算**：各分项在行业内打 **1–10 十分位**（等权相加得 raw score），再与行业内比较得 **0–100** 的最终 EQ 分数（**0 最差**）
- **DSO / DIO 监控**：`% Change in DSO = DSO Current / DSO One-year Ago`，`DSO = Accounts Receivable / Most recent quarter Sales × 90`；`% Change in Days Inventory = Days Inventory Current / Days Inventory One-year Ago`，`Days Inventory = Inventory / Most recent quarter COGS × 90`。变化最小（下降）的公司跑赢同业；变化最大（上升）的公司跑输（落在第 5 分位）

### 决策规则与阈值

- **RF 尽调触发条件**：A/P 余额增速显著快于收入增速 → 立刻核查是否存在反向保理
- **成本资本化检查阈值 5%**：任何一项超过 5% 即需在年报附注中核对
- **EQ Score 0–100**：**分数越低盈利质量越差**；结合七指标得分与附加负面信号筛选做空候选
- **M&A Risk 阈值 top 20%**：商誉与无形资产的同比增幅/市值落入行业最差 20% 即为负面信号
- **Non-GAAP 调整阈值 10%**：单季 Non-GAAP 高出 GAAP 10% 计入指标六；连续 12 季度中超过 10 个季度如此则为独立负面信号
- **DSO / DIO 变化方向**：**变化最小者跑赢，变化最大者跑输**（落在第 5 分位）
- **申报截止日利用**：60/75/90 天 + 15 天延期的窗口决定财报季的信息获取节奏

### 常见错误与陷阱

- **把反向保理当成经营现金流**：这是"short-term debt disguised as accounts payable"，最坏情形会触发流动性危机
- **RF 的流动性风险**：额度一旦收紧须立即偿付以解约——恰在公司最困难时发生；供应商可能要求恢复 60 天甚至 10 天账期
- **RF 会计处理无明确规则**：各公司处理分歧，多数视为"非事项"继续计入应付账款
- **成本资本化绕过现金流量表**：把费用资本化可同时提升利润与经营现金流
- **Bonus depreciation 造成的现金税率假象**：2022 年后递减 20%，会人为压低现金税率并造成"boomerang"
- **SBC excess tax benefits 的反转**：股价下跌时该税收利益消失，现金税率会跳升
- **Big bath 与 cookie jar**：一次性大额计提后再通过准备金冲回平滑利润
- **其他资产相对收入增加**：历史上预测股价跑输的指标之一
- **GAAP 与 IFRS 分类差异**：不做调整直接横向比较会产生假信号

### 逐字引文

> "Reverse factoring (RF) is short-term debt disguised as accounts payable and is artificially boosting cash flow."（*10-K Navigation Guide*, p.1）

> "We find spotty disclosures, and RF could create a liquidity crisis in a worst-case scenario."（*10-K Navigation Guide*, p.1）

> "M&A accounting continues to be a broad area of accounting abuse and was an early warning signal at Kraft-Heinz."（*10-K Navigation Guide*, p.1）

---

## 附：行业 primer 库索引

延伸阅读库位于课件包的 Module 1–15 各 `Supplemental Reading` 目录。其中**行业 primer 库**位于 `Module 8-Industry Coverage/Industry Primers/`。

该目录实测 **98 份 PDF**（文件名均含机构与年份，如 `Global Oil & Gas Industry Primer - UBS (2004).pdf`），覆盖领域包括：

| 领域 | 代表文件 |
|---|---|
| 航空航天 | Aerospace Industry Overview - Stout Risius Ross (2011)；Global Aerospace Market and Forecast - Deloitte (2010) |
| 农业与化肥 | Agricultural Opportunities - Credit Suisse (2007)；Global Fertilizers Industry Primer - UBS (2008)；Potash 101 - UBS (2009)；North America Fertilizers Primer - UBS (2006) |
| 航空 | Airline Industry Overview - Regional Airline Association (2010)；Airlines 101 - ESG Aviation Services (1998)；US Airlines - Air Transportation Association (2011) |
| 银行 | Banking 101 - Large Cap Bank Primer - Deutsche Bank (2011)；Global Banking - Ceres (2008)；Global Banking Outlook - UBS (2010)；Profiles of US Banks - Ceres (2008)；Loan Market Guide - S&P (2011) |
| 清洁科技与电动车 | Clean Tech Industry Primer - Jefferies (2008)；US Cleantech Primer - Barclays (2011)；Electric Cars - Deutsche Bank (2008/2009) |
| 煤炭与商品 | Coal 101 - UBS (2009)；Commodities Primer - RBS (2009)；Global Commodities Primer - RBS (2009) |
| 铜与金属 | Copper - Scotia Capital (2006)；Japan Metals Update - UBS (2010) |
| 电力与公用事业 | Electric Utilities Industry Overview - Morgan Stanley (2010)；Electric Utilities Primer Vol. II - Jefferies (2007)；Electric Utilities and Power Industry Primer - Oppenheimer (2009)；Electricity Futures & Other Derivatives - Berkeley National Laboratory (1998)；Utilities and Power Industry Update - Deutsche Bank (2010) |
| 能源与油气场 | Global Energy Industry Primer - Credit Suisse (2012)；Global Energy Outlook 2012 - Platts (2011)；Caterpillar Oil & Gas Primer - Morgan Stanley (2011)；Global Gas Industry - Credit Suisse (2011)；Oil & Gas Basics - JP Morgan (2008)；Oil & Gas Production Handbook - ABB (2010) |
| 食品饮料 | Global Food & Beverage Primer - IMAP (2010)；Canadian Food Retail Sector - OSEC (2011) |
| 黄金与贵金属 | North America Gold Producers Primer - UBS (2009)；Global Energy / Gold Producers（Credit Suisse / UBS） |
| 医疗与制药 | US Healthcare Industry Primer - Morgan Stanley (2011)；European Pharmaceuticals - Deutsche Bank (2010)；Global Pharmaceuticals - Deutsche Bank (2005)；M&A in the Pharmaceutical and Biotech Industries - NBER (2004) |
| 保险与再保险 | Health Insurance Industry Market Structure - Congressional Research Service (2010)；Reinsurance Primer - Swiss Re |
| 钢铁与铁矿 | Global Steel Primer - RBS (2010)；Steel Industry Primer - Credit Suisse (2011)；Global Mining & Steel Primer - UBS (2008)；Japan Metals Update |
| 奢侈品与消费 | China Luxury Primer (Dipped In Gold) - CLSA (2011)；Consumer 相关见 Global Food & Beverage / Canadian Food Retail |
| 矿业 | Metals & Mining Industry Primer - Credit Suisse (2009)；Mining Industry Report - Deloitte (2010)；Mining Glossary - ABN AMRO；Valuation of Metals and Mining Securities - Basinvest (2010) |
| 稀土与战略性矿产 | Rare Earth Elements Industry Primer - Jacob Securities (2011)；China Rare Earth Elements Industry Primer - IAGS (2010) |
| 炼化与页岩气 | US Shale Gas Industry Primer - US DOE (2009)；Global Oil & Gas Primer - Credit Suisse First Boston (2002) |
| 半导体 | Semiconductor Industry Primer - Oppenheimer (2011)；Semiconductor Industry Primer - Wachovia (2008) |
| 电信与互联网 | Global Telecom Primer - Morgan Stanley (1999)；Broadband Wireless Industry Primer - Near Earth LLC (2007)；Internet Sector Initiation - JP Morgan (2011)；Mobility 2020 - Jefferies (2011) |
| 卡车运输 | Trucking Industry Primer - Transportation Research Board (2010) |
| 铀 | Uranium 101 - UBS (2009) |
| 水务 | Water Sector Primer - Goldman Sachs (2005)；Water Sector Investing - Goldman Sachs (2008) |
| 区域市场与宏观 | Asia Middle Class - CLSA (2007)；China Cement / Energy / Industrial primers；Vietnam Economic Outlook / Retail；Demographics and Asset Prices - Credit Suisse (2012)；Global Industry Trends - Stockcube (2011) |
| 金融结构与另类资产 | Islamic Finance Primer - CFA Institute (2009)；Sovereign Wealth Funds Primer - JP Morgan (2008)；Master Limited Partnerships（Wachovia 4 版 / Credit Suisse）；Global Financial Advisory M&A Rankings - Bloomberg (Q1 2012） |

---

## 附：写报告时的公式速查

| 用途 | 公式 |
|---|---|
| ROIC | `NOPAT / 投入资本 (Invested Capital)` |
| NOPAT | `EBITA − 现金税`（实务近似 `EBITA × (1 − 税率)`） |
| 投入资本（经营法） | `净营运资本 + 净固定资产 + 商誉 + 其他长期经营资产` |
| 投入资本（融资法） | `短期债务 + 长期债务 + 其他长期负债 + 优先股 + 普通股权益` |
| 经济利润 | `(ROIC − WACC) × 投入资本` |
| FCF | `NOPAT − 对未来增长的投资（≈ Δ投入资本）` |
| FCFE | `净利润 + D&A + 非现金项 − ΔNWC − Capex − 现金收购 + 债务净流入` |
| FCFF | `EBIT × (1 − t) − ΔNWC − (Capex − D&A) − 其他再投资` |
| Ke | `Rf + β × ERP` |
| WACC | `Ke × E/V + Kd × (1 − t) × D/V` |
| 杜邦式 ROIC | `(NOPAT / 销售额) × (销售额 / 投入资本)` |
| ROIIC | `(本年 NOPAT − 上年 NOPAT) / (上年投入资本 − 上上年投入资本)` |
| 再投资率 | `增长 / 增量ROIC` |
| 价值创造 | `ΔNOPAT − WACC × Δ投入资本` |
| 隐含稳态利润率 | `(现价 × 股数) / (1 − t) / NTM收入`（对目标 P/E 反推） |
| PSUC | `Upside / (Upside + |Downside|)` |
| 增长与 ROIC（简化） | `增长 = ROIC × (1 − 派息率)` |

---

## 附：跨文献的共识（写报告时可直接引用）

1. **现金创造能力是价值的基础**：只有 ROIC 超过 WACC 才有价值创造 `[Calculate ROIC]`
2. **回报均值回归是基准率**，模型必须尊重；高回报不会永续 `[Calculate ROIC]` `[Measuring the Moat]`
3. **FCF 口径必须先说清归属**（FCFE vs FCFF）；**SBC 不得加回** `[A Primer on FCF]` `[PWC on SBC]`
4. **倍数是速记而非估值**，必须回到 DCF 经济学 `[Common Errors in DCF Models]` `[What Does a PE Multiple Mean]`
5. **DCF 的两大硬标准**：经济合理（economically sound）+ 透明（transparent） `[Common Errors in DCF Models]`
6. **资本配置的核心是"对股东回报率"，不是"返还了多少现金"** `[Thoughts on Dividends and Buybacks]` `[Stock Buybacks Add or Destroy Value]`
7. **大额并购的协同兑现要打折**——"7 times out of ten, napkin math has failed" `[M&A Assessment Checklist]`
8. **终值归零估值是识别"融化冰块"的最快方法** `[Measuring the Moat]`（见 `06-industry-and-management.md` A8）

---

> 来源：Fundamental Edge 买方培训课件配套延伸阅读（Mauboussin / Damodaran / Wolfe Research / Credit Suisse / PWC / Zion / Bear Stearns）。方法论引用，不构成投资建议。
