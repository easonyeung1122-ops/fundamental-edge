#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
风险/回报与仓位引擎 —— Fundamental Edge 方法论实现
（来源：Module 2 Life on the Buy-Side / Module 3 Thesis Development / Module 5 Idea Generation / Module 15）

核心公式：
  Upside   = (目标价 - 现价) / 现价
  Downside = (现价 - 止损价) / 现价
  PSUC     = Upside / (Upside + |Downside|)
      锚点：抛硬币 50%；并购套利 83.3%；10:1 赔率生物科技 9.1%
  R/R      = Upside / |Downside|
      门槛：R/R ≥ 2.0x 可建仓；R/R ≥ 3.0x = slam-dunk
  12 个月目标价 = NTM2 EPS x NTM2 P/E
  组合净敞口 = Σ 持仓权重；基金预测表现 = 基准涨跌幅 x 净敞口

用法：
  python riskreward.py --price 100 --target 140 --stop 85
  python riskreward.py --reward-ladder --price 100 --ntm2-eps 8.5 --ntm2-pe 22 --eps-epsn 4.2
  python riskreward.py --scenario bull:150:0.3,base:110:0.5,bear:70:0.2 --price 100
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import sys
from typing import Dict, List

PSUC_ANCHORS = {
    "抛硬币": 0.50,
    "并购套利": 0.833,
    "10:1 赔率生物科技": 0.091,
}
RR_SOFT = 2.0
RR_SLAM = 3.0


def _f(x, nd=2, dash="n.a."):
    if x is None:
        return dash
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return dash
    return f"{x:,.{nd}f}"


def psuc(upside: float, downside: float) -> Dict[str, float]:
    """PSUC = Upside / (Upside + |Downside|)。downside 传正数表示损失幅度。"""
    denom = upside + abs(downside)
    value = upside / denom if denom else float("nan")
    label = None
    for k, v in PSUC_ANCHORS.items():
        if abs(value - v) < 0.015:
            label = k
            break
    return {"upside": upside, "downside": downside,
            "psuc": value, "psuc_pct": value, "anchor": label}


def risk_reward(upside: float, downside: float) -> Dict[str, float]:
    rr = upside / abs(downside) if downside else float("inf")
    verdict = "slam-dunk" if rr >= RR_SLAM else ("可建仓" if rr >= RR_SOFT else "不足")
    return {"upside": upside, "downside": downside, "rr": rr, "verdict": verdict}


def reward_ladder(price: float, eps_epsn: float, ntm2_eps: float,
                  ntm2_pe: float, steps: List[int] = None) -> List[Dict]:
    """
    12 个月目标价 = NTM2 EPS x NTM2 P/E
    回报阶梯：每个目标价对应的 P/E、隐含涨跌幅、PSUC（用止损价反推下行）。
    """
    steps = steps or [-2, -1, 0, 1, 2]
    target = ntm2_eps * ntm2_pe
    rows = []
    for s in steps:
        pe = ntm2_pe + s
        tgt = ntm2_eps * pe
        up = (tgt - price) / price
        rows.append({"step": s, "ntm2_pe": pe, "target": tgt,
                     "upside": up, "eps_ntm_epsn": eps_epsn,
                     "eps_growth": (ntm2_eps / eps_epsn - 1) if eps_epsn else None,
                     "reward": up})
    return rows, target


def scenario_analysis(price: float, scenarios: List[Dict]) -> Dict:
    """
    概率加权：期望值 = Σ p_i x price_i
    scenarios: [{'name','price','prob'}]
    """
    ev = sum(s["price"] * s["prob"] for s in scenarios)
    probs = sum(s["prob"] for s in scenarios)
    # 上行 = 最好的情景相对现价的涨幅；下行 = 最差情景的跌幅（均为正的幅度）
    upside_scen = max(0.0, max((s["price"] - price) / price for s in scenarios))
    downside_scen = max(0.0, max((price - s["price"]) / price for s in scenarios))
    return {
        "scenarios": scenarios,
        "probability_sum": probs,
        "expected_value": ev,
        "expected_return": (ev / price - 1) if price else None,
        "upside": upside_scen,
        "downside": downside_scen,
        "psuc": psuc(upside_scen, downside_scen)["psuc"],
        "rr": risk_reward(upside_scen, downside_scen)["rr"],
    }


