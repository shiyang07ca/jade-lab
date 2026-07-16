# Created by shiyang07ca at 2023/06/16 12:50
# https://leetcode.cn/problems/parallel-courses-ii/

"""
1494. 并行课程 II (Hard)
给你一个整数 `n` 表示某所大学里课程的数目，编号为 `1` 到 `n` ，数组 `relations` 中， `relations[i] =
[xᵢ, yᵢ]`  表示一个先修课的关系，也就是课程 `xᵢ` 必须在课程 `yᵢ` 之前上。同时你还有一个整数 `k` 。

在一个学期中，你 **最多** 可以同时上 `k` 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

**示例 1：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_1
.png)**

```
输入：n = 4, relations = [[2,1],[3,1],[1,4]], k = 2
输出：3
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，
第三个学期上课程 4 。

```

**示例 2：**

**![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_2
.png)**

```
输入：n = 5, relations = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课
程 1 ，第四学期上课程 5 。

```

**示例 3：**

```
输入：n = 11, relations = [], k = 2
输出：6

```

**提示：**

- `1 <= n <= 15`
- `1 <= k <= n`
- `0 <= relations.length <= n * (n-1) / 2`
- `relations[i].length == 2`
- `1 <= xᵢ, yᵢ <= n`
- `xᵢ != yᵢ`
- 所有先修关系都是不同的，也就是说 `relations[i] != relations[j]` 。
- 题目输入的图是个有向无环图。

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp, bitmask


class Solution:
    # 链接：https://leetcode.cn/problems/parallel-courses-ii/solutions/2310878/zi-ji-zhuang-ya-dpcong-ji-yi-hua-sou-suo-oxwd/
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        """
        设全集 U = {0, 1, 2, ..., n-1}, 设 pre[j] 为集合 j 中所有先修课的并集。

        定义 dfs(i) 表示上完集合 i 中的课程，最少需要多少个学期（注意这意味着补
        集 Cui 中的课程均已修完）

        """
        pre1 = [0] * n
        for x, y in relations:
            pre1[y - 1] |= 1 << (x - 1)  # y 的先修课程集合，下标改从 0 开始

        u = (1 << n) - 1  # 全集

        @cache  # 记忆化搜索
        def dfs(i: int) -> int:
            if i == 0:  # 空集
                return 0
            ci = u ^ i  # i 的补集
            i1 = 0  # i1 表示可以学的课程
            for j, p in enumerate(pre1):
                if i >> j & 1 and p | ci == ci:  # p 在 i 的补集中，可以学（否则这学期一定不能学）
                    i1 |= 1 << j
            if i1.bit_count() <= k:  # 如果个数小于 k，则可以全部学习，不再枚举子集
                return dfs(i ^ i1) + 1
            res = inf
            j = i1
            while j:  # 枚举 i1 的子集 j
                if j.bit_count() == k:
                    res = min(res, dfs(i ^ j) + 1)
                j = (j - 1) & i1
            return res

        return dfs(u)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    relations: List[List[int]] = deserialize("List[List[int]]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minNumberOfSemesters(n, relations, k)

    print("\noutput:", serialize(ans))
