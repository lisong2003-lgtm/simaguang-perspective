#!/usr/bin/env python3
"""Check core integration files, knowledge packages, routing links and privacy."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "SKILL.md",
    "test-prompts.json",
    "manifest.json",
    "references/方法网络.md",
    "references/核心概念索引.md",
    "references/技能合并索引.md",
    "references/技能路由索引.md",
    "references/技能路由配置.md",
    "references/技能路由反馈日志.md",
    "references/素材来源索引.md",
    "references/技能异同表.md",
    "references/调用优化协议.md",
    "references/知识蒸馏日志.md",
    "references/自我学习日志.md",
    "references/学习循环协议.md",
    "references/对话与身份适配协议.md",
    "references/变化时空象数模块协议.md",
    "references/推演决策时机协议.md",
    "references/溯源标注协议.md",
    "references/蒸馏方法论强化技能包.md",
    "references/高生产力服务协议.md",
    "references/高生产力协作分工协议.md",
    "references/高生产力场景模板.md",
    "references/能力转工作成果清单.md",
    "references/AI影视工具与提示词协议.md",
    "references/小说剧本融合创作协议.md",
    "references/专业边界与复核清单.md",
    "references/事实与数据核验协议.md",
    "references/高生产力反馈闭环协议.md",
    "references/高生产力输出自检清单.md",
    "references/行业模板与评审标准库.md",
    "scripts/review_learning_log.py",
    "scripts/build_traceability_panel.py",
    "scripts/generate_work_product.py",
    "scripts/check_distillation_quality.py",
    "scripts/run_high_productivity_checks.py",
    "scripts/archive_work_product_feedback.py",
    "scripts/run_regression_evals.py",
    "knowledge/README.md",
]

EXPECTED_TEST_CASES = 303
EXPECTED_BOOKS = 215
EXPECTED_SUMMARIES = 215

PRIVACY_PATTERNS = [
    "/Users" + "/lis",
    "~/" + ".codex",
    "cc-" + "switch",
    "CC " + "Switch",
    "Tik" + "Tok",
    "林" + "深",
    "El" + "on",
    "Mu" + "sk",
    "马" + "斯克",
    "无" + "墨者",
    "成" + "人用品",
    "书籍蒸" + "馏/",
    "inp" + "ut/",
    "清" + "理版",
]


def main() -> int:
    ok = True
    for rel in REQUIRED:
        path = ROOT / rel
        exists = path.exists()
        ok = ok and exists
        print(f"{'OK' if exists else 'MISSING'} {rel}")

    prompts_path = ROOT / "test-prompts.json"
    if prompts_path.exists():
        data = json.loads(prompts_path.read_text(encoding="utf-8"))
        cases = data.get("test_cases", [])
        print(f"test_cases: {len(cases)} expected: {EXPECTED_TEST_CASES}")
        ok = ok and len(cases) == EXPECTED_TEST_CASES
    else:
        ok = False

    books = ROOT / "knowledge" / "books"
    summaries = ROOT / "knowledge" / "summaries"
    book_count = len([p for p in books.glob("*.md")]) if books.exists() else 0
    summary_count = len([p for p in summaries.glob("*.md")]) if summaries.exists() else 0
    print(f"knowledge_books: {book_count} expected: {EXPECTED_BOOKS}")
    print(f"knowledge_summaries: {summary_count} expected: {EXPECTED_SUMMARIES}")
    ok = ok and book_count == EXPECTED_BOOKS and summary_count == EXPECTED_SUMMARIES
    nested_skill_files = list(books.rglob("SKILL.md")) if books.exists() else []
    print(f"nested_skill_files: {len(nested_skill_files)} expected: 0")
    ok = ok and not nested_skill_files

    routing_path = ROOT / "references" / "技能路由索引.md"
    if routing_path.exists():
        routing_text = routing_path.read_text(encoding="utf-8")
        links = {
            name
            for name in re.findall(
                r"knowledge/books/([^/`\s]+)\.md", routing_text
            )
            if name != "*"
        }
        missing = [
            name for name in sorted(links) if not (books / f"{name}.md").exists()
        ]
        print(f"routing_links: {len(links)} missing_links: {len(missing)}")
        for name in missing[:20]:
            print(f"MISSING_ROUTING_BOOK {name}")
        ok = ok and not missing
    else:
        ok = False

    scan_targets = [
        ROOT / "SKILL.md",
        ROOT / "test-prompts.json",
        ROOT / "manifest.json",
        *sorted((ROOT / "references").glob("*.md")),
        *sorted((ROOT / "scripts").glob("*.py")),
        *sorted((ROOT / "knowledge" / "summaries").glob("*.md")),
    ]
    privacy_hits = []
    for path in scan_targets:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for pattern in PRIVACY_PATTERNS:
            if pattern in text:
                privacy_hits.append((str(path.relative_to(ROOT)), pattern))
    print(f"privacy_hits: {len(privacy_hits)}")
    for rel, pattern in sorted(set(privacy_hits))[:30]:
        print(f"PRIVACY_HIT {rel}: {pattern}")
    ok = ok and not privacy_hits

    print("INTEGRATION_OK" if ok else "INTEGRATION_INCOMPLETE")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
