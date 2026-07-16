# Created by shiyang07ca at 2023/06/01 00:00
# https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/

"""
2517. 礼盒的最大甜蜜度 (Medium)
给你一个正整数数组 `price` ，其中 `price[i]` 表示第 `i` 类糖果的价格，另给你一个正整数 `k` 。

商店组合 `k` 类 **不同** 糖果打包成礼盒出售。礼盒的 **甜蜜度** 是礼盒中任意两种糖果 **价格** 绝对差
的最小值。

返回礼盒的 **最大** 甜蜜度。

**示例 1：**

```
输入：price = [13,5,1,8,21,2], k = 3
输出：8
解释：选出价格分别为 [13,5,21] 的三类糖果。
礼盒的甜蜜度为 min(|13 - 5|, |13 - 21|, |5 - 21|) = min(8, 8, 16) = 8 。
可以证明能够取得的最大甜蜜度就是 8 。

```

**示例 2：**

```
输入：price = [1,3,1], k = 2
输出：2
解释：选出价格分别为 [1,3] 的两类糖果。
礼盒的甜蜜度为 min(|1 - 3|) = min(2) = 2 。
可以证明能够取得的最大甜蜜度就是 2 。

```

**示例 3：**

```
输入：price = [7,7,7,7], k = 2
输出：0
解释：从现有的糖果中任选两类糖果，甜蜜度都会是 0 。

```

**提示：**

- `1 <= price.length <= 10⁵`
- `1 <= price[i] <= 10⁹`
- `2 <= k <= price.length`

"""

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: binary search

# https://leetcode.cn/problems/maximum-tastiness-of-candy-basket/solutions/2031994/er-fen-da-an-by-endlesscheng-r418/
class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        """
        随着甜蜜度增大，能选择的 k 变小，有单调性，可以二分

        定义 f(d)表示甜蜜度至少为 d 时，至多能选多少类糖果
        将 price 从小到大排序，从 price[0] 开始选；假设上一个可以选的数是 pre，
        那么当 price[i] >= pre + d 时，才可以选 price[i]
        """

        price.sort()

        def f(d):
            cnt = 1
            pre = price[0]
            for p in price:
                if p >= pre + d:
                    cnt += 1
                    pre = p

            return cnt

        l, r = 0, 10**9
        while l < r:
            mid = (l + r + 1) >> 1
            if f(mid) >= k:
                l = mid
            else:
                r = mid - 1

        return l


# @lc code=end

if __name__ == "__main__":
    price: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maximumTastiness(price, k)

    print("\noutput:", serialize(ans))
