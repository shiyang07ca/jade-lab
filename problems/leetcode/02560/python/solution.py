# Created by shiyang07ca at 2023/09/18 08:26
# leetgo: dev
# https://leetcode.cn/problems/house-robber-iv/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: binary search, dp

"""
链接：https://leetcode.cn/problems/house-robber-iv/solution/er-fen-da-an-dp-by-endlesscheng-m558/

设二分的最大金额为 mx，定义 f[i] 表示在前 i 个房屋中窃取金额不超过 mx 的房屋最大个数

分类讨论：
  * 不选第 i 个房屋：f[i] = f[i-1]
  * 选第 i 个房屋，前提是金额不超过 mx：f[i] = f[i-2] + 1
两者取最大值，即
       f[i] = max(f[i−1], f[i−2]+1)

代码实现时，可以用两个变量滚动计算。

"""


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(mx):
            d0 = d1 = 0
            for n in nums:
                if n > mx:
                    d0 = d1
                else:
                    d0, d1 = d1, max(d0 + 1, d1)
            return d1

        l, r = 0, max(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid) >= k:
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().minCapability(nums, k)

    print("\noutput:", serialize(ans))