def position_sizing(portfolio_value: float, risk_pct: float,
                    entry: float, stop: float) -> Dict:
    """
    按止损定仓：仓位金额 = 组合净值 x 单笔风险预算 / (入场价 - 止损价)
    约束：单笔最大亏损 ≤ 组合 x risk_pct；并受最大权重上限约束。
    """
    per_share_risk = entry - stop
    if per_share_risk <= 0:
        raise ValueError("止损价必须低于入场价")
    shares_by_risk = portfolio_value * risk_pct / per_share_risk
    value_by_risk = shares_by_risk * entry
    return {
        "portfolio_value": portfolio_value,
        "risk_pct": risk_pct,
        "risk_budget": portfolio_value * risk_pct,
        "entry": entry, "stop": stop,
        "per_share_risk": per_share_risk,
        "shares_by_risk": shares_by_risk,
        "position_value": value_by_risk,
        "weight": value_by_risk / portfolio_value if portfolio_value else None,
        "max_loss": shares_by_risk * per_share_risk,
    }


def net_exposure(positions: List[Dict]) -> Dict:
    """
    组合敞口：positions: [{'ticker','weight'}]（可负 = 空头）
    基金预测表现 = 基准涨跌幅 x 净敞口
    """
    gross = sum(abs(p["weight"]) for p in positions)
    net = sum(p["weight"] for p in positions)
    return {
        "gross_exposure": gross,
        "net_exposure": net,
        "long_exposure": sum(p["weight"] for p in positions if p["weight"] > 0),
        "short_exposure": sum(p["weight"] for p in positions if p["weight"] < 0),
        "n_positions": len(positions),
        "long_count": sum(1 for p in positions if p["weight"] > 0),
        "short_count": sum(1 for p in positions if p["weight"] < 0),
    }


