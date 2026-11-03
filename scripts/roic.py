#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ROIC 与价值创造引擎 —— Fundamental Edge 方法论实现
（来源：Module 7 Analyze a Business / Mauboussin "Calculate ROIC, 2022" / "ROIC Valuation"）

核心公式：
  NOPAT                = EBIT x (1 - 税率)
  投入资本 (IC)        = 净营运资本 + 净固定资产
  净营运资本 (NWC)     = 经营性流动资产 - 经营性流动负债
  ROIC                 = NOPAT / IC
  增量 ROIC            = ΔNOPAT / ΔIC
  有形 ROIC            = NOPAT / (IC - 商誉 - 其他无形资产)
  价值创造条件         : ROIC > WACC
  增长与再投资         : 增长 = 增量ROIC x 再投资率  →  再投资率 = 增长 / 增量ROIC
  价值创造金额         : Δ价值 = ΔNOPAT - WACC x ΔIC

用法：
  python roic.py --ebit 500 --tax-rate 0.25 --nwc 100 --net-fixed-assets 800 --wacc 0.08
  python roic.py --history hist.csv --wacc 0.08
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import sys
from typing import Dict, List, Sequence


def _f(x, nd=2, dash="n.a."):
    if x is None:
        return dash
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return dash
    return f"{x:,.{nd}f}"


def compute_roic(ebit: float, tax_rate: float, nwc: float,
                 net_fixed_assets: float, goodwill: float = 0.0,
                 other_intangibles: float = 0.0) -> Dict[str, float]:
    nopat = ebit * (1.0 - tax_rate)
    invested_capital = nwc + net_fixed_assets
    tangible_ic = invested_capital - goodwill - other_intangibles
    return {
        "ebit": ebit,
        "tax_rate": tax_rate,
        "nopat": nopat,
        "nwc": nwc,
        "net_fixed_assets": net_fixed_assets,
        "invested_capital": invested_capital,
        "goodwill": goodwill,
        "other_intangibles": other_intangibles,
        "tangible_invested_capital": tangible_ic,
        "roic": nopat / invested_capital if invested_capital else float("nan"),
        "tangible_roic": nopat / tangible_ic if tangible_ic else float("nan"),
        "nopat_margin": nopat / ebit if ebit else float("nan"),
    }


def value_creation(roic: float, wacc: float, delta_nopat: float,
                   delta_ic: float) -> Dict[str, float]:
    """
    价值创造分解（M7 / Mauboussin）：
      价值创造 = ΔNOPAT - WACC x ΔIC
      经济利润 (EVA-like) = (ROIC - WACC) x IC
      若 ROIC > WACC → 价值创造为正
    """
    spread = roic - wacc
    econ_profit = spread * (delta_nopat / roic) if roic else float("nan")
    value_created = delta_nopat - wacc * delta_ic
    return {
        "roic": roic,
        "wacc": wacc,
        "roic_wacc_spread": spread,
        "spread_bps": spread * 10000,
        "delta_nopat": delta_nopat,
        "delta_ic": delta_ic,
        "value_created": value_created,
        "incremental_roic": delta_nopat / delta_ic if delta_ic else float("nan"),
        "economic_profit": econ_profit,
        "verdict": "价值创造" if spread > 0 else "价值毁灭",
    }


def growth_and_reinvestment(growth: float, incremental_roic: float) -> Dict[str, float]:
    """
    增长 = 增量ROIC x 再投资率  →  再投资率 = 增长 / 增量ROIC
    （M4 p.81：价值对再投资率高度敏感）
    """
    if not incremental_roic:
        return {"growth": growth, "incremental_roic": incremental_roic,
                "reinvestment_rate": float("nan"),
                "growth_at_10x": float("nan")}
    reinvestment_rate = growth / incremental_roic
    return {
        "growth": growth,
        "incremental_roic": incremental_roic,
        "reinvestment_rate": reinvestment_rate,
        "reinvestment_rate_pct": reinvestment_rate,
        "growth_at_10x": 0.10 * incremental_roic,
        "growth_at_5x": 0.05 * incremental_roic,
        "growth_at_3x": 0.03 * incremental_roic,
    }


