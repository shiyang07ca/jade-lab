# Created by shiyang07ca at 2026/09/29 19:53
# leetgo: 1.4.17
# https://leetcode.cn/problems/increasing-triplet-subsequence/

from bisect import bisect_left
from typing import *

from leetgo_py import *

# @lc code=begin

# TODO

# 链接：https://leetcode.cn/problems/increasing-triplet-subsequence/solutions/3844143/tong-yong-jie-fa-ba-3-gai-cheng-k-ye-nen-t8si/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == 2:  # LIS 长度至少是 3
                return True
            if j == len(g):  # >=x 的 g[j] 不存在
                g.append(x)
            else:
                g[j] = x
        return False


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().increasingTriplet(nums)
    print("\noutput:", serialize(ans, "boolean"))
