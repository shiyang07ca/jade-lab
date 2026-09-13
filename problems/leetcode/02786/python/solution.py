from __future__ import annotations

from functools import cache

# Created by shiyang07ca at 2024/06/14 23:57
# leetgo: dev
# https://leetcode.cn/problems/visit-array-positions-to-maximize-score/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/visit-array-positions-to-maximize-score/solutions/2810386/jiao-ni-yi-bu-bu-si-kao-dpcong-ji-yi-hua-jhvr/
    def maxScore(self, nums: list[int], x: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int, j: int) -> int:
            if i == len(nums):
                return 0
            if nums[i] % 2 != j:
                return dfs(i + 1, j)
            return max(dfs(i + 1, j), dfs(i + 1, j ^ 1) - x) + nums[i]

        return dfs(0, nums[0] % 2)


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    x: int = deserialize("int", read_line())
    ans = Solution().maxScore(nums, x)
    print("\noutput:", serialize(ans, "long"))
