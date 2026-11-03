#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Reverse DCF —— 反推市场隐含假设（Fundamental Edge Module 10 / Module 3）

核心原则：
  * 价格是一个 FCF 预测（Price is a FCF forecast）
  * Expectations Gap = 市场观点 − 内部观点（M1 p.91-92）
  * 先写下市场怎么看，再形成自己的看法
  * 典型股票只需 25-35 年 FCF 折现才能解释今天的价格（M1 p.16）

求解目标（择一或多个）：
  --implied-growth    给定 WACC，反推永续增长率 g
  --implied-wacc      给定 g，反推市场隐含 WACC（market-implied WACC）
  --implied-margin    给定收入路径与目标倍数，反推市场隐含的稳态经营利润率
  --implied-terminal  给定 WACC 与 g，反推市场隐含的终值倍数

用法：
  python reverse_dcf.py --csv fcff.csv --price 100 --shares 100 --net-debt 0 --solve growth
  python reverse_dcf.py --csv fcff.csv --price 100 --shares 100 --solve wacc --terminal-growth 0.025
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import sys
from typing import Callable, List, Sequence


def _f(x, nd=2, dash="n.a."):
    if x is None:
        return dash
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return dash
    return f"{x:,.{nd}f}"


def discount(fcff: Sequence[float], rate: float) -> List[float]:
    return [f / ((1.0 + rate) ** (i + 1)) for i, f in enumerate(fcff)]


def equity_from_fcff(fcff: Sequence[float], rate: float,
                      g: float | None, exit_multiple: float | None,
                      net_debt: float, shares: float) -> float:
    """给定折现率与终值假设，算出每股价值。"""
    n = len(fcff)
    pv_explicit = sum(discount(fcff, rate))
    if g is not None:
        if rate <= g:
            raise ValueError("WACC 必须大于 g")
        tv = fcff[-1] * (1 + g) / (rate - g)
    elif exit_multiple is not None:
        tv = exit_multiple * fcff[-1]
    else:
        raise ValueError("需要 g 或 exit_multiple")
    pv_tv = tv / ((1.0 + rate) ** n)
    ev = pv_explicit + pv_tv
    equity = ev - net_debt
    return equity / shares


def solve_bisect(fn: Callable[[float], float], lo: float, hi: float,
                  tol: float = 1e-7, max_iter: int = 300) -> float:
    """在 [lo, hi] 上二分求根：fn(x) = 0。"""
    flo, fhi = fn(lo), fn(hi)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        raise ValueError(f"区间 [{lo}, {hi}] 无根（f(lo)={flo:.6g}, f(hi)={fhi:.6g}）")
    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        fmid = fn(mid)
        if abs(fmid) < tol or (hi - lo) < tol:
            return mid
        if flo * fmid < 0:
            hi, fhi = mid, fmid
        else:
            lo, flo = mid, fmid
    return (lo + hi) / 2.0


def implied_growth(fcff: Sequence[float], price: float, shares: float,
                   net_debt: float, wacc: float) -> float:
    """给定 WACC，反推市场隐含的永续增长率 g。"""
    def f(g: float) -> float:
        try:
            return equity_from_fcff(fcff, wacc, g, None, net_debt, shares) - price
        except ValueError:
            return float("inf")
    # g 的可行上界：略低于 WACC
    return solve_bisect(f, -0.50, wacc - 1e-4)


def implied_wacc(fcff: Sequence[float], price: float, shares: float,
                 net_debt: float, g: float) -> float:
    """给定 g，反推市场隐含 WACC（market-implied WACC）。"""
    def f(r: float) -> float:
        try:
            return equity_from_fcff(fcff, r, g, None, net_debt, shares) - price
        except ValueError:
            return float("inf")
    # 下界必须 > g
    lo = max(g + 1e-4, 0.0001)
    return solve_bisect(f, lo, 5.0)


