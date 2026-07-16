# Created by shiyang07ca at 2023/06/26 13:08
# https://leetcode.cn/problems/find-the-pivot-integer/

"""
2485. 找出中枢整数 (Easy)
给你一个正整数 `n` ，找出满足下述条件的 **中枢整数** `x` ：

- `1` 和 `x` 之间的所有元素之和等于 `x` 和 `n` 之间所有元素
之和。

返回中枢整数 `x` 。如果不存在中枢整数，则返回 `-1` 。题目保
证对于给定的输入，至多存在一个中枢整数。

**示例 1：**

```
输入：n = 8
输出：6
解释：6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 =
21 。

```

**示例 2：**

```
输入：n = 1
输出：1
解释：1 是中枢整数，因为 1 = 1 。

```

**示例 3：**

```
输入：n = 4
输出：-1
解释：可以证明不存在满足题目要求的整数。
```

**提示：**

- `1 <= n <= 1000`

"""

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def pivotInteger(self, n: int) -> int:
        pre, nxt = 0, sum(list(range(n + 1)))
        for i in range(1, n + 1):
            pre += i
            if pre == nxt:
                return i
            nxt -= i
        return -1


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().pivotInteger(n)
    print("output:", serialize(ans))
