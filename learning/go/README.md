# Go 学习工作区

目标是独立开发和交付 Go 后端：能修改程序并补测试，解释类型、值、错误与资源生命周期，交付可重复启动、
使用真实数据库且有明确停止行为的服务。以独立应用和可观察结果检验理解。

## 路线

| 顺序 | 内容与可观察结果 |
| --- | --- |
| 必要基础 | 类型、函数、值与指针、结构体、slice/map、错误和基本测试；能独立修改小程序 |
| HTTP | `net/http`、JSON、输入验证、错误响应、包与模块；得到可调用、可测试的接口 |
| PostgreSQL | SQL、迁移、约束、事务、连接清理；验证重启后的持久化和真实数据库行为 |
| 并发与生命周期 | 从小例子理解 goroutine、同步和取消，再引入有限后台处理与优雅关闭 |
| 部署 | 构建、本机 Linux 容器、配置、日志、健康检查、迁移、停止和重启；留下可重复运行说明 |

按当前问题细化路线；真实项目阅读、框架和进阶专题随实际需要引入。

## 当前与下一步

当前在必要语言基础阶段。固定工具链、程序运行、故意制造测试失败并恢复已有证据；对 `map[string]int`
缺失键的零值有初步理解。独立编码与竞态同步方案仍待验证，详见
[0002 练习记录](learning-records/0002-phase0-lesson01-toolchain-and-feedback.md)。

下一步从 [countWords](exercises/lesson01/main.go) 做一次小变更，讲清参数和返回类型、局部类型推断、值与参数传递。
区分普通值复制与复制后仍共享底层数据的值，再预测结果或修改条件，用运行结果反馈。

## 工程入口

工具版本由根 [mise.toml](../../mise.toml) 和 [mise.lock](../../mise.lock) 维护。从仓库根目录运行：

```sh
sh learning/go/check.sh
```

检查包含格式、普通测试、竞态检测、静态分析和构建；单独运行当前练习见[练习入口](exercises/README.md)。
首次按需执行 `mise install go`，通过 mise 使用固定工具链。课程专用实现的位置见[仓库架构](../../docs/project/architecture.md)。

## 当前资料

- [Go 语言规范](https://go.dev/ref/spec)：类型、赋值、参数和语言保证。
- [Go 工具命令](https://go.dev/doc/cmd)与[工具链](https://go.dev/doc/toolchain)：运行、构建、测试与版本选择。
- [testing](https://pkg.go.dev/testing)与[数据竞争检测器](https://go.dev/doc/articles/race_detector)：测试接口与检测范围。
