# Nuclei：高并发网络程序比较案例

返回[案例索引](../CASES.md)。固定版本为 `v3.11.1`，commit
`a8c88feb4a1c8e961b7902534ce3af97e9d524a4`。本案例为选修，按需比较并发、限速和 HTTP 资源管理，不学习漏洞
利用，也不通读仓库。

## 开始前验证

至少保留 8 GiB 可用空间，然后在 Nuclei 仓库根目录运行：

```sh
git rev-parse HEAD
mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOPROXY=https://proxy.golang.org,direct \
  GOSUMDB=sum.golang.org \
  go test -mod=readonly -p=1 -run '^$' \
  ./internal/runner \
  ./pkg/core \
  ./pkg/input/provider \
  ./pkg/catalog/loader \
  ./pkg/templates \
  ./pkg/protocols/http \
  ./pkg/protocols/http/httpclientpool \
  ./pkg/output
```

`HEAD` 必须等于固定 commit。`-run '^$'` 只验证包和测试文件能够编译；旧版本 v3.8.0 的结果不能用于本版本。

2026-08-12 的空缓存基准已经通过，见[固定案例冷缓存编译记录](../evidence/0001-pinned-case-cold-builds.md)。开始
选择本案例时仍运行上述命令，确认当前 clone 和依赖没有偏离记录。

## N1：Runner 到 Engine

1. `cmd/nuclei/main.go`
2. `internal/runner/options.go`
3. `internal/runner/runner.go`
4. `pkg/core/engine.go`
5. `pkg/core/execute_options.go`
6. `pkg/core/executors.go`

只使用一个本地 HTTP 输入和一个最小模板。需要用小规模测量说明 template-spray 与 host-spray 如何展开任务，
以及配置中的 concurrency、bulk size 与 rate limit 分别限制什么。

## N2：WorkPool 与 HTTP client pool

1. `pkg/core/workpool.go`
2. `pkg/protocols/common/contextargs/contextargs.go`
3. `pkg/protocols/http/request.go`
4. `pkg/protocols/http/build_request.go`
5. `pkg/protocols/http/httpclientpool/clientpool.go`
6. `pkg/output/output.go`

优先测试：

- `pkg/core/engine_test.go`
- `pkg/core/executors_test.go`
- `pkg/core/workflow_execute_test.go`
- `pkg/protocols/http/httpclientpool/clientpool_test.go`
- `pkg/protocols/http/httpclientpool/perhost_ratelimit_pool_close_test.go`

需要证明：任务并行度、请求速率、连接数和内存是不同限制；取消时哪些 goroutine 和响应体必须结束；client pool
何时共享、何时关闭。最终产出是与 Dagu 队列并发和资源生命周期的具体比较，不是框架功能列表。

## 安全限制

- 只访问 `httptest.Server`、课程本地服务或用户明确授权的目标。
- 使用课程提供的最小模板和输入，运行时传入 `-disable-update-check`，不自动取得浮动模板集合。
- 不使用公网模板更新、AI 模板生成、云端结果、Headless、JavaScript、code template 或 fuzzing。
- 目标是理解并发和网络资源管理，不是发现或利用漏洞。
