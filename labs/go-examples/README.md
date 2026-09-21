# Go 语言与标准库示例

这里保存可独立运行的 Go 语言、标准库与并发示例，内容最初参考 [Go by Example](https://gobyexample.com/)。每个子目录都是独立的 `main` package，用于观察指针、接口、错误、goroutine、channel、同步和时间控制等行为；这些目录不是供其他 Go 代码导入的软件包。

进入本目录后运行全部检查或单个示例：

```sh
test -z "$(gofmt -l .)"
go test ./...
go vet ./...
go run ./language/channels
```
