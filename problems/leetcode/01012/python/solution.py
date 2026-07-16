# Created by shiyang07ca at 2023/06/05 22:21
# https://leetcode.cn/problems/numbers-with-repeated-digits/

"""
1012. 至少有 1 位重复的数字 (Hard)
给定正整数 `n`，返回在 `[1, n]` 范围内具有 **至少 1 位** 重复数字的正整数的个数。

**示例 1：**

```
输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

```

**示例 2：**

```
输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

```

**示例 3：**

```
输入：n = 1000
输出：262

```

**提示：**

- `1 <= n <= 10⁹`

"""
from functools import *

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: dp


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        s = str(n)

        @cache  # 记忆化搜索
        def f(i: int, mask: int, is_limit: bool, is_num: bool) -> int:
            if i == len(s):
                return int(is_num)  # is_num 为 True 表示得到了一个合法数字
            res = 0
            if not is_num:  # 可以跳过当前数位
                res = f(i + 1, mask, False, False)
            low = 0 if is_num else 1  # 如果前面没有填数字，必须从 1 开始（因为不能有前导零）
            up = (
                int(s[i]) if is_limit else 9
            )  # 如果前面填的数字都和 n 的一样，那么这一位至多填 s[i]（否则就超过 n 啦）
            for d in range(low, up + 1):  # 枚举要填入的数字 d
                if (mask >> d & 1) == 0:  # d 不在 mask 中
                    res += f(i + 1, mask | (1 << d), is_limit and d == up, True)
            return res

        return n - f(0, 0, True, False)


# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/numbers-with-repeated-digits/solutions/1748539/by-endlesscheng-c5vg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().numDupDigitsAtMostN(n)

    print("\noutput:", serialize(ans))
