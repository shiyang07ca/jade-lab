# Agent 指南

## Agent skills

### Issue tracker

任务票据、规格文档（固定文件名为 `spec.md`）和 Wayfinder 地图使用 `.scratch/` 下的本地 Markdown 管理。详见 `docs/agents/issue-tracker.md`。

### Triage labels

普通任务票据使用五个固定的任务分类状态：`needs-triage`、`needs-info`、`ready-for-agent`、`ready-for-human` 和 `wontfix`。详见 `docs/agents/triage-labels.md`。

### Domain docs

本仓库使用单一领域上下文布局：根目录 `CONTEXT.md` 与 `docs/adr/`。详见 `docs/agents/domain.md`。

## 文档语言与术语

- 面向项目成员的说明、规格文档、任务票据和架构决策记录默认使用中文。先给结论，再写清具体对象、
  动作、条件和依据。

- 领域概念使用 `CONTEXT.md` 中的中文主名称。不要在同一文档中交替使用中文名、英文名、缩写和
  自造译名指代同一概念。

- 外部规范或实现要求保留英文时，第一次出现先写中文含义，再在括号或代码格式中给出原名；后文
  使用中文名或精确标识符，不重复并列中英文。

- 标识符、API 名、协议名、命令、文件路径、配置键、状态值、错误消息和引用原文保持原样。
  Matt Pocock 文档技能要求的固定字段与标题，例如 `Type:`、`Status:`、`Blocked by:`、`## Question`、
  `## Answer` 和 Wayfinder 地图标题，也保持原样。

- 优先使用具体名词和动词，说明哪个文件、模块、数据、状态或决定发生了什么。不得用“对齐”“赋能”
  “抓手”“拉通”“闭环”“沉淀”“水位”“基座”“门禁”“口径”“链路”“拓扑”或“契约”等词
  代替具体说明；按语义改写为基础依赖、阻断条件、计算方法、调用路径、组件关系、规则或接口约束。

- `CONTEXT.md` 只保存稳定的领域词汇，不保存参数、验收条件或实现方案；这些内容分别写入规格文档、
  Wayfinder 票据或架构决策记录。

- 写完后检查：不了解相关技能的读者是否能理解发生了什么、为什么，以及下一步需要做什么。
