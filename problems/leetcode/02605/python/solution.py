from __future__ import annotations

from sys import maxsize as inf

# Created by shiyang07ca at 2023/09/05 00:03
# leetgo: dev
# https://leetcode.cn/problems/form-smallest-number-from-two-digit-arrays/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def minNumber(self, nums1: list[int], nums2: list[int]) -> int:
        ans = inf
        for n in nums1:
            if n in nums2:
                ans = min(ans, n)
        if ans is not inf:
            return ans
        else:
            n1, n2 = min(nums1), min(nums2)
            return min(n1, n2) * 10 + max(n1, n2)


# @lc code=end

if __name__ == "__main__":
    nums1: list[int] = deserialize("List[int]", read_line())
    nums2: list[int] = deserialize("List[int]", read_line())
    ans = Solution().minNumber(nums1, nums2)

    print("\noutput:", serialize(ans))
