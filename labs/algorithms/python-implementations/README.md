# Python 算法实现实验

本实验保留尚未形成稳定公开接口的 Python 算法、数据结构和竞赛实现。它们仍有逐项审查和比较价值，但部分文件
只有内嵌 `unittest`、依赖当前目录导入或同时包含多种未验证实现，因此不能从目录位置推断可复用性。

已经整理并由消费方测试验证的实现位于
[`packages/python-algorithms/`](../../../packages/python-algorithms/)；本实验测试只通过 `jade_algorithms` 公开接口
调用它们，避免重新复制一份实现。

```sh
mise install python uv
mise run check lab-python-implementations
```

当前检查运行消费方测试，并对保留源码执行语法编译。某个旧实现需要复用时，逐项补输入限制、错误类型和行为测试，
然后移动到按能力命名的软件包；其余源码继续作为实验保留，不标记为稳定。
