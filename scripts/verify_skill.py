#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
校验 fundamental-edge skill 目录结构完整性。

检查项：
  * SKILL.md 存在、frontmatter 含 name / description / agent_created
  * references/ 下所有 SKILL.md 索引到的文件都存在且非空
  * scripts/ 下所有脚本可编译（py_compile）
  * assets/ 下所有 Excel 可被 openpyxl 打开
  * 每个 references 文件带页码引用标记（[Mn p.x]）

用法：python verify_skill.py [skill_dir]
"""
from __future__ import annotations

import os
import re
import sys

SKILL_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))

ok = True


def check(cond: bool, label: str, detail: str = "") -> None:
    global ok
    print(f"  {'PASS' if cond else 'FAIL'}  {label}{('  -> ' + detail) if detail else ''}")
    if not cond:
        ok = False


print(f"校验目录：{SKILL_DIR}\n")

# ---- 1. SKILL.md ----
print("[1] SKILL.md")
skill_md = os.path.join(SKILL_DIR, "SKILL.md")
check(os.path.isfile(skill_md), "SKILL.md 存在")
if os.path.isfile(skill_md):
    text = open(skill_md, encoding="utf-8").read()
    fm = text.split("---")[1] if text.startswith("---") else ""
    check("name: fundamental-edge" in fm, "frontmatter name 正确")
    check("description:" in fm and len(fm.split("description:", 1)[1].strip()) > 80,
          "description 存在且足够详细")
    check("agent_created: true" in fm, "agent_created: true 已设置")
    check(len(text) < 40000, "SKILL.md 体量合理（精简原则）",
          f"{len(text)} 字符")

    # ---- 2. references 索引完整性 ----
    print("\n[2] references 索引")
    refs_dir = os.path.join(SKILL_DIR, "references")
    listed = sorted(set(re.findall(r"references/([A-Za-z0-9_\-.]+\.md)", text)))
    on_disk = sorted(f for f in os.listdir(refs_dir) if f.endswith(".md")) \
        if os.path.isdir(refs_dir) else []
    for r in listed:
        p = os.path.join(refs_dir, r)
        check(os.path.isfile(p) and os.path.getsize(p) > 500,
              f"索引引用 {r}", f"{os.path.getsize(p) if os.path.isfile(p) else 0} 字节")
    orphan = [f for f in on_disk if f not in listed]
    check(not orphan, "无孤儿 reference 文件", ", ".join(orphan) if orphan else "")
    check(len(listed) == len(on_disk), "索引数量 == 磁盘数量",
          f"{len(listed)} vs {len(on_disk)}")

    # ---- 3. 页码引用 ----
    print("\n[3] 页码引用标记")
    # 两种格式：模块页码 [M1 p.97]；文献页码（*Calculate ROIC*, p.1）——半角/全角括号都支持
    cite_pat = re.compile(
        r"\[M\d+ p\.\d+\]"
        r"|[（(]\s*\*[^)）]*\*\s*,\s*p\.\d+\s*[)）]"
        r"|[（(][A-Za-z][^)）]*,\s*p\.\d+\s*[)）]")
    no_cite = []
    for f in on_disk:
        body = open(os.path.join(refs_dir, f), encoding="utf-8").read()
        if not cite_pat.search(body):
            no_cite.append(f)
    check(not no_cite, "每个 reference 都含页码引用标记",
          ", ".join(no_cite) if no_cite else "")

# ---- 4. scripts ----
print("\n[4] scripts")
scripts_dir = os.path.join(SKILL_DIR, "scripts")
py_files = sorted(f for f in os.listdir(scripts_dir) if f.endswith(".py")) \
    if os.path.isdir(scripts_dir) else []
check(len(py_files) >= 4, "脚本数量 >= 4", f"{len(py_files)} 个")
import py_compile
_pyc_dir = os.path.join(SKILL_DIR, ".pyc_check")
os.makedirs(_pyc_dir, exist_ok=True)
try:
    for f in py_files:
        p = os.path.join(scripts_dir, f)
        try:
            py_compile.compile(p, doraise=True,
                               cfile=os.path.join(_pyc_dir, f + "c"))
            check(True, f"可编译 {f}")
        except Exception as e:
            check(False, f"可编译 {f}", str(e)[:80])
finally:
    for fn in os.listdir(_pyc_dir):
        try:
            os.remove(os.path.join(_pyc_dir, fn))
        except OSError:
            pass
    try:
        os.rmdir(_pyc_dir)
    except OSError:
        pass

# ---- 5. assets ----
print("\n[5] assets")
assets_dir = os.path.join(SKILL_DIR, "assets")
if not os.path.isdir(assets_dir):
    print("  SKIP  assets/ 不存在（本仓库刻意不含课件原始 Excel；"
          "需自备时从课件库复制，结构见 SKILL.md 第 4 节）")
    xl = []
else:
    xl = sorted(f for f in os.listdir(assets_dir) if f.endswith(".xlsx"))
    check(len(xl) >= 3, "Excel 模板 >= 3", f"{len(xl)} 个")
try:
    import openpyxl
    for f in xl:
        p = os.path.join(assets_dir, f)
        try:
            wb = openpyxl.load_workbook(p, read_only=True)
            check(len(wb.sheetnames) > 0, f"可打开 {f}", f"{len(wb.sheetnames)} 个 sheet")
            wb.close()
        except Exception as e:
            check(False, f"可打开 {f}", str(e)[:80])
except ImportError:
    print("  SKIP  openpyxl 未安装")

print("\n" + ("=" * 60))
print("结果：全部通过 ✅" if ok else "结果：存在失败项 ❌")
print("=" * 60)
sys.exit(0 if ok else 1)
