# Created by shiyang07ca at 2023/06/20 23:05
# https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/

"""
1595. 连通两组点的最小成本 (Hard)
给你两组点，其中第一组中有 `size₁` 个点，第二组中有 `size₂` 个点，且 `size₁ >= size₂` 。

任意两点间的连接成本 `cost` 由大小为 `size₁ x size₂` 矩阵给出，其中 `cost[i][j]` 是第一组中的点 `i`
和第二组中的点 `j` 的连接成本。 **如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是
连通的。** 换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一
组中的一个点连接。

返回连通两组点所需的最小成本。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex1.jpg)

```
输入：cost = [[15, 96], [36, 2]]
输出：17
解释：连通两组点的最佳方法是：
1--A
2--B
总成本为 17 。

```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex2.jpg)

```
输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
输出：4
解释：连通两组点的最佳方法是：
1--A
2--B
2--C
3--A
最小成本为 4 。
请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需
要关心最低总成本。
```

**示例 3：**

```
输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
输出：10

```

**提示：**

- `size₁ == cost.length`
- `size₂ == cost[i].length`
- `1 <= size₁, size₂ <= 12`
- `size₁ >= size₂`
- `0 <= cost[i][j] <= 100`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp, bitmask


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/minimum-cost-to-connect-two-groups-of-points/solutions/2314687/jiao-ni-yi-bu-bu-si-kao-dong-tai-gui-hua-djxq/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    # 定义 dfs(i, j) 表示第一组 0,1,...,i 和第二组中的 0,1,...,m-1 相连，且第二组的集合
    # j 未被连接时，最小成本是多少
    # 枚举第一组的点 i 和第二组的 0，1，，，，，m-1 其中一个点先练，取最小值，即
    #                dfs(i, j) = min(dfs(i - 1, j \ {k}) + cost[i][k]), 0<=k<=m-1
    # 其中 j\{k} 表示集合 j 中去掉元素 k 后的集合。
    # 递归边界：设第二组的点 x 与第一组的点连接时，最小成本是 minCost[x], 那么有
    #                dfs(-1, j) = sum(minCost[k])
    def connectTwoGroups1(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])
        min_cost = [min(col) for col in zip(*cost)]  # 每一列的最小值

        @cache  # 记忆化搜索
        def dfs(i: int, j: int) -> int:
            if i < 0:
                return sum(c for k, c in enumerate(min_cost) if j >> k & 1)
            return min(
                dfs(i - 1, j & ~(1 << k)) + c for k, c in enumerate(cost[i])
            )  # 第一组的点 i 与第二组的点 k

        return dfs(n - 1, (1 << m) - 1)

    # 递推
    # f[i+1][j] = min(f[i][j\{k] + cost[i][k]), 0<=k<=m-1
    # 初始值 f[0][j] = sum(minCost[k])
    def connectTwoGroups(self, cost: List[List[int]]) -> int:
        n, m = len(cost), len(cost[0])
        min_cost = [min(col) for col in zip(*cost)]  # 每一列的最小值

        f = [[0] * (1 << m) for _ in range(n + 1)]
        for j in range(1 << m):
            f[0][j] = sum(c for k, c in enumerate(min_cost) if j >> k & 1)

        for i, row in enumerate(cost):
            for j in range(1 << m):
                f[i + 1][j] = min(
                    f[i][j & ~(1 << k)] + c for k, c in enumerate(row)
                )  # 第一组的点 i 与第二组的点 k
        return f[n][-1]


# @lc code=end

if __name__ == "__main__":
    cost: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().connectTwoGroups(cost)

    print("\noutput:", serialize(ans))