def render_all(args, rr: Dict, ps: Dict, ladder, target: float,
               scen: Dict | None, sizing: Dict | None, expo: Dict | None) -> str:
    o = io.StringIO()
    o.write("## 风险/回报与仓位\n\n")

    o.write("### 1. 风险回报比\n\n")
    o.write("| 项目 | 值 |\n|---|---|\n")
    o.write(f"| 现价 | {_f(args.price)} |\n")
    if args.target:
        o.write(f"| 目标价 | {_f(args.target)} |\n")
    if args.stop:
        o.write(f"| 止损价 | {_f(args.stop)} |\n")
    # 多头结构校验：目标价必须高于现价，且必须给止损，否则第 1 节无意义。
    # 不校验会把「目标价低于现价 + 无止损」算成 PSUC 100% / slam-dunk（假信号）。
    invalid = []
    if args.target and args.target <= args.price:
        invalid.append(f"目标价 {_f(args.target)} ≤ 现价 {_f(args.price)}，不是多头结构")
    if args.stop and args.stop >= args.price:
        invalid.append(f"止损价 {_f(args.stop)} ≥ 现价 {_f(args.price)}")
    if not args.stop and args.target:
        invalid.append("未给 --stop，下行幅度无法定义")
    if invalid:
        o.write("| **状态** | **输入不构成有效多头 R/R，本节不作裁定** |\n\n")
        for msg in invalid:
            o.write(f"- 起因：{msg}\n")
        o.write("- 处置：改用第 3 节情景加权（R/R 与 PSUC 由 bull/base/bear 导出），"
                "或补 `--stop` 并令目标价 > 现价。\n\n")
    else:
        o.write(f"| 上行 Upside | {_f(rr['upside']*100)}% |\n")
        o.write(f"| 下行 Downside | {_f(rr['downside']*100)}% |\n")
        o.write(f"| **R/R** | **{_f(rr['rr'])}x** |\n")
        o.write(f"| **PSUC** | **{_f(ps['psuc']*100)}%**"
                + (f"（锚点参照：{ps['anchor']}）" if ps.get("anchor") else "") + " |\n")
        o.write(f"| 裁定 | **{rr['verdict']}** "
                f"(门槛 R/R ≥ {RR_SOFT}x 可建仓，≥ {RR_SLAM}x = slam-dunk) |\n\n")
    o.write("PSUC 锚点：抛硬币 50% / 并购套利 83.3% / 10:1 赔率生物科技 9.1%\n\n")

    if ladder:
        base_target = next((r["target"] for r in ladder if r["step"] == 0), target)
        o.write("### 2. 12 个月回报阶梯（目标价 = NTM2 EPS x NTM2 P/E）\n\n")
        o.write(f"- NTM2 EPS = {_f(args.ntm2_eps)}"
                f"　NTM2 P/E = {_f(args.ntm2_pe)}x"
                f"　→ 基准目标价 **{_f(base_target)}**\n")
        if ladder[0].get("eps_growth") is not None:
            o.write(f"- 隐含 EPS 增长（NTM2 vs NTM）：{_f(ladder[0]['eps_growth']*100)}%\n")
        o.write("\n| 步长 | NTM2 P/E | 目标价 | 上行幅度 | 备注 |\n|---|---|---|---|---|\n")
        for r in ladder:
            note = "基准" if r["step"] == 0 else f"{r['step']:+d} 档"
            o.write(f"| {r['step']:+d} | {_f(r['ntm2_pe'])}x | {_f(r['target'])} | "
                    f"{_f(r['upside']*100)}% | {note} |\n")
        o.write("\n")

    if scen:
        o.write("### 3. 情景概率加权\n\n")
        o.write("| 情景 | 价格 | 概率 | 相对现价 |\n|---|---|---|---|\n")
        for s in scen["scenarios"]:
            o.write(f"| {s['name']} | {_f(s['price'])} | {_f(s['prob']*100)}% | "
                    f"{_f((s['price']/args.price-1)*100)}% |\n")
        o.write(f"| **概率合计** | | {_f(scen['probability_sum']*100)}% | |\n\n")
        o.write(f"- 期望值 = {_f(scen['expected_value'])}　期望回报 = "
                f"{_f(scen['expected_return']*100)}%\n")
        o.write(f"- 上行 {_f(scen['upside']*100)}% / 下行 {_f(scen['downside']*100)}%　"
                f"PSUC {_f(scen['psuc']*100)}%　R/R {_f(scen['rr'])}x\n\n")

    if sizing:
        o.write("### 4. 仓位（按止损定仓）\n\n")
        o.write("| 项目 | 值 |\n|---|---|\n")
        for k, label in [
            ("portfolio_value", "组合净值"), ("risk_pct", "单笔风险预算 %"),
            ("risk_budget", "风险预算金额"), ("entry", "入场价"), ("stop", "止损价"),
            ("per_share_risk", "每股风险"), ("shares_by_risk", "**可买份数**"),
            ("position_value", "**仓位金额**"), ("weight", "组合权重 %"),
            ("max_loss", "最大亏损金额"),
        ]:
            v = sizing[k]
            if k == "risk_pct":
                o.write(f"| {label} | {_f(v*100)}% |\n")
            elif k == "weight":
                o.write(f"| {label} | {_f(v*100)}% |\n")
            else:
                o.write(f"| {label} | {_f(v, 0 if '份数' in label or '金额' in label else 2)} |\n")
        o.write("\n")

    if expo:
        o.write("### 5. 组合敞口\n\n")
        o.write("| 项目 | 值 |\n|---|---|\n")
        o.write(f"| 持仓数 | {expo['n_positions']}（多 {expo['long_count']} / 空 {expo['short_count']}） |\n")
        o.write(f"| 总敞口 Gross | {_f(expo['gross_exposure']*100)}% |\n")
        o.write(f"| **净敞口 Net** | **{_f(expo['net_exposure']*100)}%** |\n")
        o.write(f"| 多头敞口 | {_f(expo['long_exposure']*100)}% |\n")
        o.write(f"| 空头敞口 | {_f(expo['short_exposure']*100)}% |\n")
        o.write("\n> 基金预测表现 = 基准涨跌幅 x 净敞口（M2 风险敞口框架）。\n")
    return o.getvalue()


