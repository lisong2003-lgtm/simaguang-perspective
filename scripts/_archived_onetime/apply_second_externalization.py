#!/usr/bin/env python3
"""Externalize method network and material source sections from SKILL.md."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
SOURCE_REF = ROOT / "references" / "素材来源索引.md"


def find_block(lines, start_marker, end_marker):
    start = None
    end = None
    for index, line in enumerate(lines):
        if start is None and line.startswith(start_marker):
            start = index
        elif start is not None and line.startswith(end_marker):
            end = index
            break
    if start is None or end is None:
        raise ValueError(f"block not found: {start_marker} -> {end_marker}")
    return start, end


def main():
    lines = SKILL.read_text(encoding="utf-8").splitlines(keepends=True)

    start, end = find_block(lines, "## 方法神经网络", "## 我绝不会做的事")
    removed_method = end - start
    lines[start:end] = [
        "## 方法神经网络\n",
        "\n",
        "完整节点、连接、激活、执行和输出格式见 `references/方法网络.md`。\n",
        "\n",
        "核心链路：视觉输入（如需）→ L1 质检 → L2 分析 → L3 策略 → L4 仲裁 → 轮值主席 → 三方会诊 → 反方批判 → 冲突裁决 → 分层输出 → 复盘。\n",
        "\n",
    ]

    start2 = next(
        index for index, line in enumerate(lines) if line.startswith("## 素材来源")
    )
    material = "".join(lines[start2:])
    SOURCE_REF.write_text(material, encoding="utf-8")
    removed_material = len(lines) - start2
    lines[start2:] = [
        "## 素材来源\n",
        "\n",
        "技能包和原书路径见 `references/技能路由索引.md`；完整素材来源索引见 `references/素材来源索引.md`。\n",
    ]

    SKILL.write_text("".join(lines), encoding="utf-8")
    print(f"removed_method_lines={removed_method}")
    print(f"removed_material_lines={removed_material}")
    print(f"new_skill_lines={len(lines)}")


if __name__ == "__main__":
    main()
