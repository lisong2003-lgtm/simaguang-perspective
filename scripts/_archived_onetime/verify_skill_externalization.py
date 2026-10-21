#!/usr/bin/env python3
"""Check whether SKILL externalization draft sections are covered by routing/packs."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parents[1]
DRAFT = PROJECT / "学习记录" / "主SKILL逐书判断尺外移草稿-2026-08-20.md"
INDEX = ROOT / "references" / "技能路由索引.md"
OUT = PROJECT / "学习记录" / "主SKILL外移覆盖核对-2026-08-20.md"

GROUP_MARKERS = [
    "模块",
    "协议",
    "补给",
    "新并入",
    "定向",
    "科技演化",
    "空间均衡",
    "金融制度",
    "关系平衡",
    "领导转变",
    "个人成长",
    "历史文章",
    "多通道观察",
    "工程实践",
    "江湖生存",
    "系统连接",
    "科学思维",
    "与市场",
    "与芯片",
    "思维",
    "方法",
    "能力",
    "判断尺",
]

PACK_ALIASES = {
    "第一哲学沉思集": ["笛卡尔-第一哲学沉思集"],
    "理解媒介": ["理解媒介-麦克卢汉"],
    "理解媒介：论人的延伸": ["理解媒介-麦克卢汉"],
    "犯罪心理学－ID": ["犯罪心理学"],
    "弘一法师": ["弘一法师全集"],
    "心理学家的读脸术": ["读脸术"],
}


def norm(text):
    return re.sub(r"[\s《》()（）,:：\-_—/\\，。；、]+", "", text).lower()


PACK_ALIASES_NORM = {
    norm(key): {norm(alias) for alias in aliases}
    for key, aliases in PACK_ALIASES.items()
}


def active_match(key, pack_names):
    if key in pack_names:
        return True
    aliases = PACK_ALIASES_NORM.get(key, set())
    return any(alias in pack_names or any(pack in alias or alias in pack for pack in pack_names) for alias in aliases)


def main():
    draft = DRAFT.read_text(encoding="utf-8")
    index_text = INDEX.read_text(encoding="utf-8")
    pack_names = {
        norm(path.parent.name)
        for path in (PROJECT / "书籍蒸馏").rglob("SKILL.md")
        if "/skills/" in str(path)
    }
    legacy_names = {
        norm(path.parent.name)
        for path in (PROJECT / "其他书籍").rglob("SKILL.md")
    }
    haystack = norm(index_text)

    headings = []
    for line in draft.splitlines():
        m = re.match(r"^### (.+)$", line.strip())
        if m:
            headings.append(m.group(1).strip())
    section_titles = []
    for line in draft.splitlines():
        m = re.match(r"^## (.+)$", line.strip())
        if m:
            section_titles.append(m.group(1).strip())

    missing_headings = []
    covered_headings = []
    legacy_only_headings = []
    group_headings = []
    for heading in headings:
        if re.search(r"N\d+", heading) or any(marker in heading for marker in GROUP_MARKERS):
            group_headings.append(heading)
            continue
        book = ""
        bm = re.search(r"《([^》]+)》", heading)
        if bm:
            book = bm.group(1)
        if book:
            key = norm(book)
            active = bool(key and active_match(key, pack_names))
            legacy_only = bool(not active and key in legacy_names)
        else:
            tokens = re.findall(r"[\u4e00-\u9fff]{2,}", heading)
            active = False
            legacy_only = False
            for token in tokens:
                key = norm(token)
                if len(key) <= 4:
                    active = active_match(key, pack_names)
                else:
                    active = (
                        key in haystack
                        or active_match(key, pack_names)
                        or any(
                            norm(pack) in key or key in norm(pack)
                            for pack in pack_names
                        )
                    )
                if active:
                    active = True
                    break
                if key in legacy_names or any(
                    norm(pack) in key or key in norm(pack)
                    for pack in legacy_names
                ):
                    legacy_only = True
        if active:
            covered_headings.append(heading)
        elif legacy_only:
            legacy_only_headings.append(heading)
        else:
            missing_headings.append(heading)

    missing_sections = []
    group_sections = []
    for title in section_titles:
        if "并入的" in title and "判断尺" in title:
            group_sections.append(title)
            continue
        short = title.replace("并入的", "").replace("判断尺", "").strip()
        key = norm(short)
        if key and key in haystack:
            continue
        if any(part and norm(part) in haystack for part in re.split(r"[、，,]", short)):
            continue
        missing_sections.append(title)

    lines = [
        "# 主 SKILL 外移覆盖核对（2026-08-20）",
        "",
        "## 统计",
        "",
        f"- 草稿小节：{len(headings)}",
        f"- 书级小节：{len(headings) - len(group_headings)}",
        f"- 已覆盖书级小节：{len(covered_headings)}",
        f"- 仅旧技能包覆盖：{len(legacy_only_headings)}",
        f"- 未覆盖书级小节：{len(missing_headings)}",
        f"- 分组/协议小节：{len(group_headings)}",
        f"- 草稿大节：{len(section_titles)}",
        f"- 分组大节：{len(group_sections)}",
        f"- 未覆盖大节：{len(missing_sections)}",
        "",
        "## 未覆盖书级小节",
        "",
    ]
    for heading in missing_headings:
        lines.append(f"- {heading}")
    if not missing_headings:
        lines.append("- 无")
    lines += ["", "## 仅旧技能包覆盖（不能作为外移唯一依据）", ""]
    for heading in legacy_only_headings:
        lines.append(f"- {heading}")
    if not legacy_only_headings:
        lines.append("- 无")
    lines += ["", "## 未覆盖大节", ""]
    for title in missing_sections:
        lines.append(f"- {title}")
    if not missing_sections:
        lines.append("- 无")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"sections={len(headings)} covered={len(covered_headings)} missing={len(missing_headings)}")
    print(f"missing_sections={len(missing_sections)}")
    print(f"report={OUT}")


if __name__ == "__main__":
    main()
