# 司马光综合思维（公开版）

一个以《资治通鉴》式历史校准为基础，融合现代系统思维、心理、法律、投资、侦查、易学、奇门和推演决策时机的综合决策技能。

GitHub：[lisong2003-lgtm/simaguang-perspective](https://github.com/lisong2003-lgtm/simaguang-perspective)
Release：[v0.3.1](https://github.com/lisong2003-lgtm/simaguang-perspective/releases/tag/v0.3.1)

## 产品说明

完整产品介绍、能力簇、使用场景、输出结构和边界见 [产品说明.md](产品说明.md)。
用户反馈的查看、分类、修复和回归流程见 [反馈处理流程.md](反馈处理流程.md)。

## 独立项目

本目录是独立发布项目，不依赖任何内部项目文件；可直接复制、安装、打包或上传到技能平台。

## 特点

- 28 个能力簇
- 303 条测试
- 来源可追溯
- 自学习闭环
- 模块按需增强，日常不强制展示
- 高生产力输出：项目策划、产品方案、论文报告、辩词、路演、商业计划书、小说与剧本
- 内嵌蒸馏强化：不依赖外部蒸馏 skill，强化“如何把书变成可执行判断尺”
- 影视摄影与 AI 短剧：分镜、MiniMax H3、Seedance 2.5 提示词和 AI 短剧流程
- 高质量交付：输出自检、事实核验、专业边界复核、真实反馈闭环
- AIGC 美学、镜头语法、电影构图、剪辑语法

已并入新增技能：中医入门、深度工作、网络是怎样连接的、战争艺术史、刻板印象、二十四史。
本轮公开版同步补齐 215 个逐书知识文件，覆盖非虚构写作、写作工艺、影视摄影、AIGC 提示词、战争论、东周列国志等最新并入内容。

## 安装

将本目录作为 Codex Skill 安装，或按目标平台的 Skill 格式打包。

## 目录

- `SKILL.md`：主技能入口
- `AGENTS.md`：项目规则
- `references/`：协议、方法网络、索引和模板
- `scripts/`：校验、复盘、溯源和蒸馏脚本
- `test-prompts.json`：测试集
- `examples/`：快速上手示例
- `platforms/`：Codex 插件和通用 Skill 平台适配文件
- `dist/`：已打包的发行压缩包

## 多平台发布包

- Codex 插件：`dist/simaguang-perspective-0.3.1-codex-plugin.zip`
- Codex 知识扩展：`dist/simaguang-perspective-0.3.1-codex-knowledge.zip`
- Codex 市场仓库：`dist/simaguang-perspective-0.3.1-codex-marketplace.zip`
- 通用 Skill：`dist/simaguang-perspective-public-0.3.1.zip`
- 知识扩展包：`dist/simaguang-perspective-public-0.3.1-knowledge.zip`
- 平台说明：[platforms/README.md](platforms/README.md)
- WorkBuddy 安装：[platforms/WorkBuddy安装.md](platforms/WorkBuddy安装.md)
- Codex 插件发布：[platforms/Codex插件发布.md](platforms/Codex插件发布.md)
- 综合 Skill 平台发布：[platforms/综合Skill平台发布.md](platforms/综合Skill平台发布.md)
- 介绍与演示：[platforms/介绍与演示.md](platforms/介绍与演示.md)
- 发布流程：[platforms/发布流程.md](platforms/发布流程.md)
- 平台发布步骤：[platforms/平台发布步骤.md](platforms/平台发布步骤.md)
- 发布检查清单：[platforms/发布检查清单.md](platforms/发布检查清单.md)
- 发布提交材料：[platforms/发布提交材料.md](platforms/发布提交材料.md)
- 发布前检查报告：[发布前检查报告.md](发布前检查报告.md)

重新打包：

```bash
python3 scripts/build_release.py
python3 scripts/build_knowledge_extension.py
```

## 用户选择

- 轻量包：主 SKILL + references + 215 条书籍摘要，token 更省。
- 知识扩展包：额外包含 215 个逐书知识文件，深度能力更强，按需读取。

## 常见问题

### 为什么完整版只显示一个 Skill？

完整版把 215 本书放在 `knowledge/books/<书>.md`，这些是知识数据，不是独立 Skill。

`v0.3.1` 已修复 WorkBuddy 把每个 `SKILL.md` 当成独立技能的问题：

- 旧版结构：`knowledge/books/<书>/SKILL.md`
- 新版结构：`knowledge/books/<书>.md`

如果旧版已经在 WorkBuddy 中出现多个技能，请删除旧版安装和残留技能，再安装 `v0.3.1`。

### SkillHub 版本会有这个问题吗？

SkillHub 当前提供的是轻量版，不包含 `knowledge/books/`，因此不会出现多个技能。

如果需要在 SkillHub 版中使用完整知识库，请从 GitHub Release 下载 `simaguang-perspective-public-0.3.1-knowledge.zip`，并按安装说明合并 `knowledge/books/`。

## 快速开始

```text
用司马光综合思维帮我分析一个跨部门项目该不该继续。

请给出：
1. 关键变量和最大风险
2. 两条以上可能路径
3. 当前最佳行动时点
4. 相反辩证视角
5. 需要验证的信息
```

## 授权

CC BY-NC-SA 4.0。不随公开版发布原始书籍文本。
