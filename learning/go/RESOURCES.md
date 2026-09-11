# Go 学习资源

按当前问题查阅，不要求通读资源表。Gin、gRPC、Nuclei 和深入性能诊断为选修；已有案例和资料不决定课程顺序。

> 核实日期：2026-08-12。课程固定使用 Go 1.26.5；案例和第三方依赖使用 [CASES.md](CASES.md) 中的
> tag 与 commit。这里保留少量高可信入口，不用链接数量代替资料质量。

## Knowledge

### 语言、工具链与模块

- [Go 语言规范](https://go.dev/ref/spec)
  类型、赋值、方法集、接口、泛型和控制语句等语言事实的首要来源。用在解释“语言保证什么”，不用于推导
  某个项目的工程选择。
- [Go 1.26 Release Notes](https://go.dev/doc/go1.26)
  Go 1.26 的语言、工具链、运行时和标准库变化。用在区分课程版本的新行为与长期稳定规则。
- [Go Release History](https://go.dev/doc/devel/release)
  核验 Go 1.26.5 的发布日期及安全、编译器和运行时修复。课程升级补丁版本前先查这里。
- [Go toolchains](https://go.dev/doc/toolchain)
  `GOTOOLCHAIN`、`go` 与 `toolchain` 指令的精确定义。用在当前机器的启动工具链与课程工具链不一致时。
- [Go Modules Reference](https://go.dev/ref/mod)
  模块版本选择、`go.mod`、`go.sum`、workspace、vendor 和依赖认证。用在依赖升级、固定和 checksum 问题。
- [Module authentication](https://go.dev/ref/mod#authenticating)
  `go.sum` 与 checksum database 如何验证下载内容。出现 checksum mismatch 时必须回到这里，不关闭验证绕过。
- [Command Documentation](https://go.dev/doc/cmd)
  `go`、`fmt`、`vet`、`cover`、`trace` 和 `pprof` 的官方入口。用在区分构建、测试、分析和格式化职责。
- [Standard library for Go 1.26.5](https://pkg.go.dev/std@go1.26.5)
  固定版本标准库索引。课程引用 API 和行为时优先进入对应 1.26.5 页面。

### 惯用写法、测试与诊断

- [Effective Go](https://go.dev/doc/effective_go)
  理解基础惯用写法。它的首页明确说明内容没有覆盖所有现代生态变化；涉及泛型、模块和新 API 时必须再查
  当前规范、文档和源码。
- [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments)
  常见代码评审建议。用在评审练习，但每项建议仍需结合调用方、失败行为和项目限制判断。
- [testing — Go 1.26.5](https://pkg.go.dev/testing@go1.26.5)
  单元测试、子测试、benchmark、fuzz 和测试产物 API。用在所有课程测试任务。
- [testing/synctest — Go 1.26.5](https://pkg.go.dev/testing/synctest@go1.26.5)
  在隔离环境中测试部分并发和时间行为。适用于没有真实网络或外部进程的自包含测试，不强行替代集成测试。
- [Go Fuzzing](https://go.dev/doc/security/fuzz/)
  官方 fuzz 教程和语料管理。用在解析器、字符串与不可信输入边界，不用 fuzz 代替明确的行为测试。
- [Data Race Detector](https://go.dev/doc/articles/race_detector)
  `go test -race` 的用法、限制和典型竞态。所有并发练习和相关 patch 都要使用。
- [Go Memory Model](https://go.dev/ref/mem)
  happens-before、channel、锁和原子操作正确性的正式依据。用在并发可见性问题；若代码只能靠复杂内存模型
  推理才能理解，应先简化设计。
- [Go Concurrency Patterns: Context](https://go.dev/blog/context) 与
  [Pipelines and cancellation](https://go.dev/blog/pipelines)
  请求范围取消、deadline 和 goroutine 退出的官方模式。用在 worker、Dagu 和 HTTP/RPC 生命周期课程。
- [Diagnostics](https://go.dev/doc/diagnostics)
  profiling、tracing、metrics 与调试工具概览。只有存在可复现的慢、卡住或资源问题时进入。
- [Go Vulnerability Management](https://go.dev/doc/security/vuln/)
  `govulncheck` 和 Go 漏洞数据库。用在发布检查和依赖风险评估。

### HTTP、PostgreSQL 与 Gin

- [`net/http` — Go 1.26.5](https://pkg.go.dev/net/http@go1.26.5)
  `Handler`、`Server`、`Transport`、timeout、连接复用和 `Shutdown` 的主要资料。框架课之前先查这里。
- [`context` — Go 1.26.5](https://pkg.go.dev/context@go1.26.5)
  取消、deadline 和 request-scoped value 规则。用在 HTTP、数据库、子进程与 gRPC 的调用边界。
- [Accessing relational databases](https://go.dev/doc/database/)
  `database/sql` 的连接、查询、事务和取消教程。用在 Dagu SQL 路径与后端能力实验。
- [Executing transactions](https://go.dev/doc/database/execute-transactions)
  `sql.Tx`、commit/rollback 和事务期间不能混用 `sql.DB` 的原因。用在并发领取任务和幂等写入。
- [`database/sql` — Go 1.26.5](https://pkg.go.dev/database/sql@go1.26.5)
  `DB`、`Rows`、`Tx`、连接池和资源生命周期的 API 依据。
- [PostgreSQL 18 Documentation](https://www.postgresql.org/docs/18/)
  课程固定主版本的约束、事务隔离、锁、索引和 SQL 行为来源。
- [PostgreSQL 18 `SELECT`](https://www.postgresql.org/docs/18/sql-select.html)
  `FOR UPDATE`、`NOWAIT` 和 `SKIP LOCKED` 的准确语义。官方明确指出 `SKIP LOCKED` 适合 queue-like table，
  但会给出不一致视图；后端实验如果采用该机制，需要讨论适用边界，不预先固定事务领取方案。
- [pgx v5.9.2](https://github.com/jackc/pgx/tree/v5.9.2)
  固定 PostgreSQL 驱动，commit `0aeabbcf11d859229c1f0b20e710d3596c76bf27`，与 Dagu v2.13.0 使用版本一致。
  课程先通过 `database/sql` 与 `pgx/v5/stdlib` 学习通用接口，再按真实需求使用 pgx 原生 API。
- [Gin v1.12.0](https://github.com/gin-gonic/gin/tree/v1.12.0)
  固定 HTTP 框架源码，commit `73726dc606796a025971fe451f0aa6f1b9b847f6`。只作为 adapter 对照，不用它
  绕过 `http.Server`、输入验证、错误处理或关闭行为。
- [Gin binding](https://gin-gonic.com/en/docs/binding/) 与
  [Gin testing](https://gin-gonic.com/en/docs/testing/)
  比较 `Bind`/`ShouldBind` 的错误控制及使用 `httptest` 测试 handler。课程要求复用标准库版本的行为测试。

### Dagu：主要后端与系统案例

版本表见 [CASES.md](CASES.md)，详细代码路径和任务限制见 [Dagu 案例](cases/dagu.md)。

- [Dagu v2.13.0 source](https://github.com/dagucloud/dagu/tree/v2.13.0) 与
  [v2.13.0 release](https://github.com/dagucloud/dagu/releases/tag/v2.13.0)
  固定 commit `13745bb8811de8e1cdbe116561e4a4e491edbed5`。源码用于证明实际实现，发布说明用于了解该
  快照的改动背景；不跟随 `main`。
- [Dagu architecture](https://docs.dagu.sh/overview/architecture)
  standalone 与 coordinator/worker 模式的官方说明。用在确定组件职责，再回到固定源码核实实现。
- [Dagu YAML specification](https://docs.dagu.sh/writing-workflows/yaml-specification)
  工作流输入、step、参数、并发与输出规则。用在建立 `go-project-check` 和无效输入实验。
- [Dagu queue configuration](https://docs.dagu.sh/server-admin/queues) 与
  [queue assignment](https://docs.dagu.sh/writing-workflows/queues)
  named queue、`max_concurrency`、enqueue 和默认行为。用在队列上限、等待原因与恢复实验。
- [Dagu REST API](https://docs.dagu.sh/web-ui/api)
  OpenAPI、API 路径和认证方式的官方参考。用在追踪固定源码中的 Chi/OpenAPI HTTP 层。
- [Dagu ETL & SQL](https://docs.dagu.sh/step-types/sql/)
  `postgres.query`、参数、事务、隔离级别、advisory lock 和 streaming。用在实际 PostgreSQL workflow 与源码
  对照，不能替代 PostgreSQL 官方语义。
- [Dagu shared-nothing workers](https://docs.dagu.sh/server-admin/distributed/workers/shared-nothing)
  `ReportStatus`、`StreamLogs` 和无共享文件系统 worker 的官方行为。用在本地断连实验和可靠性讨论。
- [Dagu Web UI](https://docs.dagu.sh/overview/web-ui)
  运行、日志、历史和系统状态的操作入口。课程只使用 UI 观察行为，不学习前端实现。
- [Dagu contributing guide](https://docs.dagu.sh/overview/contributing)
  查找 issue、测试和贡献流程。课程只准备本地 patch；是否联系维护者或提交另行决定。

### gRPC

- [gRPC Go basics](https://grpc.io/docs/languages/go/basics/)
  `.proto`、生成 client/server、unary 与 streaming RPC 的官方入门。用在阅读 Dagu coordinator service。
- [gRPC generated-code reference for Go](https://grpc.io/docs/languages/go/generated-code/)
  `.proto` 如何映射到 Go 接口和 stream 类型。用在区分生成代码与手写 handler。
- [gRPC deadlines](https://grpc.io/docs/guides/deadlines/)
  默认不会自动设置 deadline；客户端和服务端各自的取消责任。用在 worker/coordinator 中断实验。
- [gRPC status codes](https://grpc.io/docs/guides/status-codes/)
  `CANCELLED`、`DEADLINE_EXCEEDED`、`FAILED_PRECONDITION`、`ABORTED`、`UNAVAILABLE` 等语义。用在错误映射与
  判断重试层级。
- [gRPC retry](https://grpc.io/docs/guides/retry/)
  retry policy、backoff、retryable status 和透明重试。用在解释为什么非幂等操作不能看到 `UNAVAILABLE`
  就机械重试。

### leetgo 与 Nuclei

- [leetgo v1.4.17](https://github.com/j178/leetgo/tree/v1.4.17) 与
  [release](https://github.com/j178/leetgo/releases/tag/v1.4.17)
  固定 commit `393d4219207884c675fc0e3557ff64f86f5c61de`。用于语言、CLI、HTTP、文件和子进程实践。
- [leetgo open issues](https://github.com/j178/leetgo/issues?q=is%3Aissue%20is%3Aopen)
  真实修改候选。状态和讨论会变化，开始当天必须检查已有 PR 并在固定版本复现。
- [Nuclei v3.11.1](https://github.com/projectdiscovery/nuclei/tree/v3.11.1) 与
  [release](https://github.com/projectdiscovery/nuclei/releases/tag/v3.11.1)
  固定 commit `a8c88feb4a1c8e961b7902534ce3af97e9d524a4`。仅用于选修并发与 HTTP client pool 比较。
- [Running Nuclei](https://docs.projectdiscovery.io/opensource/nuclei/running)
  官方 CLI、执行策略、concurrency、bulk size 与 rate limit 说明。课程只针对本地夹具并关闭更新检查。
- [Mass scanning with Nuclei](https://docs.projectdiscovery.io/opensource/nuclei/mass-scanning-cli)
  解释不同并发限制和 rate limiter 所在位置对内存的影响。用来提出可测量假设，不作为公网扫描指南。

## Wisdom (Communities)

- [Go Forum](https://forum.golangbridge.org/) 与 [Gophers Slack](https://invite.slack.golangbridge.org/)
  用于让其他 Go 实践者评审接口、并发和职业问题。社区答案是经验信号，语言事实仍回到官方资料核验。
- [Go GitHub Discussions](https://github.com/golang/go/discussions)
  用于 Go 项目的一般问答；缺陷和提案应使用项目规定的 issue 流程，不把 discussion 投票当成规范。
- [Dagu GitHub issues](https://github.com/dagucloud/dagu/issues) 与
  [Dagu Discord](https://discord.gg/gpahPUjGRk)
  用于验证真实使用问题、了解维护背景并取得 patch 反馈。先遵循贡献指南，未获用户授权不代表用户对外发言。
- [leetgo issues](https://github.com/j178/leetgo/issues) 与
  [Nuclei discussions](https://github.com/projectdiscovery/nuclei/discussions)
  用于理解案例的实际限制和维护者取舍。评论代表参与者观点，不自动成为通用 Go 规则。

## Gaps

- 当前没有外部维护者对学习者 patch 的反馈证据。完成本地可评审修改后，再由学习者决定是否向项目社区请求评审。
- 当前没有部署和故障恢复记录。核心课程加入本机 Linux 容器部署；公网部署、升级、备份和恢复作为后续实践。
- ORM、Redis、Kafka 和 Kubernetes 不进入第一轮核心。是否加入应由目标岗位和真实服务需求决定，而不是为
  技术名词覆盖率添加。
