#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
从 Fundamental Edge 课件库抽取 PDF 文本，用于回查原文。

课件根目录：优先取 --root 参数，其次取环境变量 FUNDAMENTAL_EDGE_ROOT。
用途：当 references/ 里的摘要不足以支撑某个细节时，直接回原文取页码与原话。

注意：课件页眉页脚含 "STRICTLY CONFIDENTIAL. NOT FOR DISTRIBUTION" 水印，
抽取结果仅供内部研究使用，勿外传。

用法：
  # 列出全部 PDF（含所在模块）
  python extract_course_pdf.py --list

  # 抽取某个模块的全部 PDF
  python extract_course_pdf.py --module "Module 11" --out-dir ./course_text

  # 抽取单个文件（模糊匹配文件名）
  python extract_course_pdf.py --file "Measuring the Moat" --out-dir ./course_text

  # 全文检索（跨全部 PDF）
  python extract_course_pdf.py --grep "ROIC" --max-hits 40
"""
from __future__ import annotations

import argparse
import hashlib
import os
import re
import sys

COURSE_ROOT = os.environ.get("FUNDAMENTAL_EDGE_ROOT", "")
SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def iter_pdfs(root: str):
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if f.lower().endswith(".pdf"):
                yield os.path.join(dp, f)


def extract_text(path: str) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        from PyPDF2 import PdfReader  # type: ignore
    reader = PdfReader(path)
    parts = []
    for i, pg in enumerate(reader.pages):
        try:
            parts.append(f"\n===== PAGE {i+1} =====\n" + (pg.extract_text() or ""))
        except Exception:
            parts.append(f"\n===== PAGE {i+1} =====\n")
    return "".join(parts)


def cmd_list(root: str) -> int:
    n = 0
    for p in sorted(iter_pdfs(root)):
        rel = os.path.relpath(p, root)
        print(f"{os.path.getsize(p)/1024:>9.0f} KB  {rel}")
        n += 1
    print(f"\n共 {n} 个 PDF")
    return 0


def cmd_grep(root: str, pattern: str, max_hits: int) -> int:
    rx = re.compile(pattern, re.IGNORECASE)
    hits = 0
    seen = set()
    for p in sorted(iter_pdfs(root)):
        key = hashlib.md5(open(p, "rb").read()).hexdigest()
        if key in seen:
            continue          # 跳过 (1) 重复文件
        seen.add(key)
        try:
            text = extract_text(p)
        except Exception as e:
            print(f"ERR {os.path.basename(p)}: {e}")
            continue
        rel = os.path.relpath(p, root)
        for m in rx.finditer(text):
            start = max(0, m.start() - 220)
            end = min(len(text), m.end() + 220)
            snippet = " ".join(text[start:end].split())
            print(f"\n--- {rel}\n    ...{snippet}...")
            hits += 1
            if hits >= max_hits:
                print(f"\n[已达上限 {max_hits} 条]")
                return 0
    print(f"\n共 {hits} 处命中")
    return 0


def cmd_extract(root: str, files: list[str], out_dir: str) -> int:
    os.makedirs(out_dir, exist_ok=True)
    for f in files:
        try:
            text = extract_text(f)
        except Exception as e:
            print(f"ERR {f}: {e}")
            continue
        base = os.path.splitext(os.path.basename(f))[0]
        dest = os.path.join(out_dir, base + ".txt")
        with open(dest, "w", encoding="utf-8") as fh:
            fh.write(text)
        print(f"OK {len(text):>8}c  {dest}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Fundamental Edge 课件 PDF 抽取工具")
    p.add_argument("--root", default=COURSE_ROOT,
                   help="课件根目录（也可用环境变量 FUNDAMENTAL_EDGE_ROOT 指定）")
    p.add_argument("--list", action="store_true", help="列出全部 PDF")
    p.add_argument("--module", help="按模块目录名抽取，如 'Module 11'")
    p.add_argument("--file", help="按文件名模糊匹配抽取")
    p.add_argument("--grep", help="全文正则检索")
    p.add_argument("--max-hits", type=int, default=40)
    p.add_argument("--out-dir", default=os.path.join(SKILL_ROOT, "course_text"))
    a = p.parse_args(argv)

    if not a.root:
        print("未指定课件目录。请用 --root <path> 或设置环境变量 FUNDAMENTAL_EDGE_ROOT。")
        return 1
    if not os.path.isdir(a.root):
        print(f"课件目录不存在：{a.root}\n请用 --root 指定正确路径。")
        return 1

    if a.list:
        return cmd_list(a.root)

    if a.grep:
        return cmd_grep(a.root, a.grep, a.max_hits)

    targets: list[str] = []
    if a.module:
        targets = [p for p in iter_pdfs(a.root)
                   if a.module.lower() in os.path.relpath(p, a.root).lower()]
    elif a.file:
        key = a.file.lower()
        targets = [p for p in iter_pdfs(a.root)
                   if key in os.path.basename(p).lower()]
    if not targets:
        print("未匹配到文件。用 --list 查看全部，或 --grep 全库检索。")
        return 1
    print(f"匹配 {len(targets)} 个文件 → {a.out_dir}")
    return cmd_extract(a.root, targets, a.out_dir)


if __name__ == "__main__":
    sys.exit(main())
