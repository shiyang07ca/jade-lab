# Created by shiyang07ca at 2023/10/30 00:07
# leetgo: dev
# https://leetcode.cn/problems/h-index-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: binary search


class Solution:
    def hIndex1(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i, c in enumerate(citations, start=1):
            if c < i:
                return i - 1
        return i

    # https://leetcode.cn/problems/h-index-ii/solutions/871112/gong-shui-san-xie-liang-chong-er-fen-ji-sovjb
    def hIndex(self, cs: List[int]) -> int:
        n = len(cs)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) >> 1
            if cs[mid] >= n - mid:
                r = mid
            else:
                l = mid + 1
        return n - r if cs[r] >= n - r else 0


# @lc code=end

if __name__ == "__main__":
    citations: List[int] = deserialize("List[int]", read_line())
    ans = Solution().hIndex(citations)

    print("\noutput:", serialize(ans))
