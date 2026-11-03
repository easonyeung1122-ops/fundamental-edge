#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DCF 估值引擎 —— Fundamental Edge 方法论实现

核心原则（来源：Fundamental Edge Module 1 / Module 4 / Module 11）：
  * "Everything is a DCF" —— 倍数只是 DCF 的速记
  * 价格是一个 FCF 预测（Price is a FCF forecast）
  * DCF 是"简单但不容易"：复杂度来自股权的久期（25-35 年）
  * 终值占比应尽量 < 25% NPV（Module 3 p.66）
  * 16x P/E <-> 8% WACC（Module 1 p.10 校准锚）

用法：
  python dcf.py --help
  python dcf.py --csv fcff.csv --wacc 0.08 --terminal-growth 0.025
  python dcf.py --csv fcff.csv --wacc 0.08 --exit-multiple 10 --sensitivity
"""
from __future__ import annotations

import argparse
import csv
import io
import math
import sys
from typing import List, Sequence

# ---------------------------------------------------------------- 常量锚点
# Fundamental Edge 课件给出的校准锚（用于 sanity check）
ANCHOR_WACC_PE = {0.04: 55.0, 0.07: 27.0, 0.10: 16.0, 0.11: 11.0, 0.12: 8.0}
TV_MAX_SHARE_OF_NPV = 0.25   # M3 p.66：终值应尽量 < 25% NPV
BASE_TERMINAL_MULTIPLE = 10.0  # M4 p.78 示例终值倍数


# ---------------------------------------------------------------- 工具
def _fmt(x, nd=2, dash="n.a."):
    if x is None:
        return dash
    if isinstance(x, str):
        return x
    if isinstance(x, float) and (math.isnan(x) or math.isinf(x)):
        return dash
    return f"{x:,.{nd}f}"


def discount(fcff: Sequence[float], wacc: float) -> List[float]:
    """按 WACC 逐年折现（期末折现，t=1..n）。"""
    return [f / ((1.0 + wacc) ** (i + 1)) for i, f in enumerate(fcff)]


def build_wacc(rf: float, beta: float, erp: float,
               kd_pretax: float, tax_rate: float,
               equity_weight: float, debt_weight: float) -> dict:
    """
    资本成本搭建（Module 1 p.10 / Module 11）：
      Cost of Equity  = Rf + Beta x ERP
      WACC            = Ke x E/V + Kd_after_tax x D/V
    """
    if abs(equity_weight + debt_weight - 1.0) > 1e-6:
        raise ValueError("E/V + D/V 必须等于 1.0")
    ke = rf + beta * erp
    kd_after_tax = kd_pretax * (1.0 - tax_rate)
    wacc = ke * equity_weight + kd_after_tax * debt_weight
    return {
        "risk_free": rf, "beta": beta, "erp": erp,
        "cost_of_equity": ke, "kd_pretax": kd_pretax, "tax_rate": tax_rate,
        "kd_after_tax": kd_after_tax,
        "equity_weight": equity_weight, "debt_weight": debt_weight,
        "wacc": wacc,
    }


def dcf(fcff: Sequence[float],
        wacc: float,
        terminal_growth: float | None = None,
        exit_multiple: float | None = None,
        net_debt: float = 0.0,
        shares: float = 1.0,
        cash: float = 0.0,
        minority: float = 0.0) -> dict:
    """
    两阶段 DCF。
      显性期：fcff 为未杠杆自由现金流序列（长度 = 预测年数）
      终值：perpetuity growth 与 exit multiple 二选一（或同时给出做对比）
    返回 EV / Equity Value / 每股价值 / 终值占比 / 隐含 P/E 等。
    """
    if not fcff:
        raise ValueError("fcff 序列不能为空")
    n = len(fcff)
    df = discount(fcff, wacc)
    pv_explicit = sum(df)

    # 终值（Gordon 增长）
    tv_gordon = None
    pv_tv_gordon = None
    if terminal_growth is not None:
        if wacc <= terminal_growth:
            raise ValueError("WACC 必须大于永续增长率 g")
        tv_gordon = fcff[-1] * (1 + terminal_growth) / (wacc - terminal_growth)
        pv_tv_gordon = tv_gordon / ((1 + wacc) ** n)

    # 终值（退出倍数）
    tv_multiple = None
    pv_tv_multiple = None
    if exit_multiple is not None:
        tv_multiple = exit_multiple * fcff[-1]
        pv_tv_multiple = tv_multiple / ((1 + wacc) ** n)

    # 选择用于估值的终值：显式指定优先；都没指定则用 Gordon
    if pv_tv_gordon is not None:
        use_pv_tv, use_tv = pv_tv_gordon, tv_gordon
        tv_method = "perpetuity growth"
    elif pv_tv_multiple is not None:
        use_pv_tv, use_tv = pv_tv_multiple, tv_multiple
        tv_method = "exit multiple"
    else:
        raise ValueError("必须提供 terminal_growth 或 exit_multiple")

    ev = pv_explicit + use_pv_tv
    equity_value = ev - net_debt + cash - minority
    per_share = equity_value / shares if shares else None
    tv_share = use_pv_tv / ev if ev else None

    # 隐含终值倍数（用 Gordon 反推）
    implied_exit = (tv_gordon / fcff[-1]) if (tv_gordon and fcff[-1]) else None

    return {
        "n_years": n,
        "wacc": wacc,
        "pv_explicit": pv_explicit,
        "tv_gordon": tv_gordon, "pv_tv_gordon": pv_tv_gordon,
        "tv_multiple": tv_multiple, "pv_tv_multiple": pv_tv_multiple,
        "tv_used": use_tv, "pv_tv_used": use_pv_tv, "tv_method": tv_method,
        "tv_share_of_npv": tv_share,
        "ev": ev,
        "net_debt": net_debt, "cash": cash, "minority": minority,
        "equity_value": equity_value,
        "shares": shares,
        "per_share": per_share,
        "implied_exit_multiple": implied_exit,
        "discounted_fcff": df,
    }


def implied_pe(per_share: float, eps: float) -> float | None:
    """从每股价值与 EPS 反推隐含 P/E。"""
    if not eps:
        return None
    return per_share / eps


def sensitivity(fcff: Sequence[float], waccs: Sequence[float],
                growths: Sequence[float], net_debt: float,
                shares: float, cash: float = 0.0, minority: float = 0.0) -> dict:
    """WACC x 永续增长率 的每股价值敏感性矩阵。"""
    grid = []
    for g in growths:
        row = {"terminal_growth": g, "values": []}
        for w in waccs:
            try:
                r = dcf(fcff, w, terminal_growth=g, net_debt=net_debt,
                        shares=shares, cash=cash, minority=minority)
                row["values"].append(r["per_share"])
            except ValueError:
                row["values"].append(None)
        grid.append(row)
    return {"waccs": list(waccs), "grid": grid}


# ---------------------------------------------------------------- 输出
def render_markdown(result: dict, wacc_detail: dict | None,
                    eps: float | None, price: float | None,
                    sens: dict | None) -> str:
    out = io.StringIO()
    out.write("## DCF 估值结果\n\n")

    if wacc_detail:
        out.write("### 资本成本构建\n\n")
        out.write("| 参数 | 值 |\n|---|---|\n")
        out.write(f"| 无风险利率 Rf | {_fmt(wacc_detail['risk_free']*100)}% |\n")
        out.write(f"| Beta | {_fmt(wacc_detail['beta'])}x |\n")
        out.write(f"| 股权风险溢价 ERP | {_fmt(wacc_detail['erp']*100)}% |\n")
        out.write(f"| **股权成本 Ke** | **{_fmt(wacc_detail['cost_of_equity']*100)}%** |\n")
        out.write(f"| 税前债务成本 Kd | {_fmt(wacc_detail['kd_pretax']*100)}% |\n")
        out.write(f"| 税率 | {_fmt(wacc_detail['tax_rate']*100)}% |\n")
        out.write(f"| 税后债务成本 | {_fmt(wacc_detail['kd_after_tax']*100)}% |\n")
        out.write(f"| E/V | {_fmt(wacc_detail['equity_weight']*100)}% |\n")
        out.write(f"| D/V | {_fmt(wacc_detail['debt_weight']*100)}% |\n")
        out.write(f"| **WACC** | **{_fmt(wacc_detail['wacc']*100)}%** |\n\n")

    out.write("### 估值桥\n\n")
    out.write("| 项目 | 值 |\n|---|---|\n")
    out.write(f"| 显性期年数 | {result['n_years']} |\n")
    out.write(f"| 显性期现值 (PV of FCF) | {_fmt(result['pv_explicit'])} |\n")
    out.write(f"| 终值 (TV) | {_fmt(result['tv_used'])} |\n")
    out.write(f"| 终值现值 | {_fmt(result['pv_tv_used'])} |\n")
    out.write(f"| 终值方法 | {result['tv_method']} |\n")
    out.write(f"| **企业价值 EV** | **{_fmt(result['ev'])}** |\n")
    out.write(f"| 减：净债务 | {_fmt(result['net_debt'])} |\n")
    out.write(f"| 加：现金 | {_fmt(result['cash'])} |\n")
    out.write(f"| 减：少数股东权益 | {_fmt(result['minority'])} |\n")
    out.write(f"| **股权价值** | **{_fmt(result['equity_value'])}** |\n")
    out.write(f"| 稀释股数 | {_fmt(result['shares'], 0)} |\n")
    out.write(f"| **每股价值** | **{_fmt(result['per_share'])}** |\n")

    tv_share = result["tv_share_of_npv"]
    if tv_share is not None:
        flag = "OK" if tv_share <= TV_MAX_SHARE_OF_NPV else "**超标**"
        out.write(f"| 终值占 NPV 比重 | {_fmt(tv_share*100)}% ({flag}, 目标 <{int(TV_MAX_SHARE_OF_NPV*100)}%) |\n")
    if result["implied_exit_multiple"]:
        out.write(f"| 隐含终值倍数 (Gordon 反推) | {_fmt(result['implied_exit_multiple'])}x |\n")
    if eps:
        pe = implied_pe(result["per_share"], eps)
        out.write(f"| 隐含 P/E | {_fmt(pe)}x |\n")
    if price:
        up = result["per_share"] / price - 1 if result["per_share"] and price else None
        out.write(f"| 现价 | {_fmt(price)} |\n")
        out.write(f"| 上行空间 | {_fmt(up*100)}% |\n")
    out.write("\n")

    if sens:
        out.write("### 敏感性：每股价值（WACC × 永续增长率）\n\n")
        head = "| g \\ WACC | " + " | ".join(f"{w*100:.1f}%" for w in sens["waccs"]) + " |\n"
        out.write(head)
        out.write("|---" * (len(sens["waccs"]) + 1) + "|\n")
        for row in sens["grid"]:
            cells = " | ".join(
                (_fmt(v) if v is not None else "n.a.") for v in row["values"])
            out.write(f"| **{row['terminal_growth']*100:.1f}%** | {cells} |\n")
        out.write("\n")

    # 锚点校验
    w = result["wacc"]
    nearest = min(ANCHOR_WACC_PE, key=lambda k: abs(k - w))
    out.write("### 锚点校验（Fundamental Edge Module 1 p.10）\n\n")
    out.write(f"- 课件隐含 P/E 参照（Cost of Equity {nearest*100:.0f}%）：{ANCHOR_WACC_PE[nearest]}x\n")
    if eps:
        pe = implied_pe(result["per_share"], eps)
        out.write(f"- 本模型隐含 P/E：{_fmt(pe)}x")
        if pe:
            out.write(f"　→ 与参照偏离 {_fmt((pe/ANCHOR_WACC_PE[nearest]-1)*100)}%\n")
    return out.getvalue()


def render_tsv(result: dict, wacc_detail: dict | None,
               eps: float | None, price: float | None) -> str:
    rows = [("item", "value")]
    if wacc_detail:
        for k, v in wacc_detail.items():
            rows.append((f"wacc.{k}", f"{v:.6f}" if isinstance(v, float) else str(v)))
    for k in ("n_years", "pv_explicit", "tv_gordon", "pv_tv_gordon",
              "tv_multiple", "pv_tv_multiple", "tv_used", "pv_tv_used",
              "tv_method", "tv_share_of_npv", "ev", "net_debt", "cash",
              "minority", "equity_value", "shares", "per_share",
              "implied_exit_multiple"):
        v = result.get(k)
        if isinstance(v, float):
            rows.append((k, f"{v:.6f}"))
        elif v is not None:
            rows.append((k, str(v)))
    if eps and result["per_share"]:
        rows.append(("implied_pe", f"{implied_pe(result['per_share'], eps):.4f}"))
    if price and result["per_share"]:
        rows.append(("upside_pct", f"{(result['per_share']/price-1)*100:.4f}"))
    buf = io.StringIO()
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerows(rows)
    return buf.getvalue()


# ---------------------------------------------------------------- CLI
def read_fcff(path: str) -> List[float]:
    vals: List[float] = []
    with open(path, "r", encoding="utf-8-sig", newline="") as f:
        sample = f.read(4096)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t;") \
            if any(d in sample for d in ",\t;") else csv.excel
        for row in csv.reader(f, dialect):
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
        raise SystemExit(f"未能从 {path} 解析出任何数值")
    return vals


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Fundamental Edge DCF 估值引擎",
        formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--csv", help="FCFF 序列 CSV（每行一个数值，或末列为数值）")
    p.add_argument("--fcff", help="直接以逗号分隔给出 FCFF 序列")
    p.add_argument("--wacc", type=float, help="折现率（WACC）")
    p.add_argument("--terminal-growth", type=float, help="永续增长率 g")
    p.add_argument("--exit-multiple", type=float, help="退出倍数（终值倍数）")
    p.add_argument("--net-debt", type=float, default=0.0)
    p.add_argument("--cash", type=float, default=0.0)
    p.add_argument("--minority", type=float, default=0.0)
    p.add_argument("--shares", type=float, default=1.0)
    p.add_argument("--eps", type=float, help="用于反推隐含 P/E 的 EPS")
    p.add_argument("--price", type=float, help="现价，用于计算上行空间")
    p.add_argument("--sensitivity", action="store_true", help="输出敏感性矩阵")
    p.add_argument("--build-wacc", action="store_true",
                   help="用 Rf/Beta/ERP/Kd/税率/权重 构建 WACC")
    p.add_argument("--rf", type=float, default=0.045)
    p.add_argument("--beta", type=float, default=1.0)
    p.add_argument("--erp", type=float, default=0.05)
    p.add_argument("--kd", type=float, default=0.06, help="税前债务成本")
    p.add_argument("--tax-rate", type=float, default=0.25)
    p.add_argument("--equity-weight", type=float, default=0.70)
    p.add_argument("--debt-weight", type=float, default=0.30)
    p.add_argument("--format", choices=["md", "tsv", "both"], default="both")
    a = p.parse_args(argv)

    fcff: List[float] = []
    if a.csv:
        fcff = read_fcff(a.csv)
    elif a.fcff:
        fcff = [float(x) for x in a.fcff.replace(" ", "").split(",") if x]
    else:
        p.error("必须提供 --csv 或 --fcff")

    wacc_detail = None
    if a.build_wacc:
        wacc_detail = build_wacc(a.rf, a.beta, a.erp, a.kd, a.tax_rate,
                                  a.equity_weight, a.debt_weight)
        wacc = wacc_detail["wacc"]
    elif a.wacc is not None:
        wacc = a.wacc
    else:
        p.error("必须提供 --wacc 或 --build-wacc")

    result = dcf(fcff, wacc, terminal_growth=a.terminal_growth,
                  exit_multiple=a.exit_multiple, net_debt=a.net_debt,
                  shares=a.shares, cash=a.cash, minority=a.minority)

    sens = None
    if a.sensitivity:
        waccs = [wacc - 0.02, wacc - 0.01, wacc, wacc + 0.01, wacc + 0.02]
        base_g = a.terminal_growth if a.terminal_growth is not None else 0.025
        growths = [base_g - 0.01, base_g - 0.005, base_g,
                   base_g + 0.005, base_g + 0.01]
        sens = sensitivity(fcff, waccs, growths, a.net_debt, a.shares,
                           a.cash, a.minority)

    if a.format in ("md", "both"):
        print(render_markdown(result, wacc_detail, a.eps, a.price, sens))
    if a.format in ("tsv", "both"):
        print(render_tsv(result, wacc_detail, a.eps, a.price))
    return 0


if __name__ == "__main__":
    sys.exit(main())