def implied_terminal_multiple(fcff: Sequence[float], price: float, shares: float,
                              net_debt: float, wacc: float, g: float) -> float:
    """给定 WACC 与 g，反推市场隐含终值倍数。"""
    n = len(fcff)
    pv_explicit = sum(discount(fcff, wacc))
    target_ev = price * shares + net_debt
    pv_tv_needed = target_ev - pv_explicit
    tv_needed = pv_tv_needed * ((1 + wacc) ** n)
    if tv_needed <= 0:
        return float("nan")
    return tv_needed / fcff[-1]


def implied_margin(revenue: Sequence[float], price: float, shares: float,
                   net_debt: float, wacc: float, g: float,
                   tax_rate: float, target_pe: float) -> dict:
    """
    给定收入路径与目标 P/E，反推市场隐含的稳态经营利润率。

    推导：Price = Target_PE x EPS
          EPS = NOPAT / Shares = (Revenue x OperatingMargin x (1 - t)) / Shares
          => OperatingMargin = Price x Shares x t_adj / (Revenue_ntm x Target_PE)
    其中 t_adj = 1 - tax_rate。
    """
    ntm_revenue = revenue[-1]
    implied_nopat = price * shares
    implied_operating_profit = implied_nopat / (1.0 - tax_rate)
    implied_margin = implied_operating_profit / ntm_revenue
    implied_eps = price / target_pe
    return {
        "ntm_revenue": ntm_revenue,
        "target_pe": target_pe,
        "implied_eps": implied_eps,
        "implied_nopat": implied_nopat,
        "implied_operating_profit": implied_operating_profit,
        "implied_operating_margin": implied_margin,
    }


def expectations_gap(market_value: float, internal_value: float) -> dict:
    """
    Expectations Gap = 市场观点 − 内部观点（M1 p.91）
    price_value_gap = 现价 − 内在价值（Alpha Load）
    """
    gap = market_value - internal_value
    pct = gap / internal_value if internal_value else None
    upside = (internal_value - market_value) / market_value if market_value else None
    return {
        "market_value": market_value,
        "internal_value": internal_value,
        "expectations_gap": gap,
        "expectations_gap_pct": pct,
        "price_value_gap": market_value - internal_value,
        "upside_to_internal": upside,
    }


def render(result: dict) -> str:
    o = io.StringIO()
    o.write("## Reverse DCF —— 市场隐含假设\n\n")
    o.write("| 项目 | 值 |\n|---|---|\n")
    PCT_KEYS = {"wacc", "terminal_growth", "implied_growth", "implied_wacc",
                "implied_margin"}
    for k, label in [
        ("solve", "求解目标"),
        ("price", "现价"),
        ("shares", "稀释股数"),
        ("net_debt", "净债务"),
        ("wacc", "使用 WACC"),
        ("terminal_growth", "使用永续增长率 g"),
        ("implied_growth", "**市场隐含永续增长率 g**"),
        ("implied_wacc", "**市场隐含 WACC**"),
        ("implied_terminal_multiple", "**市场隐含终值倍数**"),
        ("implied_margin", "**市场隐含稳态经营利润率**"),
        ("implied_eps", "隐含 EPS（按目标 P/E）"),
        ("target_pe", "目标 P/E"),
    ]:
        if k in result and result[k] is not None:
            v = result[k]
            if k in PCT_KEYS and isinstance(v, float):
                suffix = "x" if k == "implied_terminal_multiple" else "%"
                o.write(f"| {label} | {_f(v*100)}{suffix} |\n")
            elif isinstance(v, float):
                o.write(f"| {label} | {_f(v)} |\n")
            else:
                o.write(f"| {label} | {v} |\n")
    o.write("\n")

    if result.get("gap"):
        g = result["gap"]
        o.write("### Expectations Gap（市场观点 − 内部观点）\n\n")
        o.write("| 项目 | 值 |\n|---|---|\n")
        o.write(f"| 市场隐含价值 | {_f(g['market_value'])} |\n")
        o.write(f"| 内部价值 | {_f(g['internal_value'])} |\n")
        o.write(f"| **Expectations Gap** | **{_f(g['expectations_gap'])}** |\n")
        if g["expectations_gap_pct"] is not None:
            o.write(f"| Gap 幅度 | {_f(g['expectations_gap_pct']*100)}% |\n")
        o.write(f"| 上行空间至内部价值 | {_f(g['upside_to_internal']*100)}% |\n\n")

    o.write("### 解读纪律\n\n")
    o.write("- 先写下市场观点（reverse DCF 结果），再形成内部观点；顺序反了会被锚定。\n")
    o.write("- 市场隐含 g 远高于可持续水平 ⇒ 市场在给不可持续的高增长定价 → 偏空。\n")
    o.write("- 市场隐含 WACC 远高于同业 ⇒ 市场在给高风险定价，可能是折价机会，也可能是市场对的。\n")
    o.write("- 隐含稳态利润率高于历史峰值 ⇒ 预期不可实现 → 偏空。\n")
    return o.getvalue()


