# Created by shiyang07ca at 2023/06/29 00:23
# https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/

"""
1253. 重构 2 行二进制矩阵 (Medium)
给你一个 `2` 行 `n` 列的二进制数组：

- 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 `0` 就是 `1`。
- 第 `0` 行的元素之和为 `upper`。
- 第 `1` 行的元素之和为 `lower`。
- 第 `i` 列（从 `0` 开始编号）的元素之和为 `colsum[i]`， `colsum` 是一个长度为 `n` 的整数数组。

你需要利用 `upper`， `lower` 和 `colsum` 来重构这个矩阵，并以二维整数数组的形式返回它。

如果有多个不同的答案，那么任意一个都可以通过本题。

如果不存在符合要求的答案，就请返回一个空的二维数组。

**示例 1：**

```
输入：upper = 2, lower = 1, colsum = [1,1,1]
输出：[[1,1,0],[0,0,1]]
解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。

```

**示例 2：**

```
输入：upper = 2, lower = 3, colsum = [2,2,1,1]
输出：[]

```

**示例 3：**

```
输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

```

**提示：**

- `1 <= colsum.length <= 10^5`
- `0 <= upper, lower <= colsum.length`
- `0 <= colsum[i] <= 2`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def reconstructMatrix1(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        if upper + lower != sum(colsum):
            return []

        n = len(colsum)
        ans = [[0] * n, [0] * n]
        for i, s in enumerate(colsum):
            if s == 2:
                if upper > 0 and lower > 0:
                    ans[0][i] = 1
                    ans[1][i] = 1
                    upper -= 1
                    lower -= 1
                else:
                    return []

        for i, s in enumerate(colsum):
            if s == 1:
                if upper > 0:
                    ans[0][i] = 1
                    upper -= 1
                elif lower > 0:
                    ans[1][i] = 1
                    lower -= 1
                else:
                    return []
        return ans

    # 链接：https://leetcode.cn/problems/reconstruct-a-2-row-binary-matrix/solutions/2324031/python3javacgotypescript-yi-ti-yi-jie-ta-ecug/
    def reconstructMatrix(
        self, upper: int, lower: int, colsum: List[int]
    ) -> List[List[int]]:
        n = len(colsum)
        ans = [[0] * n for _ in range(2)]
        for j, v in enumerate(colsum):
            if v == 2:
                ans[0][j] = ans[1][j] = 1
                upper, lower = upper - 1, lower - 1
            if v == 1:
                if upper > lower:
                    upper -= 1
                    ans[0][j] = 1
                else:
                    lower -= 1
                    ans[1][j] = 1
            if upper < 0 or lower < 0:
                return []
        return ans if lower == upper == 0 else []


# @lc code=end

if __name__ == "__main__":
    upper: int = deserialize("int", read_line())
    lower: int = deserialize("int", read_line())
    colsum: List[int] = deserialize("List[int]", read_line())
    ans = Solution().reconstructMatrix(upper, lower, colsum)

    print("\noutput:", serialize(ans))
