# Dagu 与 Nuclei 固定版本冷缓存编译

> 执行日期：2026-08-12。该记录证明课程指定包可以在记录的环境中准备完成，不是学习记录，也不证明业务测试
> 或运行时行为已经通过。

## 共同条件

| 项目 | 值 |
| --- | --- |
| 平台 | `darwin/arm64` |
| Go | `go1.26.5`，由 `mise exec go@1.26.5` 显式选择 |
| 工具链切换 | `GOTOOLCHAIN=local` |
| 模块代理 | `GOPROXY=https://proxy.golang.org,direct` |
| 校验服务 | `GOSUMDB=sum.golang.org` |
| 依赖模式 | `-mod=readonly`，没有修改案例的 `go.mod` 或 `go.sum` |
| 并发 | `-p=1`，降低首次编译的磁盘与内存峰值 |
| 缓存 | 每个案例使用新建的空 `GOMODCACHE` 和空 `GOCACHE`；完成后删除 |

两个案例都先核对 `git rev-parse HEAD`，且开始时可用空间高于案例文档的最低值。完整下载日志是可重建的机器
状态，没有写入 Git。

## Dagu v2.13.0

- Commit：`13745bb8811de8e1cdbe116561e4a4e491edbed5`
- 命令：

```sh
case_cache=$(mktemp -d "${TMPDIR:-/tmp}/dagu-cold.XXXXXX")
/usr/bin/time -p mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOMODCACHE="$case_cache/mod" \
  GOCACHE="$case_cache/build" \
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

- 结果：退出状态 `0`；命令列出的包及 `sql/...` 展开的 PostgreSQL、SQLite 包均编译成功。
- `/usr/bin/time -p`：`real 924.22`、`user 394.29`、`sys 72.37` 秒。

## Nuclei v3.11.1

- Commit：`a8c88feb4a1c8e961b7902534ce3af97e9d524a4`
- 命令：

```sh
case_cache=$(mktemp -d "${TMPDIR:-/tmp}/nuclei-cold.XXXXXX")
/usr/bin/time -p mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOMODCACHE="$case_cache/mod" \
  GOCACHE="$case_cache/build" \
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

- 结果：退出状态 `0`；八个目标包均编译成功，其中 `pkg/input/provider` 没有测试文件。
- `/usr/bin/time -p`：`real 698.46`、`user 374.64`、`sys 64.26` 秒。

## 可以和不可以得出的结论

`-run '^$'` 使测试函数不运行，但 `go test` 仍编译目标包与测试文件。因此可以确认固定 commit、依赖图、Go
1.26.5 和列出的源码范围在该平台兼容；不能据此确认队列恢复、HTTP、gRPC、SQL、限速、取消或资源释放行为。
进入对应课程单元后仍须运行案例文件列出的目标测试，并针对观察问题增加最小输入。

首次编译耗时主要是依赖下载和编译，不能作为服务性能数据。若升级 tag、commit、Go 版本、目标包或平台，该记录
失效，必须重新执行并保存新结果。
