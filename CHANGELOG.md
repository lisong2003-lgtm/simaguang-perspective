# Changelog


## 0.4.5 (2026-10-21)
- 三平台对齐（cross-platform + i18n overseas）：README.en.md、`--lang en|zh` 主入口、i18n.py、CFI 三平台 workflow 全绿。
- 不改变业务算法/中文模板；平台专用调整只改发布副本。

# CHANGELOG

## 0.4.3（2026-10-18）

- 新增 `references/实时与历史报道素材索引.md`、`references/报道式决策案例库.md`、`references/跨源交叉核验协议.md`，登记 5 条历史 + 6 条实时脱敏公开素材，收录 7 个报道式决策案例。
- 路由测试提示词从 303 条扩到 311 条，新增 8 条报道式决策素材触发用例。
- 版本统一本机 / SkillHub / GitHub / ClawHub：0.4.3。
- 自检结果：`routing_accuracy_status=OK`（311 条 missed=0）、`INTEGRATION_OK`、发布合规扫描 0 命中。

## 0.4.2（2026-10-11）

- 新增 `references/使用边界与复核清单.md`：历史/预测/易学内容仅供结构参考，不替代专业判断。
- `SKILL.md` / `SKILL.lite.md` 版本统一 0.4.2。
- 自检：303 条路由提示词 `routing_accuracy_status=OK`。
