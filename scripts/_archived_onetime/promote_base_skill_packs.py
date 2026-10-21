#!/usr/bin/env python3
"""Create active skill packs for early base books from the externalization draft."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
DRAFT = PROJECT / "学习记录" / "主SKILL逐书判断尺外移草稿-2026-08-20.md"
OUT_ROOT = PROJECT / "书籍蒸馏" / "早期基础理论蒸馏" / "skills"

MAP = {
    "### 曾国藩修身处世（《挺经》）": ("挺经", "《挺经》技能包"),
    "### 曾国藩识人（《冰鉴》）": ("冰鉴", "《冰鉴》技能包"),
    "### 孙武决策（《孙子兵法》）": ("孙子兵法", "《孙子兵法》技能包"),
    "### 老子（《道德经》）": ("道德经", "《道德经》技能包"),
    "### 易经": ("易经", "易经技能包"),
    "### 庄子": ("庄子", "庄子技能包"),
    "### 鬼谷子": ("鬼谷子", "鬼谷子技能包"),
    "### 史蒂文·纳德勒（《思考，好与坏》）": ("思考好与坏", "《思考，好与坏》技能包"),
    "### 丹尼尔·卡尼曼（《思考，快与慢》）": ("思考快与慢", "《思考，快与慢》技能包"),
    "### 古斯塔夫·勒庞（《乌合之众》）": ("乌合之众", "《乌合之众》技能包"),
}


def extract_section(lines, heading):
    start = None
    for index, line in enumerate(lines):
        if line.strip() == heading:
            start = index + 1
            break
    if start is None:
        raise ValueError(f"heading not found: {heading}")
    end = len(lines)
    for index in range(start, len(lines)):
        if lines[index].startswith("### ") or lines[index].startswith("## "):
            end = index
            break
    return [line.strip() for line in lines[start:end] if line.strip()]


def main():
    lines = DRAFT.read_text(encoding="utf-8").splitlines()
    created = []
    for heading, (slug, title) in MAP.items():
        section = extract_section(lines, heading)
        out = OUT_ROOT / slug / "SKILL.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        content = [f"# {title}", "", "## 1. 司马光综合思维并入判断尺", ""]
        content.extend(section)
        content.append("")
        out.write_text("\n".join(content), encoding="utf-8")
        created.append(out)
    print(f"created={len(created)}")
    for path in created:
        print(path)


if __name__ == "__main__":
    main()
