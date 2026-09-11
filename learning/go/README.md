# Go 学习工作区

以独立交付 Go 后端为主，兼顾求职，通过真实项目维护练习能力。学习路线是必要语言基础、最小 HTTP 服务、
PostgreSQL、并发与关闭、Linux 容器部署；leetgo 和 Dagu 按问题穿插阅读，不作为开发服务前的整套必修。

## 现在从哪里继续

当前处于必要语言基础阶段。学习者已提供固定工具链、程序运行和故意测试失败的证据，测试期望已恢复；
map 零值有初步理解。数据竞争、同步和独立编码尚未充分验证，不能据此判定旧 Phase 0 全部完成。

下一步围绕现有 `countWords` 做一个小变更，补上类型、值和参数传递的理解，不重做整套环境准备。
详见[当前单元](CURRICULUM.md#当前单元)和[最近练习记录](learning-records/0002-phase0-lesson01-toolchain-and-feedback.md)。

需要核对环境或修改练习后，从仓库根目录运行：

```sh
mise run check learning-go
```

首次准备机器时按当前需要执行 `mise install go`，不预先安装或获取全部案例。裸 `go` 可能不是课程固定版本；
目标包命令见 [exercises/README.md](exercises/README.md)。既有[第 1 课课件](lessons/0001-python-to-go-mindset.html)
仅供参考，不要求整页读完再开始。

## 文档与产物

- [MISSION.md](MISSION.md)：目标和范围；[CURRICULUM.md](CURRICULUM.md)：课程顺序与当前单元。
- [NOTES.md](NOTES.md)：教学方式；[CASES.md](CASES.md)：固定版本与案例入口；[RESOURCES.md](RESOURCES.md)：按需查证资料。
- `exercises/` 保存短练习；`learning-records/` 保存实际证据、重要纠正和下一步，不记录每轮对话。
- 后端实验开始实现时进入根目录 `labs/scheduling/job-intake-go/`，范围见[实验说明](cases/backend-capability-lab.md)。
- `lessons/` 保留参考课件；`evidence/` 保留案例准备的历史验证，不代表学习者掌握了相关内容。
- 案例源码按需放仓库外或 `.scratch/`；Nuclei、Gin、Dagu 分布式专题和深入性能诊断为选修。

代码归属遵循[仓库架构](../../docs/project/architecture.md)。既有[冷缓存编译记录](evidence/0001-pinned-case-cold-builds.md)
只证明当时案例环境可准备，不替代当前业务测试或学习证据。
