# Go 语言机制实验

本实验保留能够独立运行的 Go 语言与并发机制程序，内容最初参考
[Go by Example](https://gobyexample.com/)。每个子目录都是独立 `main` package，用于观察指针、接口、错误、
goroutine、channel、同步和时间控制等行为；它们不是供其他 Go 代码导入的软件包，也不代表 Go 课程已经掌握。

```sh
mise install go
mise run check lab-go-fundamentals
go run ./language/channels
```

`go test ./...` 主要证明所有程序可用 Go 1.26.5 编译，只有少数目录有行为测试。学习时应先写出要验证的问题，
运行相关程序并增加测试；出现真实代码调用方后，再把稳定且通用的实现迁入按能力命名的 `packages/<name>/`。
