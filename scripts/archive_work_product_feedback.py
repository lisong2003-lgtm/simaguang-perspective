#!/usr/bin/env python3
"""Append a real-work feedback entry to the high-productivity feedback archive."""

import argparse
import sys
from datetime import date
from pathlib import Path

DEFAULT_ARCHIVE = Path("运行目录/学习记录/高生产力真实反馈归档.md")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, help="output type")
    parser.add_argument("--title", required=True, help="short feedback title")
    parser.add_argument("--source", default="用户", help="feedback source")
    parser.add_argument("--category", default="其他", help="feedback category")
    parser.add_argument("--feedback", required=True, help="raw feedback text")
    parser.add_argument("--archive", default=str(DEFAULT_ARCHIVE))
    args = parser.parse_args()

    archive = Path(args.archive)
    archive.parent.mkdir(parents=True, exist_ok=True)
    existing = archive.read_text(encoding="utf-8") if archive.exists() else ""
    entry = (
        f"\n## {date.today().isoformat()} {args.type}：{args.title}\n"
        f"- 输出类型：{args.type}\n"
        f"- 反馈来源：{args.source}\n"
        f"- 反馈分类：{args.category}\n"
        f"- 原始反馈：{args.feedback}\n"
        f"- 根因判断：待归因\n"
        f"- 修改动作：待处理\n"
        f"- 更新项：待确认\n"
        f"- 待验证：待确认\n"
    )
    archive.write_text(existing.rstrip() + "\n" + entry, encoding="utf-8")
    print(f"appended: {archive}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
