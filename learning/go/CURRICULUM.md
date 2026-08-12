# Go 课程大纲（10–50 小时，真实工程驱动）

> 使命与完成标准见 [MISSION.md](MISSION.md)，固定版本与源码路径见 [CASES.md](CASES.md)，一手资料见
> [RESOURCES.md](RESOURCES.md)。课程统一使用 Go 1.26.5。

## 如何使用这份大纲

- 下表时间只计算主动学习、编码、测试和复盘；依赖下载、冷缓存编译和前端构建准备不计入。
- 每个单元是 0.5–2 小时的任务组，实际执行时拆成 20–50 分钟的小节。每小节结束必须留下通过或失败的
  测试、调用说明、问题记录、代码修改或测量结果。
- 无固定学习节奏不是问题。每次回来先用 3–5 分钟不看笔记回忆上次的关键判断，再运行上次保存的命令。
- 先理解最小行为，再阅读真实实现；先观察失败，再修改代码；先取得测量结果，再谈性能优化。
- 案例用于观察现实限制和取舍，不代表其所有写法都适合新项目。

每次分析代码都回答五个问题：

1. 哪些值被复制，哪些状态被共享，它们活多久？
2. 不可信数据从哪里进入，在哪一层验证？
3. 失败如何保留原因并传给调用方，哪些失败可以重试？
4. 并发数量由什么限制，谁负责取消、等待和关闭？
5. 行为由什么测试、运行记录或测量结果证明？

## 总体路线

| 阶段 | 累计时间 | 主要结果 |
|---|---:|---|
| Phase 0–1 | 约 8 小时 | 建立 Go 语言、工具链、测试和并发基础，并直接映射到 leetgo |
| Phase 2 | 约 20 小时 | 完成 leetgo 的真实修改，达到“熟悉 Go”里程碑 |
| Phase 3 | 约 29 小时 | 实际使用 Dagu，并追踪一次本地工作流从输入到状态、日志和进程退出 |
| Phase 4 | 约 35 小时 | 从零完成一个带 HTTP、PostgreSQL、有限后台任务和优雅退出的后端能力实验 |
| Phase 5 | 约 45 小时 | 能诊断 Dagu 的队列、恢复和 gRPC worker 行为，并完成一项范围受控的修改 |
| Phase 6–7 | 约 50 小时 | 用 Nuclei 比较高并发网络程序，并完成求职与独立交付能力检查 |

## Phase 0 · 固定环境与最小反馈（1.5 小时，累计 1.5 小时）

| 单元 | 时间 | 核心任务 | 完成标准 |
|---|---:|---|---|
| 0.1 工具链与案例 | 0.5h | 核对 Go 1.26.5；获取 leetgo 并记录三个案例的固定 commit；检查代理、checksum database 和磁盘 | 能重复输出工具链、平台、commit 和依赖校验设置；Dagu/Nuclei 到对应阶段再获取 |
| 0.2 Python → Go 心智切换 | 0.5h | 完成第 1 课；区分静态类型、值语义、错误值、编译和运行 | 练习可运行；测验答案能解释原因 |
| 0.3 最小反馈 | 0.5h | 使用 `fmt`、`vet`、`test`、`-race`、`build`；故意制造一次测试失败和一次竞态 | 能只运行目标包和目标测试，并知道每个工具实际检查什么 |