def render_tsv(payload: Dict) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(["item", "value"])
    for k, v in payload.items():
        if isinstance(v, dict):
            for kk, vv in v.items():
                w.writerow([f"{k}.{kk}", f"{vv:.6f}" if isinstance(vv, float) else str(vv)])
        elif isinstance(v, list):
            for i, row in enumerate(v):
                if isinstance(row, dict):
                    for kk, vv in row.items():
                        w.writerow([f"{k}[{i}].{kk}", f"{vv:.6f}" if isinstance(vv, float) else str(vv)])
                else:
                    w.writerow([f"{k}[{i}]", str(row)])
        elif isinstance(v, float):
            w.writerow([k, f"{v:.6f}"])
        elif v is not None:
            w.writerow([k, str(v)])
    return buf.getvalue()


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Fundamental Edge 风险/回报与仓位引擎")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--target", type=float)
    p.add_argument("--stop", type=float)
    p.add_argument("--ntm2-eps", type=float)
    p.add_argument("--ntm2-pe", type=float)
    p.add_argument("--ntm-eps", type=float, help="NTM EPS（用于算隐含增长）")
    p.add_argument("--scenario", help="bull:150:0.3,base:110:0.5,bear:70:0.2")
    p.add_argument("--portfolio-value", type=float)
    p.add_argument("--risk-pct", type=float, default=0.01, help="单笔风险预算（如 0.01 = 1%%）")
    p.add_argument("--entry", type=float)
    p.add_argument("--positions", help="AAPL:0.05,MSFT:0.04,SHORT:0.02（负数为空头）")
    p.add_argument("--format", choices=["md", "tsv", "both"], default="both")
    a = p.parse_args(argv)

    target = a.target
    if a.target is None and a.ntm2_eps and a.ntm2_pe:
        target = a.ntm2_eps * a.ntm2_pe

    upside = (target - a.price) / a.price if target else 0.0
    downside = (a.price - a.stop) / a.price if a.stop else 0.0
    rr = risk_reward(upside, downside)
    ps = psuc(upside, downside)

    ladder = None
    if a.ntm2_eps and a.ntm2_pe:
        ladder, _ = reward_ladder(a.price, a.ntm_eps, a.ntm2_eps, a.ntm2_pe)

    scen = None
    if a.scenario:
        rows = []
        for part in a.scenario.split(","):
            name, pr, prob = part.split(":")
            rows.append({"name": name, "price": float(pr), "prob": float(prob)})
        scen = scenario_analysis(a.price, rows)

    sizing = None
    if a.portfolio_value and a.entry and a.stop:
        sizing = position_sizing(a.portfolio_value, a.risk_pct, a.entry, a.stop)

    expo = None
    if a.positions:
        pos = []
        for part in a.positions.split(","):
            t, wgt = part.split(":")
            pos.append({"ticker": t, "weight": float(wgt)})
        expo = net_exposure(pos)

    payload = {"price": a.price, "target": target, "stop": a.stop,
               "rr": rr, "psuc": ps, "ladder": ladder or [],
               "scenario": scen or {}, "sizing": sizing or {}, "exposure": expo or {}}

    if a.format in ("md", "both"):
        print(render_all(a, rr, ps, ladder, target or 0, scen, sizing, expo))
    if a.format in ("tsv", "both"):
        print(render_tsv(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
