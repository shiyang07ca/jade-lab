# Created by shiyang07ca at 2023/05/02 16:11
# https://leetcode.cn/problems/ones-and-zeroes/

"""
474. 一和零 (Medium)
给你一个二进制字符串数组 `strs` 和两个整数 `m` 和 `n` 。

请你找出并返回 `strs` 的最大子集的长度，该子集中 **最多** 有
`m` 个 `0` 和 `n` 个 `1` 。

如果 `x` 的所有元素也是 `y` 的元素，集合 `x` 是集合 `y` 的 *
*子集** 。

**示例 1：**

```
输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n =
3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1",
"0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"}
。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

```

**示例 2：**

```
输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

```

**提示：**

- `1 <= strs.length <= 600`
- `1 <= strs[i].length <= 100`
- `strs[i]` 仅由 `'0'` 和 `'1'` 组成
- `1 <= m, n <= 100`

"""
from functools import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


class Solution:
    # 记忆化搜索
    def findMaxForm1(self, strs: List[str], m: int, n: int) -> int:
        @cache
        def dfs(m, n, i):
            if i >= len(strs):
                return 0
            c0 = strs[i].count("0")
            c1 = strs[i].count("1")
            if c0 <= m and c1 <= n:
                return max(dfs(m, n, i + 1), dfs(m - c0, n - c1, i + 1) + 1)
            else:
                return dfs(m, n, i + 1)

        return dfs(m, n, 0)

    # 递推
    def findMaxForm2(self, strs: List[str], m: int, n: int) -> int:
        f = [
            [[0 for _ in range(n + 1)] for _ in range(m + 1)]
            for _ in range(len(strs) + 1)
        ]
        sl = [(s.count("0"), s.count("1")) for s in strs]
        for k in range(len(strs) - 1, -1, -1):
            for i in range(m + 1):
                for j in range(n + 1):
                    c0, c1 = sl[k]
                    if c0 <= i and c1 <= j:
                        f[k][i][j] = max(f[k + 1][i][j], f[k + 1][i - c0][j - c1] + 1)
                    else:
                        f[k][i][j] = f[k + 1][i][j]

        return f[0][m][n]

    # TODO 思考如何滚动更新？
    # 滚动数组
    def findMaxForm3(self, strs: List[str], m: int, n: int) -> int:
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        sl = [(s.count("0"), s.count("1")) for s in strs]
        for k in range(len(strs) - 1, -1, -1):
            c0, c1 = sl[k]
            for i in range(m, c0 - 1, -1):
                for j in range(n, c1 - 1, -1):
                    f[i][j] = max(f[i][j], f[i - c0][j - c1] + 1)
        return f[m][n]

    # TODO 这个为什么是错的？
    # 滚动数组
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        f = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        sl = [(s.count("0"), s.count("1")) for s in strs]
        for k in range(len(strs) - 1, -1, -1):
            c0, c1 = sl[k]
            for i in range(m+1):
                for j in range(n+1):
                    if c0 <= i and c1 <= j:
                        f[i][j] = max(f[i][j], f[i - c0][j - c1] + 1)
        print(f)
        return f[m][n]


# @lc code=end

if __name__ == "__main__":
    strs: List[str] = deserialize("List[str]", read_line())
    m: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().findMaxForm(strs, m, n)
    print("output:", serialize(ans))
