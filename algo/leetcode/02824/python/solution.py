from __future__ import annotations

# Created by shiyang07ca at 2023/11/24 13:27
# leetgo: dev
# https://leetcode.cn/problems/count-pairs-whose-sum-is-less-than-target/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] < target:
                    ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().countPairs(nums, target)

    print("\noutput:", serialize(ans))
