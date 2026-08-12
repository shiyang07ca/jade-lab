# Jade Algorithms

这是一个面向算法复习、面试准备和本地题解原型的 Python 软件包。使用方通过
`jade_algorithms` 导入公开名称；模块内部文件和数据结构不属于公开接口。

## 使用

仓库内的实际消费方是
[`labs/algorithms/python-implementations/`](../../labs/algorithms/python-implementations/)。从该目录添加可编辑依赖的
命令是：

```sh
uv add --editable ../../../packages/python-algorithms
```

```python
from jade_algorithms import DisjointSet, sliding_window_max

groups = DisjointSet(4)
groups.union(0, 1)
assert groups.connected(0, 1)
assert sliding_window_max([4, 3, 5, 2], 2) == [4, 5, 5]
```

公开接口包含并查集、最小堆、滑动窗口最大值、质数筛、二维前缀和、区间增量、斐波那契序列和
0-1 背包。无第三方运行时依赖；非法类型使用 `TypeError`，取值或范围无效使用 `ValueError`，访问不存在的
并查集元素或空堆使用 `IndexError`。

## 验证

```sh
mise install python uv
uv sync --frozen
uv run --frozen pytest
uv run --frozen ruff check .
uv build
```

测试只从 `jade_algorithms` 公开接口导入，构建必须生成可安装的 wheel 和源码包。仅用于讲解的另一种实现、
题目输入输出代码或未验证片段不进入本软件包。
