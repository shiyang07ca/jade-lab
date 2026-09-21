# Go 竞赛算法手册

这是独立 Go 模块，目前只包含经过行为测试的并查集，以及使用
`run(io.Reader, io.Writer)` 组织 OJ 输入输出的两数求和示例。代码面向复制使用，不承诺发布接口稳定性。

```sh
cd algo/copypasta/go
gofmt -w .
go test ./...
go vet ./...
printf '19 23\n' | go run .
```
