# 仓库架构

## 设计目标

Jade Lab 服务于一个主要维护者的学习、研究和小型工具开发。最稀缺的资源是连续注意力，因此目录结构只解决四个
问题：快速找到当前任务、按需恢复环境、判断代码是否已经验证，以及删除失去价值的内容。

仓库不是一个整体应用。模块没有共同发布周期，也不应依赖根目录的统一构建；每个模块拥有自己的依赖、README
和检查。根目录只提供模块索引、工具版本、环境诊断、公共规则检查和模块检查转发。

## 模块类型

| 类型 | 目录 | 主要调用方或读者 | 准入条件 |
| --- | --- | --- | --- |
| 学习工作区 | `learning/<topic>/` | 学习者 | 有明确使命、课程顺序、筛选资料、课程专用练习和表现检查 |
| 软件包 | `packages/<name>/` | 其他代码 | 可独立构建，通过公开接口使用，消费方测试持续通过 |
| 题解 | `problems/<platform>/` | OJ 平台与复习者 | 有稳定平台和题目标识符；允许未完成尝试 |
| 实验 | `labs/<area>/<name>/` | 研究者 | 有明确问题、预期结果、独立环境和重做命令 |
| 工具 | `tools/<name>/` | 人、CI 或定时任务 | 有命名工作流程、稳定进程入口和自动测试 |
| 外部参考源码 | `references/<project>/` | 源码研究者 | 需要长期重复阅读，以 submodule 固定 commit |

`docs/` 保存跨模块规则、研究结论和架构决定。`.scratch/` 保存本机票据、临时 clone、完整日志、构建输出和其他
可重建状态；跨机器需要保留的课程、结论和代码不得只存在于 `.scratch/`。

学习工作区中的 `exercises/` 只保存与某一课及其评分标准共同修改的短练习。需要独立依赖、能够脱离课程回答问题
或可能继续演进的实现属于根 `labs/`；这样不会在 `learning/` 和 `labs/` 下出现两个含义不同的 `labs/`。

`modules.toml` 的状态用于控制默认列表和表达当前维护方式：`stable` 表示公开行为由默认检查持续验证；`active`
表示当前课程、题解或实验；`incomplete` 表示源码保留但验证尚不足；`legacy` 表示仅按需维护；`external` 表示运行
依赖数据库、容器、公网或特定平台；`pinned` 只用于固定 commit 的外部参考源码。状态不替代各模块 README 中的
具体限制。

## 软件包

软件包的主要接口面向代码调用方。一个实现进入 `packages/` 前必须满足：

1. README 指出具体调用场景、提供的能力和不负责的内容。
2. 使用方只通过公开类型、函数或模块调用，不依赖内部文件布局。
3. 输入限制、返回值、可观察副作用和错误类型明确；外部输入在入口验证。
4. 测试从公开接口调用，覆盖正常路径、重要边界和主要错误。
5. 能构建成语言通常使用的依赖单元，例如 Python wheel、Go module、Java artifact 或原生库。
6. `modules.toml` 将模块标记为 `stable` 并加入默认检查；源码没有关键 `TODO`、空实现或同职责重复实现。

一级目录按能力命名，而不是建立 `packages/python/`、`packages/go/` 之类的大型语言抽屉。语言和运行时属于模块
元数据；不同发布周期或不同使用方的实现应是不同软件包。

## 工具

工具的主要接口面向进程调用方。它由人、CI 或定时任务直接启动，用来完成一个可以命名的重复工作流程。一个程序
进入 `tools/` 前必须说明：

1. 谁启动它、什么事件触发运行，以及成功后完成什么工作。
2. 每个受支持进程入口及其参数、配置、环境变量和外部依赖；多个入口必须说明用途差异。
3. stdout、stderr、退出码，以及会修改的文件、进程或远程状态。
4. 所需权限、敏感数据处理、重复执行结果和中断后的恢复方式。
5. 无需真实生产凭证即可运行的自动测试和本地验证命令。

