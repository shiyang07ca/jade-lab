# Created by shiyang07ca at 2023/05/10 12:58
# https://leetcode.cn/problems/smallest-integer-divisible-by-k/

"""
1015. 可被 K 整除的最小整数 (Medium)
给定正整数 `k` ，你需要找出可以被 `k` 整除的、仅包含数字 `1`
的最 **小** 正整数 `n` 的长度。

返回 `n` 的长度。如果不存在这样的 `n` ，就返回-1。

**注意：** `n` 不符合 64 位带符号整数。

**示例 1：**

```
输入：k = 1
输出：1
解释：最小的答案是 n = 1，其长度为 1。
```

**示例 2：**

```
输入：k = 2
输出：-1
解释：不存在可被 2 整除的正整数 n 。
```

**示例 3：**

```
输入：k = 3
输出：3
解释：最小的答案是 n = 111，其长度为 3。
```

**提示：**

- `1 <= k <= 10⁵`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO

# tag: math

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/smallest-integer-divisible-by-k/solutions/2263780/san-chong-suan-fa-you-hua-pythonjavacgo-tk4cj/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


class Solution:
    def smallestRepunitDivByK1(self, k: int) -> int:
        seen = set()
        x = 1 % k
        while x and x not in seen:
            seen.add(x)
            x = (x * 10 + 1) % k
        return -1 if x else len(seen) + 1


# 作者：ylb
# 链接：https://leetcode.cn/problems/smallest-integer-divisible-by-k/solutions/2263918/python3javacgotypescript-yi-ti-yi-jie-sh-8ox9/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        n = 1 % k
        for i in range(1, k + 1):
            if n == 0:
                return i
            n = (n * 10 + 1) % k
        return -1


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    ans = Solution().smallestRepunitDivByK(k)
    print("output:", serialize(ans))
