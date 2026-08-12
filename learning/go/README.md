# Go 学习工作区

目标是掌握 Go 语言和常见后端工程能力，能够求职、维护真实 Go 项目并独立交付后端服务。课程按可观察表现
判断进度，不按累计课时自动判定掌握。

## 现在开始

当前阶段：Phase 0，第 1 课尚未留下完成证据。下一次学习只做下面一项 35–50 分钟任务：

```sh
mise install go
mise run check learning-go
open learning/go/lessons/0001-python-to-go-mindset.html
```

完成课件中的第 1 课练习，故意让一个测试失败并恢复，再运行 `mise run check learning-go`。将工具链、失败原因、
最终结果和下一步写入新的 `learning-records/`；只阅读或打开课件不算完成。

长期目标与阶段标准见 [MISSION.md](MISSION.md)，课程顺序见 [CURRICULUM.md](CURRICULUM.md)。固定案例版本见
[CASES.md](CASES.md)，查证入口见 [RESOURCES.md](RESOURCES.md)，教学规则见 [NOTES.md](NOTES.md)。

## 案例职责

| 案例 | 详细路径 | 课程作用 |
| --- | --- | --- |
| leetgo | [cases/leetgo.md](cases/leetgo.md) | 语言、CLI、HTTP、文件、子进程和第一项真实修改 |
| Dagu | [cases/dagu.md](cases/dagu.md) | 实际个人自动化、后端、队列、恢复和 gRPC worker |
| 后端能力实验 | [cases/backend-capability-lab.md](cases/backend-capability-lab.md) | 从零证明 HTTP、PostgreSQL、有限 worker、取消和关闭能力 |
| Nuclei | [cases/nuclei.md](cases/nuclei.md) | 三小时比较高并发网络程序的并发、限速和 HTTP 资源管理 |

这些仓库是案例，不是通用最佳实践的证明。结论必须同时依据可观察行为、固定版本源码、测试和一手文档。

## 本课程产物

- `lessons/` 保存课件和即时测验；`exercises/` 是受检查的课程练习 Go module。
- `learning-records/` 只记录已经通过解释、修改或测试证明的结果。
- `evidence/` 保存案例准备与阶段评估；大型原始日志放 `.scratch/`。
- 后端任务接纳实验开始实现时进入仓库根目录 `labs/scheduling/job-intake-go/`，本目录只保留任务说明和链接。
- 既有语言机制程序保存在 [`labs/languages/go-fundamentals/`](../../labs/languages/go-fundamentals/)；只在当前课需要
  最小反例时使用，程序存在不算课程掌握证据。
- leetgo、Dagu 和 Nuclei 按 [CASES.md](CASES.md) 的 commit 获取到仓库外或 `.scratch/`。只有决定长期保留并维护时，
  才分别加入 `references/` submodule。

其他代码的归类规则统一见 [仓库架构](../../docs/project/architecture.md)，本页不重复维护。

## 当前状态

课程设计、固定版本和代码路径已核对。Dagu v2.13.0 与 Nuclei v3.11.1 的课程目标包已在 Go 1.26.5 和空缓存
环境中编译通过，见[冷缓存编译记录](evidence/0001-pinned-case-cold-builds.md)。这只证明课程环境可准备，不证明
对应课程已经学习或业务行为已经验证；学习仍从 Phase 0 的表现检查开始。
