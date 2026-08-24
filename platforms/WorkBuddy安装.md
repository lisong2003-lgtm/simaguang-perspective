# WorkBuddy 安装说明

## 直接下载链接

分享给其他用户时，使用下面的链接：

- 轻量包：[simaguang-perspective-public-0.3.1.zip](https://github.com/lisong2003-lgtm/simaguang-perspective/releases/download/v0.3.1/simaguang-perspective-public-0.3.1.zip)
- 知识扩展包：[simaguang-perspective-public-0.3.1-knowledge.zip](https://github.com/lisong2003-lgtm/simaguang-perspective/releases/download/v0.3.1/simaguang-perspective-public-0.3.1-knowledge.zip)

GitHub 发布页：https://github.com/lisong2003-lgtm/simaguang-perspective/releases/tag/v0.3.1

## 使用哪个包

安装 WorkBuddy 时使用通用 Skill 包：

- `dist/simaguang-perspective-public-0.3.1.zip`

不要使用 Codex 插件包，因为插件包内含 `.codex-plugin/plugin.json`，不是 WorkBuddy 需要的直接 Skill 结构。

## 安装方法

### 方法一：设置页导入

1. 打开 WorkBuddy。
2. 进入设置或技能管理页。
3. 点击“Import Skill”或“导入技能”。
4. 选择 `simaguang-perspective-public-0.3.1.zip`。
5. 导入后重启或新开对话。

### 方法二：复制到技能目录

1. 解压 `simaguang-perspective-public-0.3.1.zip`。
2. 把 `simaguang-perspective-public` 文件夹放入：
   - 项目级：`.codebuddy/skills/`
   - 用户级：`~/.workbuddy/skills/`（按 WorkBuddy 版本确认）
3. 重启 WorkBuddy 或新开对话。

## 安装后测试

```text
用司马光综合思维帮我分析一个跨部门项目该不该继续。
```

如果分析偏浅，先让 WorkBuddy 读取参考文件：

```text
请先读取 references/方法网络.md、references/核心概念索引.md 和 references/技能合并索引.md，再按司马光综合思维分析。
```

## 注意事项

- 完整版安装后，技能列表里只显示一个 `simaguang-perspective`；`knowledge/books/` 里的 215 个 `.md` 文件是知识数据，不是独立技能。
- 本 Skill 不内置识图、摄像头和 OCR；纯文字分析可直接使用，图片能力需额外视觉依赖。
- 如果 WorkBuddy 输出比 Codex 浅，优先确认它是否已读取 `references/`；未读取时应先按上面的提示让它读取。
- WorkBuddy 安装前可能做安全扫描。若脚本被拦截，先查看扫描报告，再决定是否调整。
- 如果 WorkBuddy 版本使用不同技能目录，以官方设置页显示的路径为准。
