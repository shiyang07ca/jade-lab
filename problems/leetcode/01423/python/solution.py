# Created by shiyang07ca at 2023/12/03 00:14
# leetgo: dev
# https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maxScore(self, ps: List[int], k: int) -> int:
        n = len(ps)
        ans = suf = sum(ps[-k:])
        for i in range(n - k, n):
            suf -= ps[i]
            suf += ps[(i + k) % n]
            ans = max(ans, suf)
        return max(ans, suf)


# @lc code=end

if __name__ == "__main__":
    cardPoints: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)

    print("\noutput:", serialize(ans))