工具内部可以拆成多个模块，但其他代码不能依赖这些内部模块。出现独立代码调用方时，把稳定、通用的部分提取到
`packages/`，工具只保留进程入口和流程编排。反过来，一个只有 CLI 包装、没有代码调用方的项目属于 `tools/`，
不因内部存在函数就变成软件包。

## 内容如何迁移

一次性且不准备保留的验证可以在 `.scratch/` 完成；决定保留的学习或研究代码必须进入有 README 和重做命令的
`labs/`，不能把 `.scratch/` 当作低成熟度源码目录。只有实际调用方式稳定后才决定后续去向：

- 其他代码需要依赖它：整理为 `packages/<name>/`，补公开接口、消费方测试和构建产物。
- 人或自动化系统需要重复执行它：整理为 `tools/<name>/`，补进程行为、退出码、风险说明和测试。
- 只对某次问题有解释价值：留在有完整重做说明的 lab，或删除并由 Git 历史负责恢复。
- 语言机制程序仍有独立验证价值：进入 `labs/languages/`；如果官方资料已完整替代且没有独立观察价值，再删除。

同一份实现只保留一个真实位置；学习工作区和文档使用相对链接引用，不复制代码。

## 根目录接口

- `modules.toml`：模块 ID、目录、类型、状态和模块原生检查命令。
- `mise.toml`：固定完整开发工具集，并提供 `modules`、`check`、`policy`、`doctor` 和 Bash 课程入口。
- `tools/repo-manager/`：读取模块索引并调用模块自己的构建或测试，不重新实现各语言构建系统。
- `README.md`：唯一的新机器入口和常用工作流。

`mise run check <id>` 只检查目标模块；`mise run policy` 才检查仓库结构、链接和内容规则。这样无关课件错误不会
阻止目标模块的最小反馈，公共规则仍可在 CI 中单独验证。

## 工具版本与外部源码

根 `mise.toml` 记录可复现的完整工具集，但新机器应按当前模块定向安装。只有出现真实的不兼容版本需求时，才在
子模块添加局部 `mise.toml`；mise 支持父子配置叠加和独立模块任务。

外部参考源码不是默认工作区的一部分。普通 clone 和 CI 都不递归下载 submodule；研究时使用
`git submodule update --init --recursive <path>` 获取仓库记录的 commit。公共规则通过 Git index 和
`.gitmodules` 验证记录，不要求外部源码工作树存在。

依据：

- [Go Modules Reference](https://go.dev/ref/mod)：Go module 是一起发布、版本化和分发的一组 package。
- [Python Packaging User Guide](https://packaging.python.org/en/latest/discussions/distribution-package-vs-import-package/)：
  区分可安装的 distribution package 与代码中的 import package。
- [uv Projects and workspaces](https://docs.astral.sh/uv/concepts/projects/workspaces/)：独立 Python 项目和工作区成员
  保留各自项目元数据。
- [CMake export](https://cmake.org/cmake/help/latest/command/export.html)：原生目标要成为外部构建可消费的 package，
  需要导出目标信息。
- [mise Monorepo Tasks](https://mise.jdx.dev/tasks/monorepo.html) 与
  [mise install](https://mise.jdx.dev/cli/install.html)：模块任务和按名称安装工具。
- [Git submodule](https://git-scm.com/docs/git-submodule)：按路径初始化并检出父仓库记录的 commit。

## 何时拆分仓库

只有出现以下真实条件时才迁出模块：

- 需要独立发布、版本号、issue 和使用者支持；
- 需要不同访问权限或包含不能公开的内容；
- 单个模块长期主导 clone、索引或 CI 成本；
- 模块拥有独立维护者和几乎独立的修改历史；
- 活跃模块之间存在无法由局部配置隔离的工具版本冲突。

在此之前，单仓库能降低检索和维护成本，不引入根 `go.work`、统一 Python 环境、Maven 聚合工程或新的通用构建层。
