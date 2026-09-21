from __future__ import annotations

# Created by shiyang07ca at 2023/10/14 00:02
# leetgo: dev
# https://leetcode.cn/problems/single-number/
from typing import Counter

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        cnt = Counter(nums)
        for n, c in cnt.items():
            if c == 1:
                return n
        raise ValueError("no unique number")


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().singleNumber(nums)

    print("\noutput:", serialize(ans))
