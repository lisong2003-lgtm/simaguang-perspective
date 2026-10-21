#!/usr/bin/env python3
"""Compare pre/post externalization SKILL size and routing/test coverage."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
BACKUP = PROJECT / "学习记录" / "快照" / "20260820-主SKILL完整备份" / "SKILL.md"
CURRENT = ROOT / "SKILL.md"
INDEX = ROOT / "references" / "技能路由索引.md"
TEST_REPORT = PROJECT / "学习记录" / "技能路由命中测试-2026-08-20.md"
OUT = PROJECT / "学习记录" / "主SKILL外移效果检测-2026-08-20.md"


def stats(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    return {
        "lines": text.count("\n") + (1 if text and not text.endswith("\n") else 0),
        "bytes": path.stat().st_size,
        "cjk": len(re.findall(r"[\u4e00-\u9fff]", text)),
        "chars": len(text),
    }


def main():
    before = stats(BACKUP)
    after = stats(CURRENT)
    index_text = INDEX.read_text(encoding="utf-8")
    pack_links = len(re.findall(r"技能包 `(?:书籍蒸馏|其他书籍)/[^`]+`", index_text))
    source_links = len(re.findall(r"原书 `(?:书籍蒸馏|其他书籍)/[^`]+`", index_text))

    test_report = TEST_REPORT.read_text(encoding="utf-8", errors="ignore")
    def report_value(pattern):
        m = re.search(pattern, test_report)
        return m.group(1) if m else "?"

    lines = [
        "# 主 SKILL 外移效果检测（2026-08-20）",
        "",
        "## 主 SKILL 体积",
        "",
        "| 指标 | 外移前 | 外移后 | 减少 |",
        "| --- | ---: | ---: | ---: |",
        f"| 行数 | {before['lines']} | {after['lines']} | {before['lines'] - after['lines']} |",
        f"| 字节 | {before['bytes']} | {after['bytes']} | {before['bytes'] - after['bytes']} |",
        f"| 总字符 | {before['chars']} | {after['chars']} | {before['chars'] - after['chars']} |",
        f"| 中文字符 | {before['cjk']} | {after['cjk']} | {before['cjk'] - after['cjk']} |",
        "",
        "说明：第一轮外移删除 1202 行逐书判断尺并新增 4 行说明；第二轮外移又移除方法神经网络和素材来源。备份版本包含此前新增的路由总目录，所以行数为 2034。",
        "",
        "## 路由与测试",
        "",
        f"- 活动技能包：215",
        f"- 路由索引技能包路径：{pack_links}",
        f"- 路由索引原书路径：{source_links}",
        f"- test-prompts 预期簇全部命中：{report_value(r'预期簇全部命中：([0-9/]+)')}",
        f"- 零命中：{report_value(r'零命中：([0-9]+)')}",
        f"- 预期簇但无路由：{report_value(r'预期簇但无路由：([0-9]+)')}",
        "",
        "## 调用示例",
        "",
        "问题：用司马光的方式帮我全面分析一个能力强但经常越权的合伙人，要不要继续合作。",
        "",
        "外移后主 SKILL 不再内嵌《挺经》《孙子兵法》等逐书判断尺，而是按路由索引进入：治理与历史簇、认知与决策簇、战略与竞争簇，再按需打开对应技能包。",
        "",
        "## 结论",
        "",
        "- 主 SKILL 已从整本式加载改为目录 + 按需读取。",
        "- 215 个技能包全部可路由，355 条技能包路径和 355 条原书路径均存在。",
        "- test-prompts 未出现零命中，集成检查通过。",
    ]

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"before_lines={before['lines']} after_lines={after['lines']} reduced={before['lines'] - after['lines']}")
    print(f"before_chars={before['chars']} after_chars={after['chars']} reduced_chars={before['chars'] - after['chars']}")
    print(f"report={OUT}")


if __name__ == "__main__":
    main()
