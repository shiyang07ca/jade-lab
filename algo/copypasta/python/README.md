# Python 竞赛算法手册

本目录是非发布型 uv 项目。主题实现直接放在目录根部，使用 0 基索引；区间查询除
`apply_range_additions` 的更新三元组外均采用半开区间。

当前主题包括：二分查找、排序、图表示、BFS、Dijkstra、拓扑排序、最近公共祖先、并查集、最小堆、
Fenwick 树、三类线段树、链表反转、单调栈、递归反转栈、二叉树构建与遍历、Trie、Manacher、
0-1 背包、质数筛与质因数分解、前缀和与差分、Fibonacci 和滑动窗口最大值。

线段树能力分别由以下类提供：

- `SumSegmentTree`：单点赋值、区间和。
- `LazyMinSegmentTree`：区间加、区间最小值。
- `RangeAssignSumTree`：区间赋值、区间和。

验证命令：

```sh
cd algo/copypasta/python
uv lock
uv run --frozen pytest
uv run --frozen ruff check .
uv run --frozen python -m compileall -q *.py tests
```
