# Dagu：主要后端与系统案例

返回[案例索引](../CASES.md)。固定版本为 `v2.13.0`，commit
`13745bb8811de8e1cdbe116561e4a4e491edbed5`。Dagu 先作为学习者实际使用的个人自动化工具，再用于观察后端、
调度、持久化和分布式 worker。约 1,600 个 Go 文件不适合通读，只追踪下列六条路径。

## 开始前验证

至少保留 12 GiB 可用空间，然后在 Dagu 仓库根目录运行：

```sh
git rev-parse HEAD
mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOPROXY=https://proxy.golang.org,direct \
  GOSUMDB=sum.golang.org \
  go test -mod=readonly -p=1 -run '^$' \
  ./internal/spec \
  ./internal/engine \
  ./internal/queue \
  ./internal/persis/store \
  ./internal/service/frontend/api/v1 \
  ./internal/service/scheduler \
  ./internal/service/coordinator \
  ./internal/service/worker \
  ./internal/runtime/builtin/sql/...
```

`HEAD` 必须等于固定 commit。`-run '^$'` 不运行业务测试，只验证包、测试文件和默认 vet 分析能够编译；每个
课程单元仍须运行目标测试。准备命令退出为零之前，不能把 Dagu 课程包记为已验证。

2026-08-12 的空缓存基准已经通过，见[固定案例冷缓存编译记录](../evidence/0001-pinned-case-cold-builds.md)。开始
Phase 3 时仍运行上述命令，确认当前 clone 和依赖没有偏离记录。

## D1：CLI、配置和进程装配

1. `cmd/main.go`
2. `internal/cmd/context.go`
3. `internal/cmd/start.go`
4. `internal/cmd/startall.go`
5. `internal/cmd/process/server.go`
6. `internal/cmd/process/scheduler.go`
7. `internal/cmd/process/coordinator.go`

需要证明：`start` 和 `start-all` 分别创建什么；配置、环境和 flags 在哪里组合；服务启动失败如何回到 CLI；
正常关闭由谁发起并等待。

## D2：YAML 到本地执行

1. `internal/spec/loader.go`
2. `internal/spec/validator.go`
3. `internal/engine/engine.go`
4. `internal/engine/run.go`
5. `internal/runtime/build_plan.go`
6. `internal/runtime/runner.go`
7. `internal/runtime/executor/`
8. `internal/runtime/builtin/command/`

优先测试：

- `internal/spec/loader_test.go`
- `internal/engine/run_test.go`
- `internal/runtime/executor/executor_test.go`

需要证明：外部 YAML 在哪里解码和验证；内部 DAG 和执行 plan 何时形成；step 如何启动进程；状态、输出、重试、
timeout 与取消分别由谁负责。

## D3：HTTP API 和文件持久化

1. `internal/service/frontend/server.go`
2. `internal/service/frontend/api/v1/api.go`
3. `internal/service/frontend/api/v1/dagruns.go`
4. `internal/service/frontend/api/v1/errors.go`
5. `internal/queue/`
6. `internal/persis/store/queue.go`
7. `internal/persis/store/queue_item.go`
8. `internal/persis/store/queue_index.go`

Dagu 在该版本使用 Chi 与生成的 OpenAPI server，不使用 Gin。优先运行
`internal/service/frontend/api/v1/dagruns_test.go` 和 `internal/persis/store/queue_test.go`，证明 HTTP 输入的结构与
业务验证、错误映射，以及文件写入、索引、并发和损坏数据行为。

## D4：scheduler、队列和恢复

1. `internal/service/scheduler/scheduler.go`
2. `internal/service/scheduler/enqueue.go`
3. `internal/service/scheduler/queue_dispatcher.go`
4. `internal/service/scheduler/queue_processor.go`
5. `internal/queue/enqueue_retry.go`
6. `internal/persis/store/distributed_admission.go`
7. `internal/persis/store/distributed_dispatch.go`
8. `internal/persis/store/distributed_lease.go`
9. `internal/persis/store/distributed_corruption.go`

优先测试：

- `internal/service/scheduler/queue_processor_test.go`
- `internal/persis/store/distributed_admission_test.go`
- `internal/persis/store/distributed_test.go`

需要证明：任务何时持久化、排队、取得执行资格和完成；并发上限如何生效；重复 dispatch、租约过期、进程崩溃和
文件损坏后能恢复到什么状态。

## D5：coordinator/worker 的 gRPC

1. `proto/coordinator/v1/coordinator.proto`
2. `internal/service/coordinator/service.go`
3. `internal/service/worker/worker.go`
4. `internal/service/worker/poller.go`
5. `internal/service/worker/remote_handler.go`
6. `internal/service/worker/coordreport/status_pusher.go`
7. `internal/service/worker/coordreport/log_streamer.go`

优先测试：

- `internal/service/worker/poller_test.go`
- `internal/service/worker/coordreport/status_pusher_test.go`
- `internal/service/worker/coordreport/log_streamer_test.go`

只深入 `Poll`、`Dispatch`、`Heartbeat`、`AckTaskClaim`、`ReportStatus` 和 `StreamLogs`。需要回答：deadline 由谁设置；
RPC 超时能否证明任务没执行；哪些调用可以重试；worker 消失后 coordinator 如何判断；状态与日志是否具有相同
可靠性。

## D6：PostgreSQL action

1. `internal/runtime/builtin/sql/sql.go`
2. `internal/runtime/builtin/sql/driver.go`
3. `internal/runtime/builtin/sql/drivers/postgres/postgres.go`
4. `internal/runtime/builtin/sql/input.go`
5. `internal/runtime/builtin/sql/import.go`

优先运行 `internal/runtime/builtin/sql/sql_test.go`、`race_test.go` 和 PostgreSQL driver 测试。需要证明
`database/sql` 与 pgx 如何连接；参数如何传递；timeout、事务和 isolation level 如何生效；连接池由谁拥有和
关闭；流式输出与全部缓冲的内存成本有何区别。

## 实际使用任务

第一项工作流固定为手动触发的 `go-project-check`：输入明确的本地仓库路径和目标包，输出工具链版本、测试、
竞态检测、静态检查和构建结果。它使用隔离的 `DAGU_HOME`，不把凭证、私钥或完整环境变量写入 YAML、日志或产物。

只有真实需要出现后才增加 schedule、SSH、Telegram 通知、Git 操作、Codex harness 或远程 worker。新增功能前先
定义它处理什么输入、如何失败、如何清理以及凭证保存位置。

## 真实修改选择

第一优先级是实际使用中遇到的问题。开放 issue 只用来理解问题空间，候选任务必须同时满足：

- 能在 v2.13.0 上于 30 分钟内建立最小失败；
- 原则上不超过三个包，不要求前端修改或大型新依赖；
- 能用目标包测试验证；
- 没有活跃 PR，且预期行为足够明确。

2026-08-12 可重新调查但未预选为作业的 issue 包括
[#2145](https://github.com/dagucloud/dagu/issues/2145)、
[#2047](https://github.com/dagucloud/dagu/issues/2047) 和
[#2037](https://github.com/dagucloud/dagu/issues/2037)。#2047 的报告基于旧版本，#2037 当时已有 assignee；
开始任务当天必须重新核查状态和讨论，不能直接照 issue 描述实现。
