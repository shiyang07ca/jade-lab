# Created by shiyang07ca at 2023/05/31 00:05
# https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/

"""
1130. 叶值的最小代价生成树 (Medium)
给你一个正整数数组 `arr`，考虑所有满足以下条件的二叉树：

- 每个节点都有 `0` 个或是 `2` 个子节点。
- 数组 `arr` 中的值与树的中序遍历中每个叶节点的值一一对应。
- 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。

在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

如果一个节点有 0 个子节点，那么该节点为叶节点。

**示例 1：**

![](https://assets.leetcode.com/uploads/2021/08/10/tree1.jpg)

```
输入：arr = [6,2,4]
输出：32
解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2021/08/10/tree2.jpg)

```
输入：arr = [4,11]
输出：44

```

**提示：**

- `2 <= arr.length <= 40`
- `1 <= arr[i] <= 15`
- 答案保证是一个 32 位带符号整数，即小于 `2³¹` 。

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


# 链接：https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/solutions/2290549/python3javacgotypescript-yi-ti-shuang-ji-qpwv/
class Solution:
    def mctFromLeafValues1(self, arr: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> Tuple:
            if i == j:
                return 0, arr[i]
            s, mx = inf, -1
            for k in range(i, j):
                s1, mx1 = dfs(i, k)
                s2, mx2 = dfs(k + 1, j)
                t = s1 + s2 + mx1 * mx2
                if s > t:
                    s = t
                    mx = max(mx1, mx2)
            return s, mx

        return dfs(0, len(arr) - 1)[0]

    def mctFromLeafValues(self, arr: List[int]) -> int:
        @cache
        def dfs(i: int, j: int) -> int:
            if i == j:
                return 0
            return min(
                dfs(i, k) + dfs(k + 1, j) + g[i][k] * g[k + 1][j] for k in range(i, j)
            )

        n = len(arr)
        # 使用数组 g 记录 arr 中下表范围 [i, j] 内的所有叶节点最大值
        g = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            g[i][i] = arr[i]
            for j in range(i + 1, n):
                g[i][j] = max(g[i][j - 1], arr[j])
        return dfs(0, n - 1)


# @lc code=end

if __name__ == "__main__":
    arr: List[int] = deserialize("List[int]", read_line())
    ans = Solution().mctFromLeafValues(arr)

    print("\noutput:", serialize(ans))