def reinvestment_sensitivity(starting_value: float, fcf: float,
                             horizon: int, rate: float,
                             exit_multiple: float = 15.0) -> Dict[str, float]:
    """
    再投资率敏感性（M4 p.81 锚）：

      课件锚（3 年、15x 终值倍数、起始 $10）：
        再投资率 20% → 期末 $17.28
        再投资率 10% → 期末 $13.31
        再投资率  5% → 期末 $11.58

    推导：每年留存 r 的 FCF，按退出倍数 m 变现，产生的价值增量
          ΔV = r x FCF x m
      当 FCF = V0 / m（即公司以 m 倍市盈率交易、且 FCF 为 V0/m）时：
          ΔV = r x V0   →   V_end = V0 x (1 + r) ^ h
      终值倍数 m 在数学上对消 —— 这正是该表"退出倍数不敏感、只取决于再投资率"
      的经济学含义：以公平价格再投资不创造也不毁灭价值，只按留存比例放大规模。
    """
    value_from_reinvestment = 0.0
    if exit_multiple and fcf:
        # 显式路径（保留以供审计）：按退出倍数逐年变现
        v = starting_value
        for t in range(1, horizon + 1):
            v += (fcf * rate) * exit_multiple
        value_from_reinvestment = v
    end_value = starting_value * ((1.0 + rate) ** horizon)
    return {"starting_value": starting_value, "fcf": fcf, "horizon": horizon,
            "reinvestment_rate": rate, "exit_multiple": exit_multiple,
            "ending_value": end_value,
            "ending_value_explicit_path": value_from_reinvestment or None}


def render(r: Dict, wacc: float) -> str:
    o = io.StringIO()
    o.write("## ROIC 与价值创造\n\n")
    o.write("### ROIC 计算\n\n")
    o.write("| 项目 | 值 |\n|---|---|\n")
    for k, label in [
        ("ebit", "EBIT"), ("tax_rate", "税率"), ("nopat", "NOPAT = EBIT x (1-t)"),
        ("nwc", "净营运资本 NWC"), ("net_fixed_assets", "净固定资产"),
        ("invested_capital", "投入资本 IC"),
        ("goodwill", "减：商誉"), ("other_intangibles", "减：其他无形资产"),
        ("tangible_invested_capital", "有形投入资本"),
        ("roic", "**ROIC**"), ("tangible_roic", "有形 ROIC"),
        ("nopat_margin", "NOPAT 利润率"),
    ]:
        if k in r and r[k] is not None:
            v = r[k]
            if k == "tax_rate":
                o.write(f"| {label} | {_f(v*100)}% |\n")
            elif k in ("roic", "tangible_roic", "nopat_margin"):
                o.write(f"| {label} | {_f(v*100)}% |\n")
            else:
                o.write(f"| {label} | {_f(v)} |\n")
    o.write("\n")

    if "vc" in r:
        vc = r["vc"]
        o.write("### 价值创造检验\n\n")
        o.write("| 项目 | 值 |\n|---|---|\n")
        o.write(f"| WACC | {_f(wacc*100)}% |\n")
        o.write(f"| ROIC | {_f(vc['roic']*100)}% |\n")
        o.write(f"| **ROIC - WACC 利差** | **{_f(vc['roic_wacc_spread']*100)}% "
                f"({_f(vc['spread_bps'],0)} bps)** |\n")
        o.write(f"| ΔNOPAT | {_f(vc['delta_nopat'])} |\n")
        o.write(f"| Δ投入资本 | {_f(vc['delta_ic'])} |\n")
        o.write(f"| **价值创造 = ΔNOPAT - WACC x ΔIC** | **{_f(vc['value_created'])}** |\n")
        o.write(f"| 增量 ROIC | {_f(vc['incremental_roic']*100)}% |\n")
        o.write(f"| 裁定 | **{vc['verdict']}** |\n\n")
        if vc["roic_wacc_spread"] <= 0:
            o.write("> 警示：ROIC ≤ WACC —— 增长在毁灭价值，估值不应给增长溢价。\n\n")

    if "gr" in r:
        gr = r["gr"]
        o.write("### 增长与再投资\n\n")
        o.write("| 项目 | 值 |\n|---|---|\n")
        o.write(f"| 增长率 | {_f(gr['growth']*100)}% |\n")
        o.write(f"| 增量 ROIC | {_f(gr['incremental_roic']*100)}% |\n")
        o.write(f"| **隐含再投资率 = 增长 / 增量ROIC** | **{_f(gr['reinvestment_rate']*100)}%** |\n")
        o.write(f"| 若增量 ROIC = 10%，可支撑增长 | {_f(gr['growth_at_10x']*100)}% |\n")
        o.write(f"| 若增量 ROIC = 5%，可支撑增长 | {_f(gr['growth_at_5x']*100)}% |\n")
        o.write(f"| 若增量 ROIC = 3%，可支撑增长 | {_f(gr['growth_at_3x']*100)}% |\n\n")
        o.write("> M4 p.81：价值对再投资率高度敏感；管理层创造/毁灭价值的能力是股票回报的关键变量。\n\n")

    if "rs" in r:
        o.write("### 再投资率敏感性\n\n")
        o.write("| 起始价值 | 再投资率 | 期末价值 | 回报倍数 |\n|---|---|---|---|\n")
        for row in r["rs"]:
            o.write(f"| {_f(row['starting_value'])} | {_f(row['reinvestment_rate']*100)}% | "
                    f"{_f(row['ending_value'])} | {_f(row['ending_value']/row['starting_value'])}x |\n")
        o.write("\n")
    return o.getvalue()


