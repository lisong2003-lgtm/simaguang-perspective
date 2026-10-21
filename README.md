# simaguang-perspective
**[English](./README.en.md) | [中文](./README.md)**


用司马光综合思维分析问题：以《资治通鉴》式历史校准为底座，覆盖历史、治理、商业、用人、识人、决策、博弈、心理、法律、投资、易学、影视创作和高生产力输出等跨尺度问题。

## 快速使用

- 触发词：`用司马光分析`、`司马光怎么看`、`全面分析`、`帮我决策`、`历史同构`、`相反辩证`、`项目策划`、`产品方案`、`论文`、`小说剧本`、`AI短剧`。
- 分析前按 `references/技能路由索引.md` 匹配能力簇；事件类问题先查 `references/实时与历史报道素材索引.md`。
- 交付前按 `references/使用边界与复核清单.md` 勾选人工复核项。

## 结构

- `SKILL.md` / `SKILL.lite.md`：主技能与轻量版（version 0.4.3）。
- `references/`：协议、路由、判断尺、素材与案例库。
- `scripts/`：路由测试、覆盖率、集成自检、蒸馏与高生产力检查。
- `test-prompts.json`：311 条路由测试提示词。

## 边界

- 不构成法律、医疗、投资、司法意见；不替用户做终局决定。
- 易学、风水、奇门只作文化启发，不用于现实重大决策。
- 推演不是预言；重大结果请人工复核。
- 公开版不含私人日志、公司内部数据、未授权版权原文。

## 自检

```bash
python3 scripts/test_routing_coverage.py
python3 scripts/check_integration.py
python3 scripts/run_test_prompts.py --prompts test-prompts.json
```

期望输出：`routing_accuracy_status=OK`、`INTEGRATION_OK`、`test_cases: 311`。

## 版本

- 0.4.3（2026-10-18）：新增事件素材与跨源核验三件套，路由测试扩到 311；全平台版本对齐。
