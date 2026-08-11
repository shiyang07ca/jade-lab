# Issue tracker：本地 Markdown

本仓库的票据和规格文档（你可能称为 PRD）以 Markdown 文件存放在 `.scratch/` 下。

## 约定

- 每个特性一个目录：`.scratch/<feature-slug>/`
- 规格文档：`.scratch/<feature-slug>/spec.md`
- 实现票据：每个票据一个文件，位于 `.scratch/<feature-slug>/issues/<NN>-<slug>.md`，从 `01` 开始编号——不要合并成单一票据文件
- 分类状态记录在每个票据文件顶部的 `Status:` 行（角色字符串见 `triage-labels.md`）
- 评论和讨论历史追加到文件底部 `## Comments` 标题下

## 当技能要求"发布到 issue tracker"时

在 `.scratch/<feature-slug>/` 下创建新文件（必要时先创建目录）。

## 当技能要求"获取相关票据"时

读取引用路径对应的文件。用户通常会直接传入路径或票据编号。

## Wayfinding 操作

由 `/wayfinder` 使用。**map** 是一个文件，每个票据对应一个**子**文件。

- **Map**：`.scratch/<effort>/map.md` —— 记录 Notes / Decisions-so-far / Fog 正文。
- **子票据**：`.scratch/<effort>/issues/NN-<slug>.md`，从 `01` 开始编号，问题写在正文中。`Type:` 行记录票据类型（`research`/`prototype`/`grilling`/`task`）；`Status:` 行记录 `claimed`/`resolved`。
- **阻塞**：顶部的 `Blocked by: NN, NN` 行。当列出的每个文件都是 `resolved` 时，票据解除阻塞。
- **前沿**：扫描 `.scratch/<effort>/issues/` 中打开、未阻塞、未认领的文件；编号小的优先。
- **认领**：在开始工作前设置 `Status: claimed` 并保存。
- **解决**：在 `## Answer` 标题下追加答案，设置 `Status: resolved`，然后在 `map.md` 的 Decisions-so-far 中追加上下文指针（gist + 链接）。
