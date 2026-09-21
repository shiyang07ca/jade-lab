from __future__ import annotations

# Created by shiyang07ca at 2023/11/10 10:35
# leetgo: dev
# https://leetcode.cn/problems/successful-pairs-of-spells-and-potions/
from bisect import bisect_left

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def successfulPairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]:
        potions.sort()
        ans = [0] * len(spells)
        for i, s in enumerate(spells):
            ans[i] = len(potions) - bisect_left(potions, success / s)
        return ans


# @lc code=end

if __name__ == "__main__":
    spells: list[int] = deserialize("List[int]", read_line())
    potions: list[int] = deserialize("List[int]", read_line())
    success: int = deserialize("int", read_line())
    ans = Solution().successfulPairs(spells, potions, success)

    print("\noutput:", serialize(ans))
