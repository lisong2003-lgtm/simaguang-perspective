#!/usr/bin/env python3
"""Build a compact cold-start handoff card for new conversations or new computers."""

import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
LEARNING = ROOT / "学习记录"


def head(path: Path, n: int = 25) -> str:
    if not path.exists():
        return f"[missing] {path}"
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore").splitlines()[:n])


def tail(path: Path, n: int = 30) -> str:
    if not path.exists():
        return f"[missing] {path}"
    return "\n".join(path.read_text(encoding="utf-8", errors="ignore").splitlines()[-n:])


def pending(path: Path, keywords=("下一步", "待提供", "待训练", "仍待")) -> str:
    if not path.exists():
        return f"[missing] {path}"
    lines = [
        line.strip()
        for line in path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if any(k in line for k in keywords)
    ]
    return "\n".join(lines[-12:]) or "无待办"


def main():
    date = datetime.date.today().isoformat()
    parts = [
        f"# 司马光综合思维交接卡（{date}）",
        "",
        "## 冷启动顺序",
        "",
        "1. 读取项目 `AGENTS.md`，按身份和项目规则执行。",
        "2. 读取 `PIPELINE_STATE.md`，确认当前阶段和最近并入。",
        "3. 读取 `学习记录/记忆与交接协议-2026-08-16.md`。",
        "4. 读取 `学习记录/学习日志.md` 和 `学习记录/LESSONS.md`。",
        "5. 运行 `python3 skills/simaguang-perspective/scripts/check_integration.py` 验证技能完整性。",
        "",
        "## 当前状态",
        "",
        "```text",
        head(ROOT / "PIPELINE_STATE.md", 20),
        "```",
        "",
        "## 最近学习",
        "",
        "```text",
        tail(LEARNING / "学习日志.md", 25),
        "```",
        "",
        "## 待办",
        "",
        "```text",
        pending(ROOT / "PIPELINE_STATE.md"),
        "```",
        "",
        "## 换电脑迁移",
        "",
        "1. 复制整个项目目录 `资治通鉴蒸馏/`，保留相对路径。",
        "2. 复制 `~/.codex/memories`、`~/.codex/lessons`、`~/.codex/AGENTS.md`。",
        "3. 如需保留全局技能和配置，再复制 `~/.codex/skills`、`~/.codex/config.toml` 及 CC Switch 配置。",
        "4. 新电脑安装后同步技能副本：`rsync -a skills/simaguang-perspective/ ~/.codex/skills/simaguang-perspective/`。",
        "5. 运行集成检查和能力覆盖矩阵，确认无缺失。",
        "",
        "生成时间：",
        date,
        "",
    ]
    text = "\n".join(parts)
    out = LEARNING / f"交接卡-{date}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"output: {out}")


if __name__ == "__main__":
    main()
