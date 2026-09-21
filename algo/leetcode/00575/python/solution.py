from __future__ import annotations

# Created by shiyang07ca at 2024/06/02 02:40
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies/
from typing import Counter

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        cnt = len(Counter(candyType).keys())
        n = len(candyType) // 2
        return cnt if cnt < n else n


# @lc code=end

if __name__ == "__main__":
    candyType: list[int] = deserialize("List[int]", read_line())
    ans = Solution().distributeCandies(candyType)
    print("\noutput:", serialize(ans, "integer"))
