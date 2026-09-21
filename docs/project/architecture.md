# 仓库架构

Jade Lab 按内容用途组织多个独立项目。本文说明目录分类、项目组成、依赖关系和根检查范围；新机器准备见
[`README.md`](../../README.md)，Agent 修改流程见 [`AGENTS.md`](../../AGENTS.md)。

## 设计目标

仓库服务于长期个人学习、算法练习和小型工程验证，优先保证以下能力：

1. 根据用途快速找到代码和记录。
2. 在目标目录恢复依赖并运行最窄检查。
3. 让根检查与 CI 使用相同命令。
4. 让每个项目独立管理依赖、验证周期和运行条件。

根任务采用显式项目列表；语言覆盖和验证深度由现有内容决定。

## 内容分类

| 位置 | 职责 | 完成标准 |
| --- | --- | --- |
| `algo/<platform>/` | 由平台和稳定题目标识符定位的题解 | 题目标识符、语言目录、可重做的本地用例 |
| `algo/copypasta/` | 竞赛时查阅和复制的算法与数据结构实现 | 按语言组织，提供行为测试或编译检查 |
| `learning/<topic>/` | 有明确学习使命的课程、资料、课程专用实现和学习记录 | 目标、能力路线、恢复入口和表现检查 |
| `labs/<name>/` | 可独立运行的实验、语言示例或框架验证 | README、独立环境和可重做命令 |
| `tools/<name>/` | 由开发者或 CI 直接运行、完成具体操作的程序 | 启动命令、输入、运行结果、失败表现、依赖和自动测试 |
| `references/<project>/` | 固定到具体提交的外部参考源码 | Git submodule 和父仓库记录的 gitlink |
| `docs/` | 跨项目长期有效的规则 | 明确读者、维护位置和引用对象 |
| `.scratch/` | 本机调查、临时构建和可重建输出 | 由使用它的命令按需创建 |

`.scratch/` 由 Git 忽略，一级内容目录保持稳定。

## 如何选择位置

按以下顺序判断：

1. 本机调查或可重建输出进入 `.scratch/`。
2. 源码由外部项目维护，只需要固定版本阅读：作为 `references/` 下的 Git submodule。
3. 内容由在线判题平台和题目标识符定位：放入 `algo/<platform>/`。
4. 实现已经整理为竞赛复用算法：放入 `algo/copypasta/<language>/`。
5. 代码随主题学习目标和验证要求共同变化：放入 `learning/<topic>/exercises/`。
6. 开发者或 CI 需要反复执行一项具体操作：放入 `tools/<name>/`。
7. 它能独立运行，用于观察语言、框架、系统或数据结构行为：放入 `labs/<name>/`。
8. 它是跨项目长期有效的规则或决定：放入 `docs/`，并从相关入口链接。

## 目录内部结构

### 算法

在线判题目录使用 `algo/<platform>/<problem-id>/<language>/`。同一题目的多语言解答共享题目标识符，不按语言拆成
多个题目。Python 是主要算法语言；Go 用于学习和少量题解；C++ 历史算法实现保留编译检查。三种语言按已有主题分别
维护。

`algo/copypasta/` 按语言组织，语言目录内按主题平铺。新增实现说明输入、输出和复杂度，并提供与风险相称的测试或编译
检查。

### 学习工作区

学习主题的结构和恢复步骤由 [`learning/README.md`](../../learning/README.md) 定义。每个主题仅要求 README，集中维护
目标、当前状态、下一步、必要资料和检查命令；`exercises/`、`reference/` 和 `learning-records/` 按实际需要增加。
课程专用实现进入 `exercises/`，包括可以独立运行但仍随课程目标变化的代码；有课程之外的独立维护用途时，再按实验
或工具的职责确定位置。学习记录保存真实表现及证据边界，不把材料存在视为掌握。`learning/PROFILE.md` 维护跨主题
背景和稳定偏好，修改由用户逐项确认。

### 实验与工具

每个实验自行管理所需环境，并在 README 中说明目的、前置条件、运行命令、最窄检查和已知限制。

工具以进程为调用入口。新增工具说明启动条件、输入、成功结果、状态变化和失败恢复方式。`tools/` 当前为空。

### 外部源码与文档

外部源码的初始化和更新由 [`references/README.md`](../../references/README.md) 说明。父仓库记录 URL 和 gitlink。

文档按职责维护：

| 文档 | 职责 |
| --- | --- |
| `README.md` | 首次进入、环境准备和常用入口 |
| `docs/project/architecture.md` | 内容分类、项目组成、依赖关系和检查范围 |
| `CONTEXT.md` | 跨任务使用且容易混淆的领域名称 |
| `AGENTS.md` | 维护 Agent 的读取、修改和验证流程 |
| 项目 README | 该项目的目的、入口、限制和最窄检查 |

## 依赖关系

根 [`mise.toml`](../../mise.toml) 固定 Python、uv、Go、Java、Maven、CMake、Ninja、ShellCheck、shfmt 和 LeetGo，
`mise.lock` 固定 mise 能锁定的下载信息。Bash 判定环境由根配置中的容器镜像和版本变量提供。

项目依赖仍由项目自己管理：

- Python 项目使用各自的 `pyproject.toml` 和 `uv.lock`。
- Go 项目使用各自的 `go.mod`，需要外部模块时提交 `go.sum`。
- Java 项目使用各自的 `pom.xml`。
- C++ 算法手册使用自己的 `CMakeLists.txt`，构建结果写入 `.scratch/build/`。
- 外部参考源码版本由 `.gitmodules` 和父仓库 gitlink 共同确定。

依赖声明变化时同步更新适用的锁文件。共享能力以真实调用方、公开接口和维护者为前提，再决定其项目位置。

## 根检查

根任务是 `mise.toml` 中的显式命令列表。冷缓存运行会按需访问工具、语言依赖和容器镜像仓库；任务内容限定为本地
构建、静态检查和测试。

| 任务 | 当前内容 |
| --- | --- |
| `check:algo` | Python 手册的 pytest、Ruff、compileall；Go 手册的 gofmt、test、vet；C++ 手册的 CMake/Ninja 构建；LeetCode 88 的 Python 与 Go 本地检查 |
| `check:learning` | Go 练习的格式、test、race、vet、build；全部 Bash 练习脚本的 ShellCheck、shfmt；固定容器中的语义和日志分析测试。受管子进程清理测试只静态检查，有实现后手动验收 |
| `check:labs` | `btree`、`go-examples`、`java-examples`、`mapstruct`、`python-examples`、`python-observability`、`spring-web` |
| `check` | 按算法、学习工作区、实验的顺序运行以上三个任务 |

`labs/mybatis/` 的 Maven 编译和 MySQL 验证由项目 README 分别说明。`labs/unix-linux-programming/` 按章节选择源文件、
系统条件和编译参数。两类验证按目标项目单独运行。

CI 在 pull request 和 `master` push 上使用 Ubuntu 24.04 执行 `mise run check`，检出父仓库并运行 LeetCode 已提交的
本地用例。

新增、重命名或删除项目时，同步更新项目 README、所属目录 README、依赖声明、适用的锁文件、`mise.toml` 项目列表和
路径引用。分类规则、依赖关系或检查范围变化时同步更新本文。
