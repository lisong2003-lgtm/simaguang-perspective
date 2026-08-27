# 多平台发布说明

公开版按两种交付形态打包：

| 形态 | 压缩包 | 适用场景 |
|---|---|---|
| Codex 插件 | `dist/simaguang-perspective-0.3.7-codex-plugin.zip` | Codex 插件生态、本地插件安装 |
| Codex 知识扩展 | `dist/simaguang-perspective-0.3.7-codex-knowledge.zip` | 为 Codex 插件补充完整逐书知识文件 |
| Codex 市场仓库 | `dist/simaguang-perspective-0.3.7-codex-marketplace.zip` | 上传公开仓库、提交 Codex 插件市场 |
| 通用 Skill | `dist/simaguang-perspective-public-0.3.7.zip` | OpenAI Skills、Claude Skills、通用 Skill 平台 |
| 知识扩展 | `dist/simaguang-perspective-public-0.3.7-knowledge.zip` | 需要完整逐书知识文件的深度用户 |

## Codex 插件包

插件包内已包含：

- `.codex-plugin/plugin.json`：Codex 插件清单
- `skills/simaguang-perspective/`：可被 Codex 识别的 Skill 目录
- `README.md`、`LICENSE`：安装说明和许可

本地测试时，解压后将 `skills/simaguang-perspective` 放入目标平台的 Codex 技能目录，或通过已配置的本地插件市场安装。

## 通用 Skill 包

通用包直接以 `simaguang-perspective-public/` 作为 Skill 根目录，包含：

- `SKILL.md`：主技能入口
- `references/`：协议、方法网络和索引
- `scripts/`：校验、复盘、溯源和蒸馏脚本
- `examples/`：快速上手示例
- `test-prompts.json`：303 条测试
- `README.md`、`LICENSE`、`manifest.json`

目标平台若要求 SKILL.md 带 YAML frontmatter，本包已满足。

## 发布流程

1. 打包与校验：运行 `scripts/build_release.py`，核对 `dist/SHA256SUMS.txt`。
2. 本地实测：先在 Codex、WorkBuddy 或目标平台导入，跑演示 Prompt，确认能正常调用。
3. 平台提交：按平台要求上传对应包，填写简介、隐私声明、能力边界、测试结果和 SHA256。
4. 审核与维护：审核通过后保留版本号、CHANGELOG 和更新入口；每次内容变更重新打包并更新校验值。

## 提交材料

- `dist/simaguang-perspective-public-0.3.7.zip`：通用 Skill 包
- `dist/simaguang-perspective-public-0.3.7-knowledge.zip`：可选知识扩展包
- `dist/simaguang-perspective-0.3.7-codex-plugin.zip`：Codex 插件单包
- `dist/simaguang-perspective-0.3.7-codex-marketplace.zip`：Codex 市场仓库包
- `dist/SHA256SUMS.txt`：校验清单
- `介绍与演示.md`：简介、演示 Prompt 和展示方式
- `发布提交材料.md`：平台提交文案和检查清单

## 发布前检查

```bash
python3 scripts/build_release.py
python3 scripts/check_integration.py
python3 scripts/run_test_prompts.py --prompts test-prompts.json
```

上传到公开平台需要对应平台的账号、渠道和审核流程；本目录只负责可复现打包和本地验证。

常见问题：

- 平台安全扫描可能拦截脚本：先查看扫描报告，再决定是否调整。
- 不同平台对 Skill 目录位置要求不同：以官方设置页为准。
- 上传后若无法触发：先确认是否新开对话，并确认包内 `SKILL.md` 被正确加载。

## 补充文档

- [WorkBuddy 安装说明](WorkBuddy安装.md)
- [Codex 插件发布说明](Codex插件发布.md)
- [综合 Skill 平台发布说明](综合Skill平台发布.md)
- [发布流程](发布流程.md)
- [平台发布步骤](平台发布步骤.md)
- [发布检查清单](发布检查清单.md)
- [介绍与演示](介绍与演示.md)
- [发布提交材料](发布提交材料.md)
