# Bash Anki 资料

- `cards.json`：当前 59 张候选卡片，是下一轮人工复核的输入。
- `approved.json`：当前累计批准的 57 张卡片，是同步到 Anki 的唯一输入。
- `review.md`：从候选集合生成的人工复核稿。
- `history/approved-YYYY-MM-DD.json`：现存的日期批次增量，用于解释累计集合的部分来源。最早的 11 张卡片没有
  独立历史文件，只存在于 `approved.json`；不凭 ID 反向伪造当时的复核记录。

修改卡片时先更新候选集合并生成复核稿；只有学习者明确批准的卡片才能进入 `approved.json`。Anki 导出文件、
本地数据库和同步状态可以重新生成，不进入本目录。
