# Go 学习工作区

本工作区服务于一个目标：掌握 Go 语言和常见后端工程能力，能够求职、维护真实 Go 项目并独立交付后端服务。
课程以表现而不是累计课时判断是否掌握。

## 阅读顺序

1. [MISSION.md](MISSION.md)：长期目标和 10/20/35/50 小时表现标准。
2. [CURRICULUM.md](CURRICULUM.md)：从语言基础到 leetgo、Dagu、后端实验和 Nuclei 的课程顺序。
3. [CASES.md](CASES.md)：固定版本、共同准备规则和案例入口。
4. [RESOURCES.md](RESOURCES.md)：Go 官方资料、固定版本源码和项目官方文档。
5. [第 1 课](lessons/0001-python-to-go-mindset.html)：从 Python 后端开发切换到 Go 的第一组可验证差异。

当前只有[已确认基础与课程方向](learning-records/0001-confirmed-background-and-course-direction.md)这一份学习记录。
它证明了学习目标和已有背景，不证明 Phase 0 或后续课程已经完成。

## 案例职责

| 案例 | 详细路径 | 课程作用 |
| --- | --- | --- |
| leetgo | [cases/leetgo.md](cases/leetgo.md) | 语言、CLI、HTTP、文件、子进程和第一项真实修改 |
| Dagu | [cases/dagu.md](cases/dagu.md) | 实际个人自动化、后端、队列、恢复和 gRPC worker |
| 后端能力实验 | [cases/backend-capability-lab.md](cases/backend-capability-lab.md) | 从零证明 HTTP、PostgreSQL、有限 worker、取消和关闭能力 |
| Nuclei | [cases/nuclei.md](cases/nuclei.md) | 三小时比较高并发网络程序的并发、限速和 HTTP 资源管理 |

这些仓库是案例，不是通用最佳实践的证明。结论必须同时依据可观察行为、固定版本源码、测试和一手文档。

## 学习产物的位置

- 课件与即时测验保存在 `lessons/` 和 `assets/`。
- 已证明掌握的知识写入 `learning-records/`，不记录单纯阅读或课件交付。
- 调用说明、阶段评估和精简测试结果在首次产生时创建 `evidence/`；大型原始日志放 `.scratch/`。
- 后端任务接纳实验开始实现时进入仓库根目录 `labs/scheduling/job-intake-go/`，本目录只保留任务说明和链接。
- 既有语言机制程序保存在 [`labs/languages/go-fundamentals/`](../../labs/languages/go-fundamentals/)；只在当前课需要
  最小反例时使用，程序存在不算课程掌握证据。
- 具有明确公开接口和消费方测试、能被其他代码依赖的实现进入按能力命名的 `packages/<name>/`；由人或自动化
  系统直接启动、完成重复工作流程的程序进入 `tools/`。
- leetgo、Dagu 和 Nuclei 按 [CASES.md](CASES.md) 的 commit 获取到仓库外或 `.scratch/`。只有决定长期保留并维护时，
  才分别加入 `references/` submodule。

## 当前状态

课程设计、固定版本和代码路径已核对。Dagu v2.13.0 与 Nuclei v3.11.1 的课程目标包已在 Go 1.26.5 和空缓存
环境中编译通过，见[冷缓存编译记录](evidence/0001-pinned-case-cold-builds.md)。这只证明课程环境可准备，不证明
对应课程已经学习或业务行为已经验证；学习仍从 Phase 0 的表现检查开始。
