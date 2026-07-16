# Created by shiyang07ca at 2023/10/18 00:03
# leetgo: dev
# https://leetcode.cn/problems/maximal-score-after-applying-k-operations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = [-n for n in nums]
        heapify(h)
        ans = 0
        for _ in range(k):
            ans += -h[0]
            heapreplace(h, -ceil(-h[0] / 3))

        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxKelements(nums, k)

    print("\noutput:", serialize(ans))
