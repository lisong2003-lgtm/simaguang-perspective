#!/usr/bin/env python3
"""Extract per-book judgment sections from SKILL.md into a draft without editing SKILL.md."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
OUT = ROOT.parents[1] / "学习记录" / "主SKILL逐书判断尺外移草稿-2026-08-20.md"


def section(lines, start_marker, end_marker):
    start = None
    end = None
    for index, line in enumerate(lines):
        if start is None and line.startswith(start_marker):
            start = index
        elif start is not None and line.startswith(end_marker):
            end = index
            break
    if start is None or end is None:
        raise ValueError(f"section not found: {start_marker} -> {end_marker}")
    return lines[start:end]


def main():
    lines = SKILL.read_text(encoding="utf-8").splitlines(keepends=True)
    try:
        first = section(lines, "## 并入的三书判断尺", "## 输入层 + 四层认知架构")
        second = section(lines, "## 并入的中医入门判断尺", "## 我绝不会做的事")
    except ValueError:
        print("ALREADY_EXTERNALIZED")
        return
    content = [
        "# 主 SKILL 逐书判断尺外移草稿（2026-08-20）\n",
        "\n",
        "> 本文件由 `scripts/prepare_skill_externalization.py` 从当前主 SKILL 原样抽出，主 SKILL 未修改。\n",
        "> 用途：供核对逐书判断尺是否已在技能包/技能路由索引中覆盖；批准后再从主 SKILL 删除并切换到按需读取。\n",
        "\n",
        f"- 抽出行数：{len(first) + len(second)}\n",
        "\n",
        "---\n",
        "\n",
    ]
    content.extend(first)
    content.extend(second)
    OUT.write_text("".join(content), encoding="utf-8")
    print(f"extracted_lines={len(first) + len(second)}")
    print(f"draft={OUT}")


if __name__ == "__main__":
    main()
