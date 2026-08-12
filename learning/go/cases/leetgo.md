# leetgo：语言与 CLI 案例

返回[案例索引](../CASES.md)。固定版本为 `v1.4.17`，commit
`393d4219207884c675fc0e3557ff64f86f5c61de`。本案例负责 Go 语言、CLI、HTTP、文件、缓存、子进程和第一项
真实项目修改，不增加 leetgo 运行记录或复习服务。

## 开始前验证

```sh
git rev-parse HEAD
mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOPROXY=https://proxy.golang.org,direct \
  GOSUMDB=sum.golang.org \
  go test -mod=readonly ./...
mise exec go@1.26.5 -- env \
  GOTOOLCHAIN=local \
  GOPROXY=https://proxy.golang.org,direct \
  GOSUMDB=sum.golang.org \
  go vet -mod=readonly ./...
```

`HEAD` 必须等于上述 commit。测试和静态分析退出为零后，才能把当前机器上的结果记为已验证。

## L1：启动与命令

1. `main.go`
2. `cmd/root.go`
3. `cmd/pick.go`
4. `cmd/test.go`
5. `cmd/submit.go`

需要证明：命令在哪里注册；配置何时加载；错误如何成为进程退出状态；哪些步骤访问网络、文件和子进程。

## L2：配置、认证与外部 API

1. `config/config.go`
2. `config/state.go`
3. `leetcode/client.go`
4. `leetcode/client_us.go`
5. `leetcode/credential.go`
6. `leetcode/decoder.go`

需要证明：默认值、配置文件和 CLI 如何组合；凭证从哪里进入；HTTP timeout 和异常响应如何处理；哪些值不能
进入日志。至少使用一次 `httptest.Server` 覆盖成功、取消、超时和异常响应。

## L3：缓存与数据

1. `leetcode/cache.go`
2. `leetcode/cache_json.go`
3. `leetcode/cache_sqlite.go`
4. `leetcode/models.go`
5. `leetcode/question.go`

需要证明：`QuestionsCache` 接口由哪些调用方需要；JSON 与 SQLite 实现的行为是否一致；初始化、损坏数据和并发
访问分别如何失败。测试应从接口可观察行为出发，不复制实现细节。

## L4：生成、测试与子进程

1. `lang/base.go`
2. `lang/gen.go`
3. `lang/testcase.go`
4. `lang/test.go`
5. `lang/judge.go`
6. `editor/editor.go`
7. `utils/file.go`

需要证明：模板输入如何生成文件；路径与覆盖规则是什么；本地进程的标准输出、退出状态、timeout 和取消如何呈现
给用户。至少有一个不访问 LeetCode 的本地端到端测试。

## 真实修改选择

优先修复学习过程中亲自遇到且能够稳定复现的问题。没有合适问题时，再检查以下开放 issue：

- [#409：离线测试本地保存的题目](https://github.com/j178/leetgo/issues/409)
- [#278：为配置生成 JSON Schema](https://github.com/j178/leetgo/issues/278)
- [#167：一道题支持多个解法](https://github.com/j178/leetgo/issues/167)

2026-08-12 查询时三者均开放，但不表示维护者已经接受某个方案。#409 已指向作者自己的实现且范围可能过大；
#278 描述很短且可能引入依赖；#167 会同时影响生成、测试和提交。开始任务当天必须重新检查完整讨论、已有 PR、
固定 commit 上的复现和预计修改范围。

合格任务必须先有最小失败和验收测试，再做原则上不超过三个包的最小修改。若三小时内仍无法建立明确失败，
保留调查结果并更换任务，不用猜测需求。
