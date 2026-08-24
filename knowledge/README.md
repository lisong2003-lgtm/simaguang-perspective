# 司马光综合思维 知识扩展

## 两层选择

默认轻量包只包含：

- 主 `SKILL.md`
- `references/`
- `knowledge/summaries/`：215 本书的紧凑摘要
- `scripts/`
- `examples/`
- `test-prompts.json`

可选知识扩展包额外包含：

- `knowledge/books/`：215 个逐书知识文件

这些文件是知识数据，不是独立 Skill。完整安装后，WorkBuddy/Codex 的技能列表里仍只显示一个 `simaguang-perspective`。

## 使用方式

- 默认安装：使用轻量包，日常问题按摘要和 references 判断。
- 需要深度能力：安装知识扩展包，按索引读取 1-3 个完整知识文件。
- 不能全量加载 `knowledge/books/`，否则 token 会大幅增加。
