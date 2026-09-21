from __future__ import annotations

# Created by shiyang07ca at 2023/10/19 00:01
# leetgo: dev
# https://leetcode.cn/problems/tuple-with-same-product/
from typing import Counter

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        cnt = Counter()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cnt[nums[i] * nums[j]] += 1
        return sum(n * (n - 1) // 2 for n in cnt.values()) * 8


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().tupleSameProduct(nums)

    print("\noutput:", serialize(ans))
