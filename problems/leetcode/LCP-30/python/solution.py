# Created by shiyang07ca at 2024/02/06 00:46
# leetgo: dev
# https://leetcode.cn/problems/p0NxJO/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/p0NxJO/solutions/2633201/python3javacgotypescript-yi-ti-yi-jie-ta-8cfy/
    def magicTower(self, nums: List[int]) -> int:
        q = []
        blood = 1
        ans = v = 0
        for x in nums:
            if x < 0:
                heappush(q, x)
            blood += x
            if blood <= 0:
                ans += 1
                v += q[0]
                blood -= heappop(q)
        blood += v
        return -1 if blood <= 0 else ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().magicTower(nums)

    print("\noutput:", serialize(ans))
