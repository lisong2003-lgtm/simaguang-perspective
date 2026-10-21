#!/usr/bin/env python3
"""Remove externalized per-book judgment sections from SKILL.md after backup validation."""

import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
SKILL = ROOT / "SKILL.md"
BACKUP = PROJECT / "学习记录" / "快照" / "20260820-主SKILL完整备份" / "SKILL.md"

MARKER = [
    "## 逐书判断尺（已外移）\n",
    "\n",
    "逐书判断尺已外移到 `references/技能路由索引.md` 和 `书籍蒸馏/*/skills/*/SKILL.md`；本主 SKILL 不再内嵌全文。完整备份见 `学习记录/快照/20260820-主SKILL完整备份/`。\n",
    "\n",
]


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    current_text = SKILL.read_text(encoding="utf-8", errors="ignore")
    if "## 逐书判断尺（已外移）" in current_text:
        print("ALREADY_EXTERNALIZED")
        return
    if not BACKUP.exists():
        raise SystemExit("BACKUP_MISSING")
    if sha256(SKILL) != sha256(BACKUP):
        raise SystemExit("BACKUP_CHECKSUM_MISMATCH")

    lines = current_text.splitlines(keepends=True)
    start1, end1 = find_block(lines, "## 并入的三书判断尺", "## 输入层 + 四层认知架构")
    start2, end2 = find_block(lines, "## 并入的中医入门判断尺", "## 我绝不会做的事")
    removed = (end1 - start1) + (end2 - start2)

    new_lines = lines[:start1] + MARKER + lines[end1:start2] + lines[end2:]
    SKILL.write_text("".join(new_lines), encoding="utf-8")
    print(f"removed_lines={removed}")
    print(f"new_skill_lines={len(new_lines)}")


if __name__ == "__main__":
    main()
