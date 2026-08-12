# Bash 学习工作区

本工作区用于建立阅读、维护和编写日常自动化与部署脚本的能力。目标与限制见 [MISSION.md](MISSION.md)，
课程进度见 [CURRICULUM.md](CURRICULUM.md)，资料选择见 [RESOURCES.md](RESOURCES.md)。
旧课件的版本与事实复核见 [AUDIT.md](AUDIT.md)。

## 当前材料

- `lessons/`：13 份 HTML 课件；课件存在不自动表示已经掌握。
- `exercises/`：与课件共同演进的短练习及离线测试；当前包含第 13 课日志分析器。
- `learning-records/`：12 份由学习表现支持的记录。
- `reference/`：变量展开与引用速查页。
- `anki/`：候选卡片、当前批准集合、人工复核稿和历史增量。

第 13 课已有经过静态检查和固定运行时验证的练习，但当前没有对应学习记录。下一项有意义的任务不是继续增加
通用课件，而是由学习者完成该练习，或提供一份实际需要维护的部署脚本。

只服务于某一课、与课件和评分标准共同修改的短脚本可以放 `exercises/`。需要独立依赖或回答课程之外问题的实现
进入根 `labs/`；能够稳定完成日常重复工作流程后进入 `tools/`。完整运行日志和可能包含环境信息的调试输出保存在
`.scratch/`，不写入本工作区。

## 固定运行时与检查

课程运行时是 GNU Bash 5.3.15，对应 Docker Official Image：

```text
docker.io/library/bash:5.3.15-alpine3.24@sha256:a19c811ee9e97fa8a080001d82b8e0ded303f0795cffdb1cbd162731bc8ce208
```

macOS 自带的 Bash 3.2 不是课程判定环境。准备好 Docker/OrbStack 后，从仓库根目录运行：

```bash
mise run bash --version
mise run check learning-bash
mise run bash learning/bash/exercises/log-analyzer/test.sh
```

`mise run check learning-bash` 会运行 ShellCheck、shfmt、语法检查、GNU Bash 语义冒烟测试和日志分析器离线测试。
