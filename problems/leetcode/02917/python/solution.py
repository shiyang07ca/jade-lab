from __future__ import annotations

# Created by shiyang07ca at 2024/03/06 13:34
# leetgo: dev
# https://leetcode.cn/problems/find-the-k-or-of-an-array/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        bits = max(nums).bit_length()
        ans = 0
        for b in range(bits):
            t = 0
            for n in nums:
                if n >> b & 1:
                    t += 1
            if t >= k:
                ans += 1 << b
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().findKOr(nums, k)

    print("\noutput:", serialize(ans))
