# Bash 学习工作区

目标是能够安全地阅读、修改和测试日常自动化脚本。每天只从这里进入；课程目标、顺序和资料分别见
[MISSION.md](MISSION.md)、[CURRICULUM.md](CURRICULUM.md) 与 [RESOURCES.md](RESOURCES.md)。

## 现在开始

从仓库根目录运行：

```bash
mise run check learning-bash
open learning/bash/lessons/0001-how-shell-executes-commands.html
```

若第 1–12 课概念已经熟悉，直接进入
[第 13 课](lessons/0013-log-analysis-practice.html)，先运行真实练习基线：

```bash
mise run bash learning/bash/exercises/log-analyzer/test.sh
```

一次学习只完成一个可观察结果：读一节、预测命令行为、在临时目录验证、完成迁移题，最后重跑
`mise run check learning-bash`。失败时记录命令、状态和根因；不要只记录“看完”。

## 运行范围

课程判定环境固定为 GNU Bash 5.3.15：

```text
docker.io/library/bash:5.3.15-alpine3.24@sha256:a19c811ee9e97fa8a080001d82b8e0ded303f0795cffdb1cbd162731bc8ce208
```

`mise run check learning-bash` 会运行 ShellCheck、shfmt、固定 Bash 语义测试和日志分析器离线测试。macOS
自带 Bash 3.2 只用于观察兼容差异，不是课程判定环境。

## 材料职责

- `lessons/`：13 节短课，包含预测题和实践任务。
- `exercises/`：课程唯一的可执行练习与测试；第 13 课直接引用这里的源码。
- `learning-records/`：历史学习记录，不等于当前掌握证明。
- `reference/`、`anki/`：按需查阅，不作为课程入口。
- [AUDIT.md](AUDIT.md)：2026-08-12 的事实修订和验证范围。

代码与目录去向统一由 [仓库架构](../../docs/project/architecture.md) 定义，本 README 不重复分类规则。
