# Created by shiyang07ca at 2023/07/25 12:50
# leetgo: dev
# https://leetcode.cn/problems/minimum-operations-to-halve-array-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        t = sum(nums) / 2
        ans = 0
        h = []
        for n in nums:
            heappush(h, -n)
        while True:
            if t > 0:
                t -= -h[0] / 2
                heapreplace(h, h[0] / 2)
                ans += 1
            else:
                return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().halveArray(nums)

    print("\noutput:", serialize(ans))
