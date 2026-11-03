# fundamental-edge

> **Language**: [中文](README.md) · [English](README.en.md)

A buy-side fundamental research methodology skill — turning "look at a stock" into a **repeatable, auditable, handover-ready** research pipeline.

Ships with **4 zero-dependency calculation scripts** (DCF / Reverse DCF / ROIC / Risk-Reward) and **12 methodology references** (~820k characters, every rule page-cited to its source).

```
Business → Industry → 3 Key Drivers → Model → Expectations Gap → Valuation
   → Bull/Base/Bear · Risk-Reward · Sizing → Catalysts → Thesis → Pitch → Monitoring
```

> Methodology notes, **not investment advice**. Not affiliated with the original course author. See [Provenance](#provenance).

---

## The stance

**Price is a FCF forecast. Fundamental research is not about finding truth — it's about finding the expectations gap.**

The market is right most of the time. Repeatable alpha comes from three things compounding:

```
Solid foundational skills  →  Rigorous repeatable process  →  Judgment earned in the field
```

Operationally, three rules:

| Principle | What it means | The failure mode it prevents |
|---|---|---|
| **Write the market's view first** | Use reverse DCF to back out what the price already implies | Hunting for evidence to support a conclusion you already hold |
| **Risk before reward** | "Take care of the risk case and the reward will take care of itself" | Modelling only the upside |
| **Terminal value < 25% of NPV** | Beyond that, the conclusion is a function of assumptions, not of valuation | Arguing off a perpetual growth rate 30 years out |

---

## Install

```bash
git clone https://github.com/easonyeung1122-ops/fundamental-edge.git \
  ~/.codebuddy/skills/fundamental-edge
```

Or drop it into `~/.workbuddy/skills/` (WorkBuddy user-level) or `.codebuddy/skills/` (project-level).

Scripts use **Python standard library only** — no `pip install`. On Windows use `py -3`; on macOS/Linux use `python3`.

---

## Layout

```
fundamental-edge/
├── SKILL.md                              # Entry point: main workflow, script index, hard numbers, boundaries
├── references/                           # 12 methodology references, organised by module
│   ├── 01-foundations-and-process.md     # M1 Foundations + M2 Life on the buy-side
│   ├── 02-thesis-development.md          # M3 Thesis development (ETIK→KD→VB→EP)
│   ├── 03-stock-drivers-and-ideas.md     # M4 What moves stocks + M5 Idea generation
│   ├── 04-modeling.md                    # M6 Modelling (9 forecasting frameworks)
│   ├── 05-business-analysis.md           # M7 Business analysis (moat / ROIC / FCF)
│   ├── 06-industry-and-management.md     # M8 Industry + M9 Management & capital deployment
│   ├── 07-expectations.md                # M10 Expectations & reverse DCF
│   ├── 08-valuation.md                   # M11 Applied valuation
│   ├── 09-short-selling.md               # M12 Short selling
│   ├── 10-earnings-and-pitch.md          # M13 Earnings season + M14 Pitch like a pro
│   ├── 11-portfolio-and-risk.md          # M15 Portfolio construction & risk
│   └── 12-supplemental-reading.md        # Supplemental readings (Mauboussin / Damodaran et al.)
└── scripts/
    ├── dcf.py                            # DCF + cost of capital build + sensitivity
    ├── reverse_dcf.py                    # Market-implied assumptions + expectations gap
    ├── roic.py                           # ROIC / value creation / reinvestment sensitivity
    ├── riskreward.py                     # R/R / PSUC / return ladder / sizing / exposure
    ├── extract_course_pdf.py             # Look up the source course PDFs (bring your own library)
    └── verify_skill.py                   # Skill integrity self-check
```

---

## Quick start

### 1. DCF with a full cost-of-capital build

```bash
py -3 scripts/dcf.py --csv fcff.csv --build-wacc \
  --rf 0.045 --beta 1.0 --erp 0.05 --kd 0.06 --tax-rate 0.25 \
  --equity-weight 0.70 --debt-weight 0.30 \
  --terminal-growth 0.025 --net-debt 500 --shares 100 --eps 1.85 --price 18 --sensitivity
```

Actual output (excerpt):

```
### Cost of capital
| Cost of equity Ke     |  9.50% |
| After-tax cost of debt|  4.50% |
| WACC                  |  8.00% |

### Valuation bridge
| PV of explicit FCF    |   527.00 |
| PV of terminal value  | 2,218.36 |
| Enterprise value      | 2,745.36 |
| Equity value          | 2,245.36 |
| Value per share       |    22.45 |
| TV as % of NPV        |  80.80% (**over limit**, target <25%) |
```

The terminal-value warning is the single most useful built-in discipline: it tells you when your answer is driven by the terminal assumption rather than by the forecast.

### 2. Back out what the market is assuming

```bash
py -3 scripts/reverse_dcf.py --csv fcff.csv --price 22.45 --shares 100 \
  --net-debt 500 --solve all --wacc 0.08 --internal-value 30
```

```
| Market-implied perpetuity growth g |  2.50% |
| Market-implied WACC                 |  8.00% |
| Market-implied terminal multiple    | 18.63x |
```

Add `--internal-value 30` to get the **expectations gap** directly: the market is paying 22.45, you think it's worth 30 — a 34% gap.

`--solve margin` back-solves the market-implied **steady-state operating margin** given a revenue path and a target P/E.

### 3. ROIC and value creation

```bash
py -3 scripts/roic.py --ebit 500 --tax-rate 0.25 --nwc 100 --net-fixed-assets 800 \
  --wacc 0.08 --delta-nopat 60 --delta-ic 200 --growth 0.10 --reinvestment-sensitivity
```

Outputs ROIC, tangible ROIC, the **ROIC−WACC spread in bps**, value created, incremental ROIC,
implied reinvestment rate, and a reinvestment-rate sensitivity table that reproduces the course's published figures.

### 4. Risk-reward, sizing and PSUC

```bash
py -3 scripts/riskreward.py --price 100 --target 140 --stop 85 \
  --ntm2-eps 8.5 --ntm2-pe 22 \
  --scenario "bull:150:0.30,base:110:0.50,bear:70:0.20" \
  --portfolio-value 1000000 --risk-pct 0.01
```

```
| Upside   |  40.00% |
| Downside |  15.00% |
| R/R      |  2.67x |
| PSUC     | 72.73% |
| Verdict  | Positionable (threshold ≥2.0x, ≥3.0x = slam-dunk) |
```

**PSUC** = upside ÷ (upside + |downside|) — "how much does this bet look like a coin flip."
Reference anchors: coin flip 50% / merger arb 83.3% / 10:1 biotech 9.1%.

All scripts support `--format md|tsv|both`; TSV pastes straight into Excel.

---

## Verified anchors

The scripts aren't hand-waved — they were round-trip validated against worked examples published in the course:

| Check | Expected | Actual |
|---|---|---|
| WACC build | Ke 9.5% × 70% + after-tax Kd 4.5% × 30% = **8.0%** | Match |
| Reverse DCF round-trip | Input g=2.5% / WACC=8% → solves back to **2.50% / 8.00%** | Match |
| Implied terminal multiple | DCF forward 18.63x vs reverse-solved 18.63x | Match |
| Reinvestment sensitivity | $10 over 3 years → **$17.28 / $13.31 / $11.58** | Match |
| P/E with terminal value zeroed | **4.7x** | Match |

`scripts/verify_skill.py` runs a one-shot integrity check: frontmatter, reference index vs. disk, page citations present in every reference, scripts compile.

---

## Hard numbers (do not alter)

These are the methodology's anchors. Any write-up must align with them:

| Number | Meaning |
|---|---|
| **25–35 years** | Years of FCF discounting needed to justify a typical stock price (equity duration) |
| **55x / 27x / 16x / 11x / 8x** | Implied P/E at 4% / 7% / 10% / 11% / 12% cost of equity |
| **< 25%** | Terminal value as a share of NPV — the ceiling |
| **22–30x / 14–17x / 8–10x** | Fair P/E for 8–10% / 4–6% / zero growth |
| **16x → 31x** | Fair P/E expansion when growth goes 5% → 10% for 10 years |
| **16x → 26x** | Margin expansion of +100bps/yr for 5 years |
| **16x → 21x** | Capex falling from 3% to 1% of sales |
| **4.7x** | Where P/E collapses to if terminal value is zeroed |
| **65 hours** | Due-diligence hours for one idea from scratch |
| **300 → 30 → 3** | The idea funnel |
| **5–7%** | Initial guidance cushion on first guide |
| **26%** | Typical analyst EPS dispersion |
| **75%** | Share of daily return variance that is not stock-specific |
| **3–5%** | Alpha needed to overcome a 2-and-20 fee |
| **≥ 2.0x / ≥ 3.0x** | R/R threshold to position / slam-dunk threshold |
| **2.5–20%** | Short borrow cost range |
| **≤ 50bps** | Max portfolio loss tolerance on a single short |

---

## The six-step process

| # | Step | Deliverable |
|---|---|---|
| 1 | Opportunity assessment | What's already priced in; how big is the alpha load |
| 2 | Business analysis & modelling | Build the model; judge business momentum and potential revisions |
| 3 | Key driver assessment & deep dive | Isolate the **3 key drivers**; build differential insight |
| 4 | Case construction & risk-reward | Bull/base/bear; is the R/R sufficient |
| 5 | Thesis construction & communication | Structured argument, pitched to a PM |
| 6 | Monitoring & catalyst assessment | Catalyst calendar; is the thesis still on track |

**Skipping a step is an error** — you can't validate a conclusion before you've built the model, and you can't voice a view before you've quantified the risk-reward.

Thesis chain: `ETIK (Everything There Is To Know) → KD (3 Key Drivers) → VB (Value Belief) → EP (Entry Point)`

Every thesis must answer three questions:

1. **"Get me up to speed"** — explain the business in 3 minutes
2. **"Where are we different & why"** — where's the disagreement, and why are we right
3. **"What is our path to getting paid"** — what closes the gap

Fail questions 2 and 3 and it isn't a thesis, it's a story.

---

## Common failure modes

| Failure | Consequence | Constraint |
|---|---|---|
| Conclusion first, evidence second | The thesis becomes a story | ETIK before KD |
| Voicing a view before quantifying R/R | You can't answer the first PM question | Scenarios and PSUC first |
| Terminal value dominates NPV | The answer is set by the assumption | < 25% |
| Inconsistent EPS definition | P/E can be off 26% (17.5x vs 23.7x) | One definition throughout |
| Long/short logic with no disqualifiers | You hold losers too long | Gauntlet of Disqualifiers |
| No catalyst path | "Getting paid" is unanswerable | Must state the path |
| Model disconnected from the thesis | The model doesn't drive the conclusion | The model is the thesis's spine |

---

## Provenance

The methodology originates from the **Fundamental Edge** buy-side training curriculum (Brett Caughran).

This repository is an **independent, restructured set of notes and re-expression** of that methodology:

- It contains **none** of the course's original PDFs, Excel templates, or source files
- It **does not reproduce** whole chapters; short quotations are used only to illustrate a concept, with page numbers
- The 12 references reorganise the course's frameworks, criteria and thresholds into executable notes, augmented with independently derived worked examples and script implementations
- **All rights to the original course material remain with its author. If you want to study it properly, buy the course**

The companion Excel templates (canonical MOD row order, DCF scenario tables, NVDA/NFLX/WGO worked models) are **deliberately excluded** — they are the course's original distribution files. `SKILL.md` §4 documents the canonical MOD row order and the `SUM` tab structure in text, so you can rebuild them yourself.

Supplemental readings (Mauboussin / Damodaran / Wolfe Research / Credit Suisse / PWC / Zion / Bear Stearns) are likewise **argument summaries and formula digests**, not reproductions. Rights remain with their respective authors.

## License

Code under `scripts/`: **MIT**.
`references/` and `SKILL.md` documents: personal study use only; not for resale or redistribution as a paid product.

Per-source attribution is in [NOTICE.md](NOTICE.md).

---

> Methodology research, **not investment advice**. All worked examples are illustrative and do not correspond to recommendations on any real security.
