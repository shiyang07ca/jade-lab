# Created by shiyang07ca at 2023/06/08 13:29
# https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/

"""
1240. 铺瓷砖 (Hard)
你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。

房子的客厅大小为 `n` x `m`，为保持极简的风格，需要使用尽可能少的 **正方形** 瓷砖来铺盖地面。

假设正方形瓷砖的规格不限，边长都是整数。

请你帮设计师计算一下，最少需要用到多少块方形瓷砖？

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_11_1592.png)

```
输入：n = 2, m = 3
输出：3
解释：3 块地砖就可以铺满卧室。
     2 块 1x1 地砖
     1 块 2x2 地砖
```

**示例 2：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_22_1592.png)

```
输入：n = 5, m = 8
输出：5

```

**示例 3：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_33_1592.png)

```
输入：n = 11, m = 13
输出：6

```

**提示：**

- `1 <= n <= 13`
- `1 <= m <= 13`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: backtracking

# 链接：https://leetcode.cn/problems/tiling-a-rectangle-with-the-fewest-squares/solutions/2301323/python3javacgotypescript-yi-ti-yi-jie-di-tpge/
class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        def dfs(i: int, j: int, t: int):
            nonlocal ans
            if j == m:
                i += 1
                j = 0
            if i == n:
                ans = t
                return
            if filled[i] >> j & 1:
                dfs(i, j + 1, t)
            elif t + 1 < ans:
                r = c = 0
                for k in range(i, n):
                    if filled[k] >> j & 1:
                        break
                    r += 1
                for k in range(j, m):
                    if filled[i] >> k & 1:
                        break
                    c += 1
                mx = r if r < c else c
                for w in range(1, mx + 1):
                    for k in range(w):
                        filled[i + w - 1] |= 1 << (j + k)
                        filled[i + k] |= 1 << (j + w - 1)
                    dfs(i, j + w, t + 1)
                for x in range(i, i + mx):
                    for y in range(j, j + mx):
                        filled[x] ^= 1 << y

        ans = n * m
        filled = [0] * n
        dfs(0, 0, 0)
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    m: int = deserialize("int", read_line())
    ans = Solution().tilingRectangle(n, m)

    print("\noutput:", serialize(ans))