def render_tsv(result: dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["item", "value"])
    for k, v in result.items():
        if k == "gap":
            for gk, gv in v.items():
                w.writerow([f"gap.{gk}", f"{gv:.6f}" if isinstance(gv, float) else str(gv)])
        elif v is None:
            continue
        elif isinstance(v, float):
            w.writerow([k, f"{v:.6f}"])
        else:
            w.writerow([k, str(v)])
    return buf.getvalue()


def read_series(path: str) -> List[float]:
    vals: List[float] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        for row in csv.reader(f):
            if not row:
                continue
            cell = row[-1].strip().replace(",", "").replace("%", "")
            if cell in ("", "n.a.", "na", "N/A", "-"):
                continue
            try:
                vals.append(float(cell))
            except ValueError:
                continue
    if not vals:
        raise SystemExit(f"未能从 {path} 解析出数值")
    return vals


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Fundamental Edge Reverse DCF")
    p.add_argument("--csv", required=True, help="FCFF 或收入序列 CSV")
    p.add_argument("--series-type", choices=["fcff", "revenue"], default="fcff")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--shares", type=float, required=True)
    p.add_argument("--net-debt", type=float, default=0.0)
    p.add_argument("--solve", choices=["growth", "wacc", "terminal", "margin", "all"],
                   default="all")
    p.add_argument("--wacc", type=float, default=0.08)
    p.add_argument("--terminal-growth", type=float, default=0.025)
    p.add_argument("--tax-rate", type=float, default=0.25)
    p.add_argument("--target-pe", type=float, help="--solve margin 时必填")
    p.add_argument("--internal-value", type=float, help="内部价值（每股），用于计算 Expectations Gap")
    p.add_argument("--format", choices=["md", "tsv", "both"], default="both")
    a = p.parse_args(argv)

    series = read_series(a.csv)
    result = {"solve": a.solve, "price": a.price, "shares": a.shares,
              "net_debt": a.net_debt}

    if a.series_type == "fcff":
        if a.solve in ("growth", "wacc", "terminal", "all"):
            result["wacc"] = a.wacc
            result["terminal_growth"] = a.terminal_growth
            result["implied_growth"] = implied_growth(
                series, a.price, a.shares, a.net_debt, a.wacc)
            result["implied_wacc"] = implied_wacc(
                series, a.price, a.shares, a.net_debt, a.terminal_growth)
            result["implied_terminal_multiple"] = implied_terminal_multiple(
                series, a.price, a.shares, a.net_debt, a.wacc, a.terminal_growth)
    else:
        if a.target_pe is None:
            p.error("--solve margin 需要 --target-pe")
        m = implied_margin(series, a.price, a.shares, a.net_debt,
                           a.wacc, a.terminal_growth, a.tax_rate, a.target_pe)
        result.update(m)

    if a.internal_value:
        result["gap"] = expectations_gap(a.price, a.internal_value)

    if a.format in ("md", "both"):
        print(render(result))
    if a.format in ("tsv", "both"):
        print(render_tsv(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
