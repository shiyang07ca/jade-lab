# Python 竞赛算法手册

本目录是非发布型 uv 项目。主题实现直接放在目录根部，使用 0 基索引；区间查询除
`apply_range_additions` 的更新三元组外均采用半开区间。

当前主题包括：二分查找、排序、快速选择、图表示、BFS、Dijkstra、拓扑排序、最近公共祖先、并查集、最小堆、
Fenwick 树、三类线段树、链表反转、单调栈、递归反转栈、二叉树构建与遍历、Trie、Manacher、
0-1 背包、质数筛与质因数分解、前缀和与差分、Fibonacci 和滑动窗口最大值。

[sorting.py](sorting.py) 中的 `quickselect(values, k)` 返回升序下标 `k` 对应的元素，
使用随机基准和原地三路划分，会修改输入列表，重复元素各占一个位置。
元素需支持一致的大小比较；空列表或下标不在 `[0, len(values))` 内时抛出 `IndexError`。
期望时间 `O(n)`，最坏时间 `O(n²)`，额外空间 `O(1)`。

```python
from sorting import quickselect

values = [3, 2, 1, 5, 6, 4]
quickselect(values, 0)                # 最小值：1
quickselect(values, 2 - 1)            # 第 2 小：2
quickselect(values, len(values) - 2)  # 第 2 大：5
```

[union_find.py](union_find.py) 中的 `UnionFind` 参考题解
[02867](../../leetcode/02867/python/solution.py) 和
[codeforces-go 并查集模板](../../../references/codeforces-go/copypasta/union_find.go)，使用非递归路径压缩和按大小合并。
调用方保证 `n >= 0` 且下标在 `[0, n)` 内；单次操作均摊 `O(alpha(n))`，空间 `O(n)`。

```python
from union_find import UnionFind

uf = UnionFind(5)
uf.union(0, 1)       # 合并成功返回 True，已经连通返回 False
uf.same(0, 1)        # 是否连通
uf.find(1)           # 代表元，不保证是最小或最大编号
uf.size[uf.find(1)]  # 连通块大小，只有根节点的 size 有效
uf.groups           # 连通块数量
```

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
