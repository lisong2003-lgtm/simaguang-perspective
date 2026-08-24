# 综合 Skill 平台发布说明

## 提交包

综合 Skill 平台使用通用包：

- `dist/simaguang-perspective-public-0.3.1.zip`

包内是标准 Agent Skills 目录：

```text
simaguang-perspective-public/
├── SKILL.md
├── references/
├── scripts/
├── examples/
├── sources/
├── test-prompts.json
├── README.md
├── LICENSE
└── manifest.json
```

## 提交流程

1. 进入目标平台的 Skill 市场或导入入口。
2. 选择 `simaguang-perspective-public-0.3.1.zip`。
3. 填写平台要求的名称、简介、分类、作者、隐私和免责声明。
4. 附上测试结果和 `SHA256`。
5. 提交后等待平台审核。

## 不同平台差异

- WorkBuddy：使用通用包，支持设置页导入或放入技能目录。
- Claude Skills / OpenAI Skills：通常直接识别 `SKILL.md`，导入后按平台要求确认目录位置。
- 其他综合 Skill 平台：以平台官方要求为准。

## 提交材料

- `dist/simaguang-perspective-public-0.3.1.zip`
- `dist/SHA256SUMS.txt`
- [发布提交材料](发布提交材料.md)
