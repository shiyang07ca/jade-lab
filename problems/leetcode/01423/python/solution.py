from __future__ import annotations

# Created by shiyang07ca at 2023/12/03 00:14
# leetgo: dev
# https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def maxScore(self, ps: list[int], k: int) -> int:
        n = len(ps)
        ans = suf = sum(ps[-k:])
        for i in range(n - k, n):
            suf -= ps[i]
            suf += ps[(i + k) % n]
            ans = max(ans, suf)
        return max(ans, suf)


# @lc code=end

if __name__ == "__main__":
    cardPoints: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().maxScore(cardPoints, k)

    print("\noutput:", serialize(ans))
