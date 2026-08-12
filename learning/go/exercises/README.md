# Go 课程练习

本目录是 Go 课程的可执行练习模块。每课使用独立子目录；练习只证明课程指定的行为，不作为通用软件包发布。

从仓库根目录运行全部检查：

```sh
mise run check learning-go
```

只运行第 1 课：

```sh
cd learning/go/exercises
go test -race ./lesson01
go run ./lesson01
```
