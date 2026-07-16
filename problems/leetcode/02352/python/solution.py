# Created by shiyang07ca at 2023/06/06 13:11
# https://leetcode.cn/problems/equal-row-and-column-pairs/

"""
2352. 相等行列对 (Medium)
给你一个下标从 **0** 开始、大小为 `n x n` 的整数矩阵 `grid` ，返回满足 `Rᵢ` 行和 `Cⱼ` 列相等的行列对
`(Rᵢ, Cⱼ)` 的数目。

如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。

**示例 1：**

![](https://assets.leetcode.com/uploads/2022/06/01/ex1.jpg)

```
输入：grid = [[3,2,1],[1,7,6],[2,7,7]]
输出：1
解释：存在一对相等行列对：
- (第 2 行，第 1 列)：[2,7,7]

```

**示例 2：**

![](https://assets.leetcode.com/uploads/2022/06/01/ex2.jpg)

```
输入：grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
输出：3
解释：存在三对相等行列对：
- (第 0 行，第 0 列)：[3,1,2,2]
- (第 2 行, 第 2 列)：[2,4,2,2]
- (第 3 行, 第 2 列)：[2,4,2,2]

```

**提示：**

- `n == grid.length == grid[i].length`
- `1 <= n <= 200`
- `1 <= grid[i][j] <= 10⁵`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def equalPairs1(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        for row in grid:
            for i in range(n):
                flag = True
                for j in range(n):
                    if row[j] != grid[j][i]:
                        flag = False
                        break
                ans += int(flag)
        return ans

    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid)
        cnt = defaultdict(int)
        for row in grid:
            cnt[tuple(row)] += 1
        for i in range(n):
            ans += cnt[tuple(grid[j][i] for j in range(n))]

        return ans


# @lc code=end

if __name__ == "__main__":
    grid: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().equalPairs(grid)

    print("\noutput:", serialize(ans))
