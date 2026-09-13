# Python 算法实现实验

本实验集中保存 Python 算法、数据结构和竞赛实现，包括 `algorithms` 中已经整理的实现和仍在逐项审查的旧实现。
这些代码服务于算法复习、题解原型和实验比较，不再单独作为可发布的软件包维护。

`algorithms` 是本实验内部的导入包，公开入口在
[`algorithms/__init__.py`](algorithms/__init__.py)。其他实验代码和测试可以从公开入口导入；
`algorithms/`、`competitive-programming/` 和 `data-structures/` 下的代码仍按文件自身的验证程度使用。

```sh
mise install python uv
mise run check lab-python-implementations
```

当前检查运行 `algorithms` 的行为测试，并对实验源码执行语法编译。需要把某项实现用于其他独立项目时，
再根据实际调用场景重新整理为软件包，而不是在本实验外复制一份源码。