主要资料：[Go 1.26 发布说明](https://go.dev/doc/go1.26)、[Go 工具链选择](https://go.dev/doc/toolchain)和
[Go 命令文档](https://go.dev/doc/cmd)。

## Phase 1 · 语言核心，直接映射到 leetgo（6.5 小时，累计 8 小时）

| 单元 | 时间 | 必备知识 | 实践对象与证明 |
|---|---:|---|---|
| 1.1 值、指针与生命周期 | 1.0h | 声明、named type、转换、数组/结构体复制、参数传递、`new`/`make`、方法接收者、零值、逃逸分析 | 对 `leetcode/models.go`、`config/state.go` 做复制与共享状态说明；用测试证明一次修改是否可见 |
| 1.2 切片、map、字符串与 Unicode | 1.0h | slice 描述符与底层数组、扩容、nil/empty、map 并发限制、byte/rune、`range` | 对 `lang/testcase.go`、`utils/str.go` 写边界测试和一个小 benchmark |
| 1.3 结构体、方法、接口与 nil | 1.2h | 组合与 embedding、方法集、隐式满足接口、type assertion/switch、typed nil、接口应由使用方按需要定义 | 从 `QuestionsCache` 的调用方解释接口存在的理由；制造并识别 typed nil 问题 |
| 1.4 函数、错误、`defer` 与异常边界 | 0.8h | 函数值、closure、`errors.Is/As/Join`、错误包装、资源清理、允许 `panic/recover` 的边界 | 跟踪一次 `pick` 或 `test` 失败，保留原始错误并增加必要上下文 |
| 1.5 并发、同步与取消 | 1.5h | goroutine、channel、`select`、mutex、atomic、`context`、happens-before | 写一个有上限、可取消、能等待结束的 worker 实验；运行 `go test -race` |
| 1.6 测试、包、模块与泛型 | 1.0h | table-driven test、子测试、临时目录、fuzz、benchmark、包初始化、`go.mod`、约束与类型推断 | 为一个无测试纯函数补测试；解释是否真的需要泛型或接口 |

主要资料：[Go 语言规范](https://go.dev/ref/spec)、[Go 内存模型](https://go.dev/ref/mem)、
[testing](https://pkg.go.dev/testing@go1.26.5) 和[竞态检测器](https://go.dev/doc/articles/race_detector)。

## Phase 2 · leetgo 主要动手案例（12 小时，累计 20 小时）

按照 [leetgo 案例路径](cases/leetgo.md) 学习，不从目录首页随机跳读。

| 单元 | 时间 | 任务 | 产出 |
|---|---:|---|---|
| 2.1 启动、命令与配置 | 1.0h | 从 `main.go` 进入一个子命令，追踪配置默认值、文件和 CLI 覆盖顺序 | 一页调用说明；配置优先级测试 |
| 2.2 10 小时检查 | 1.0h | 不看笔记解释一个命令；现场修改一个小行为并补 table-driven test | 达到下文 10 小时标准，或列出具体缺口后回到对应单元 |
| 2.3 HTTP/GraphQL 客户端 | 1.5h | 请求构造、认证、超时、响应解码和外部错误分类 | `httptest.Server` 覆盖成功、取消、超时和异常响应；凭证不进入日志 |
| 2.4 缓存与持久化 | 1.5h | 比较 JSON 与 SQLite 实现的初始化、并发、损坏数据和错误行为 | `QuestionsCache` 接口级测试；说明两种实现的适用条件 |
| 2.5 模板、文件与本地进程 | 1.5h | 追踪代码生成、本地测试、编辑器调用；处理路径、覆盖、退出码和取消 | 一个不访问 LeetCode 的本地端到端测试 |
| 2.6 选择真实修改 | 1.0h | 在固定版本上复现实际问题；检查开放 issue、已有 PR 和维护者讨论 | 最小复现、预期行为、影响文件、风险和验收测试 |
| 2.7 测试驱动修改 | 3.0h | 先写失败测试，再做最小完整实现和必要重构 | 可评审 patch；目标测试和已有相关测试通过 |
| 2.8 发布检查与 20 小时评审 | 1.5h | 运行格式、静态检查、测试和构建；限时讲解改动 | 本地二进制、检查记录和五分钟项目说明；未掌握项有具体练习 |

优先做与 leetgo 本身有关的真实需求，不增加“本地运行记录与复习服务”。开放 issue 只是候选，开始时必须
重新确认它在固定版本上仍存在且范围适合。

## Phase 3 · Dagu 的实际使用与本地执行（9 小时，累计 29 小时）

Dagu 从本阶段开始成为真实使用的工具和主要后端/系统案例，固定源码路径见
[Dagu 案例](cases/dagu.md)。第一项工作流固定为手动触发的
`go-project-check`：对当前 Go 仓库运行指定包的版本核对、测试、竞态检测、静态检查和构建，并保留日志与
测试产物。没有实际需要前不添加定时执行、通知、远程 SSH 或 AI 自动操作。

| 单元 | 时间 | 核心任务 | 必须取得的结果 |
|---|---:|---|---|
| 3.1 建立真实工作流 | 1.5h | 在隔离的 `DAGU_HOME` 中运行 `go-project-check`；先手动触发失败，再修正 | 能在 CLI 和 Web UI 中看到运行状态、日志、退出码和产物；工作流已用于一个真实仓库 |
| 3.2 CLI 与常驻进程 | 1.0h | 追踪 `start`、`start-all` 及配置装配；观察启动和优雅停止 | 说明 CLI、HTTP server、scheduler、coordinator 分别何时创建和停止 |
| 3.3 YAML、验证与内部表示 | 1.5h | 从 YAML 进入 loader、validator 和内部 DAG 表示；构造循环依赖、未知字段和非法参数 | 三类无效输入在执行前失败，错误能定位字段和原因 |
| 3.4 本地执行路径 | 2.0h | 追踪 Engine、runtime plan、executor 和 command action | 从一个 step 说明输入、工作目录、环境、进程、状态和输出如何变化 |
| 3.5 状态、日志、产物与进程生命周期 | 1.5h | 观察成功、非零退出、超时、取消和重试 | 每种最终状态可判定；子进程不会在取消后继续遗留 |
| 3.6 本地集成实验 | 1.5h | 使用临时目录和可控子进程测试一次完整运行；检查敏感值遮盖和清理 | 测试可离线重复；能解释哪部分是 Dagu 的领域取舍而非 Go 通用规则 |

主要资料：[Dagu v2.13.0 源码](https://github.com/dagucloud/dagu/tree/v2.13.0)、
[架构说明](https://docs.dagu.sh/overview/architecture)和
[YAML 规范](https://docs.dagu.sh/writing-workflows/yaml-specification)。

## Phase 4 · 后端能力实验（6 小时，累计 35 小时）

本阶段不创建第三个长期产品，固定行为见[后端能力实验](cases/backend-capability-lab.md)。实验对象是一个可删除的
“任务接纳切片”：`POST /jobs` 接纳任务、
`GET /jobs/{id}` 查询状态、`POST /jobs/{id}/cancel` 请求取消；PostgreSQL 18 保存任务，有限 worker 领取任务。
它用于证明能从空目录设计和实现后端行为，不宣称存在真实用户需求。

| 单元 | 时间 | 核心任务 | 必须验证的行为 |
|---|---:|---|---|
| 4.1 HTTP 与 API 边界 | 1.5h | 先用 `net/http` 实现显式 `http.Server`、路由、中间件、请求体上限、严格 JSON 和统一错误响应；再与 Dagu 的 Chi/OpenAPI 层比较 | 非法输入不进入存储；请求取消传到实际工作；关闭中的请求行为可测试 |
| 4.2 PostgreSQL 与事务 | 1.5h | 先运行 Dagu 的 `postgres.query`，再追踪其 `database/sql` + pgx 实现；为实验编写迁移、约束、幂等键和事务领取 | 真实 PostgreSQL 18 拒绝无效状态；并发领取不会重复处理；`Rows`、`Tx` 和连接正确结束 |
| 4.3 有限 executor | 1.0h | 从零实现固定 worker 数、有界等待队列、取消和关闭规则 | 队列满显式失败；停止后不接收新任务；没有 goroutine 泄漏或数据竞争 |
| 4.4 Gin 对照 | 1.0h | 只替换 HTTP adapter，复用同一应用逻辑和测试，比较绑定、中间件、错误处理和依赖成本 | 能解释 Gin 减少了什么代码、隐藏了什么行为；没有复制业务逻辑 |
| 4.5 集成与 35 小时检查 | 1.0h | 使用 `httptest`、真实 PostgreSQL、`-race` 和优雅退出测试；现场解释一个失败过程 | 三个 API、一次真实事务、有限后台任务和关闭测试全部通过 |

事务领取可以使用 `SELECT … FOR UPDATE SKIP LOCKED` 或原子 `UPDATE … RETURNING`，但必须用并发测试说明
选择依据，并讨论饥饿、公平性和重试条件，不能只因为写法常见就采用。

主要资料：[Go 数据库指南](https://go.dev/doc/database/)、
[PostgreSQL 18 文档](https://www.postgresql.org/docs/18/)、[net/http](https://pkg.go.dev/net/http@go1.26.5) 和
[Gin v1.12.0](https://github.com/gin-gonic/gin/tree/v1.12.0)。

## Phase 5 · Dagu 的可靠性、gRPC 与真实修改（10 小时，累计 45 小时）

本阶段继续使用 [Dagu 案例](cases/dagu.md) 的 D4–D6 路径，不扩大到前端或完整仓库。

| 单元 | 时间 | 核心任务 | 产出 |
|---|---:|---|---|
| 5.1 队列与文件持久化 | 1.5h | 追踪 scheduler、queue store、索引和分布式 dispatch；检查写入原子性、损坏数据和重启恢复 | 一次排队到执行的状态说明；损坏或重复输入的失败测试 |
| 5.2 有限并发、取消与恢复 | 1.5h | 分析队列并发上限、背压、重试、租约和关闭顺序；适合时用 `testing/synctest` | 饱和、取消和异常停止测试通过；运行 `-race`；能指出谁启动、取消并等待 goroutine |
| 5.3 gRPC 基础与接口规则 | 1.0h | 阅读 `.proto` 与生成代码；区分 unary、client streaming、deadline、status code 和可安全重试条件 | 能解释 `Poll`、`Dispatch`、`Heartbeat`、`ReportStatus`、`StreamLogs` 的行为和失败语义 |
| 5.4 coordinator/worker 实验 | 2.0h | 本地启动 coordinator 与 worker，追踪 polling、claim/ack、心跳、状态和日志上报；中断网络或 worker | 能判断任务是否执行过、状态是否持久化、日志是否可能丢失，以及恢复发生在哪里 |
| 5.5 日志、指标与诊断 | 1.0h | 使用结构化日志、低基数指标、`pprof` 或 trace 定位一次慢或卡住的运行 | 诊断记录包含版本、输入、时间线和证据；敏感值不输出 |
| 5.6 选择真实修改 | 1.0h | 优先处理实际使用遇到的问题；否则重查开放 issue 和 PR，在 v2.13.0 上复现 | 问题可在 30 分钟内复现，修改原则上不超过三个包，不要求 UI 或新增依赖 |
| 5.7 实现与评审 | 2.0h | 先写失败测试，完成最小修改，运行目标包格式、测试、竞态检测和静态检查 | 一份本地可评审 Dagu patch；若问题超过范围，保留复现和测试并继续到 50 小时以后，不牺牲质量 |

主要资料：[Dagu 分布式执行](https://docs.dagu.sh/server-admin/distributed/workers/shared-nothing)、
[gRPC Go 基础](https://grpc.io/docs/languages/go/basics/)、[deadline](https://grpc.io/docs/guides/deadlines/) 和
[status code](https://grpc.io/docs/guides/status-codes/)。

## Phase 6 · Nuclei 高并发网络程序比较（3 小时，累计 48 小时）

Nuclei 只访问本地课程服务或明确授权目标，并遵守 [Nuclei 案例](cases/nuclei.md) 的固定版本和安全限制。
这里不学习漏洞利用，也不试图读完整个仓库。

| 单元 | 时间 | 代码主题 | 比较结果 |
|---|---:|---|---|
| 6.1 Runner 与 Engine | 1.0h | 从 CLI options 进入 Runner、Engine 和两种执行策略 | 用小输入说明 template-spray 与 host-spray 如何改变任务数量、局部性和内存 |
| 6.2 WorkPool 与限速 | 1.0h | 追踪 `WorkPool`、并发参数和全局 rate limiter | 实验证明并发上限与每秒请求上限不是同一限制；与 Dagu 队列并发比较 |
| 6.3 HTTP client pool | 1.0h | 使用本地 `httptest.Server` 检查超时、连接复用、响应体关闭、取消和关闭过程 | 一份 Nuclei 与 Dagu 的资源生命周期比较；目标测试或 benchmark 可重复 |

主要资料：[Nuclei v3.11.1 源码](https://github.com/projectdiscovery/nuclei/tree/v3.11.1)和
[官方并发/限速说明](https://docs.projectdiscovery.io/opensource/nuclei/running)。

## Phase 7 · 50 小时能力检查（2 小时，累计 50 小时）

| 单元 | 时间 | 任务 | 通过标准 |
|---|---:|---|---|
| 7.1 项目讲解与检索练习 | 1.0h | 分别用五分钟讲 leetgo 修改、Dagu 调用路径和 Nuclei 实验；随后回答语言、并发、HTTP、数据库、测试问题 | 回答包含具体代码、失败例子或一手资料依据，不靠背目录和口号 |
| 7.2 限时诊断与最终评审 | 1.0h | 在陌生的小包中复现缺陷、补测试并做最小修复；按下表核对所有证据 | 代码可构建，失败显式，无明显资源泄漏或竞态；未达到项写成下一次真实任务 |

## 里程碑只按表现判定

| 累计投入 | 里程碑 | 必须保留的证据 | 未通过时怎么做 |
|---:|---|---|---|
| 10h | 基础可用 | 一次无笔记调用讲解、一个现场测试修改、工具链检查记录 | 回到对应语言单元做更小的反例，不提前堆框架 |
| 20h | 熟悉 Go | leetgo 最小复现、失败测试、patch、检查结果和项目讲解 | 缩小真实问题范围，补足错误或测试能力 |
| 35h | 可独立构建后端 | 实际 Dagu 工作流；任务接纳切片；PostgreSQL 并发测试；HTTP、关闭和 `-race` 结果 | 不用 mock 代替数据库或删除失败测试；允许继续超过 35 小时 |
| 50h | 本课程范围内的精通 | Dagu 队列/gRPC 诊断、真实修改、Nuclei 比较、限时修复和三份项目说明 | 按缺失证据继续真实任务；累计 50 小时不自动判定精通 |

长期精通仍是必须完成的目标。50 小时之后应至少继续完成：三个不同类型的真实 Go 修改；一个自己长期使用的
Go 后端服务；一次部署、升级或故障恢复；多轮来自维护者、同事或社区的代码评审。达到这些结果后再按实际岗位
需要引入 ORM、Redis、Kafka 或 Kubernetes。

## 调整规则

- 只有 10 小时：完成 Phase 0–1 和 Phase 2 前两项，保留基础可用证据，不声称熟悉或精通。
- 只有 20 小时：完成 leetgo 修改；Dagu 留到下一阶段。
- 只有 35 小时：必须完成真实 PostgreSQL、有限后台任务和关闭测试；Nuclei 不进入核心。
- 计划 50 小时：完成全部阶段。某项真实修改超过估时可以继续到 50 小时以后，不用删减测试或错误处理赶进度。
- 间隔较长：先做不看笔记的回忆和一个旧测试，再继续新材料；不要用重读全文代替检索练习。
- 案例 issue 或外部 API 改变：固定源码仍保持不变；记录查询日期，在固定版本上复现后再决定是否调整任务。
- 冷缓存准备过慢或磁盘不足：停止构建并先处理环境；不要把等待下载算作学习，也不要关闭 checksum 验证绕过问题。
