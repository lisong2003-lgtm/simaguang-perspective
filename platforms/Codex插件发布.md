# Codex 插件市场发布说明

## 提交包

Codex 市场建议使用：

- `dist/simaguang-perspective-0.3.7-codex-marketplace.zip`

这个压缩包包含：

```text
simaguang-perspective-marketplace/
├── marketplace.json
└── plugins/
    └── simaguang-perspective/
        ├── .codex-plugin/plugin.json
        ├── README.md
        ├── LICENSE
        └── skills/
            └── simaguang-perspective/
```

## 本地测试

1. 解压 `simaguang-perspective-0.3.7-codex-marketplace.zip`。
2. 把整个 `simaguang-perspective-marketplace` 目录放到本地插件市场目录。
3. 在 Codex 中添加该本地市场。
4. 新开对话后输入：

```text
用司马光综合思维帮我分析一个跨部门项目该不该继续。
```

## 安装知识扩展

默认 Codex 插件是轻量版，只包含摘要层。需要完整逐书知识文件时，安装：

```text
dist/simaguang-perspective-0.3.7-codex-knowledge.zip
```

解压后，将 `simaguang-perspective/skills/simaguang-perspective/knowledge/` 合并到已安装插件对应目录。

## 公开提交

1. 将 `simaguang-perspective-marketplace` 上传到一个公开仓库。
2. 确认 `marketplace.json` 中的插件路径仍为 `./plugins/simaguang-perspective`。
3. 按 Codex 插件市场要求提交仓库地址和发布说明。
4. 等待平台审核。

## 提交材料

- `dist/simaguang-perspective-0.3.7-codex-plugin.zip`：插件单包
- `dist/simaguang-perspective-0.3.7-codex-marketplace.zip`：市场仓库包
- `dist/SHA256SUMS.txt`：校验值
- [发布提交材料](发布提交材料.md)：简介、隐私声明和能力边界
