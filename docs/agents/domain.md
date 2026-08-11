# Domain Docs

工程技能在探索代码库时应如何消费本仓库的领域文档。

## 探索前先读这些

- 仓库根目录的 **`CONTEXT.md`**，或
- 仓库根目录的 **`CONTEXT-MAP.md`**（若存在）——它指向每个上下文各一个 `CONTEXT.md`。阅读与主题相关的每一个。
- **`docs/adr/`** —— 阅读与你即将工作的领域相关的 ADR。在多上下文仓库中，还要检查 `src/<context>/docs/adr/` 中的上下文级决策。

如果这些文件不存在，**静默继续**。不要指出缺失，也不要主动建议创建。`/domain-modeling` 技能（通过 `/grill-with-docs` 和 `/improve-codebase-architecture` 触达）会在术语或决策实际落定时惰性创建它们。

## 文件结构

单上下文仓库（大多数仓库）：

```
/
├── CONTEXT.md
├── docs/adr/
│   ├── 0001-event-sourced-orders.md
│   └── 0002-postgres-for-write-model.md
└── src/
```

多上下文仓库（根目录存在 `CONTEXT-MAP.md`）：

```
/
├── CONTEXT-MAP.md
├── docs/adr/                          ← 系统级决策
└── src/
    ├── ordering/
    │   ├── CONTEXT.md
    │   └── docs/adr/                  ← 上下文级决策
    └── billing/
        ├── CONTEXT.md
        └── docs/adr/
```

## 使用词汇表的词汇

当你的输出命名一个领域概念（在票据标题、重构提案、假设、测试名中）时，使用 `CONTEXT.md` 中定义的术语。不要漂移到词汇表明确避免的同义词。

如果需要的概念尚未在词汇表中，这是一个信号——要么你在发明项目未使用的语言（重新考虑），要么存在真实缺口（记下供 `/domain-modeling` 处理）。

## 标记 ADR 冲突

如果你的输出与现有 ADR 矛盾，明确标记而不是静默覆盖：

> _Contradicts ADR-0007 (event-sourced orders) — but worth reopening because…_
