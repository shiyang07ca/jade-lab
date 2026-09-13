from __future__ import annotations

# Created by shiyang07ca at 2024/05/24 22:18
# leetgo: dev
# https://leetcode.cn/problems/find-the-most-competitive-subsequence/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-the-most-competitive-subsequence/solutions/2789156/letmefly-1673zhao-chu-zui-ju-jing-zheng-dihu5/
    def mostCompetitive(self, nums: list[int], k: int) -> list[int]:
        st = []
        for i in range(len(nums)):
            while st and st[-1] > nums[i] and (len(st) - 1) + (len(nums) - i) >= k:
                st.pop()
            if len(st) < k:
                st.append(nums[i])
        return st


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().mostCompetitive(nums, k)
    print("\noutput:", serialize(ans, "integer[]"))