def render_tsv(r: Dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["item", "value"])
    for k, v in r.items():
        if k in ("vc", "gr"):
            for kk, vv in v.items():
                w.writerow([f"{k}.{kk}", f"{vv:.6f}" if isinstance(vv, float) else str(vv)])
        elif k == "rs":
            for i, row in enumerate(v):
                for kk, vv in row.items():
                    w.writerow([f"rs[{i}].{kk}", f"{vv:.6f}" if isinstance(vv, float) else str(vv)])
        elif isinstance(v, float):
            w.writerow([k, f"{v:.6f}"])
        elif v is not None:
            w.writerow([k, str(v)])
    return buf.getvalue()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Fundamental Edge ROIC 与价值创造引擎")
    p.add_argument("--ebit", type=float, help="当期 EBIT")
    p.add_argument("--tax-rate", type=float, default=0.25)
    p.add_argument("--nwc", type=float, default=0.0, help="净营运资本")
    p.add_argument("--net-fixed-assets", type=float, default=0.0)
    p.add_argument("--goodwill", type=float, default=0.0)
    p.add_argument("--other-intangibles", type=float, default=0.0)
    p.add_argument("--wacc", type=float, default=0.08)
    p.add_argument("--delta-nopat", type=float, help="ΔNOPAT")
    p.add_argument("--delta-ic", type=float, help="Δ投入资本")
    p.add_argument("--growth", type=float, help="增长率（小数）")
    p.add_argument("--incremental-roic", type=float)
    p.add_argument("--reinvestment-sensitivity", action="store_true")
    p.add_argument("--fcf", type=float, default=10.0, help="再投资敏感性用的年 FCF")
    p.add_argument("--horizon", type=int, default=3)
    p.add_argument("--exit-multiple", type=float, default=15.0)
    p.add_argument("--format", choices=["md", "tsv", "both"], default="both")
    a = p.parse_args(argv)

    result: Dict = {}
    if a.ebit is not None:
        result.update(compute_roic(a.ebit, a.tax_rate, a.nwc,
                                    a.net_fixed_assets, a.goodwill,
                                    a.other_intangibles))
        if a.delta_nopat is not None and a.delta_ic is not None:
            roic = result["roic"]
            result["vc"] = value_creation(roic, a.wacc, a.delta_nopat, a.delta_ic)
            if a.growth is not None:
                result["gr"] = growth_and_reinvestment(a.growth,
                                                      result["vc"]["incremental_roic"])
    if a.reinvestment_sensitivity:
        result["rs"] = [
            reinvestment_sensitivity(10.0, a.fcf, a.horizon, r, a.exit_multiple)
            for r in (0.20, 0.10, 0.05)
        ]

    if a.format in ("md", "both"):
        print(render(result, a.wacc))
    if a.format in ("tsv", "both"):
        print(render_tsv(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
