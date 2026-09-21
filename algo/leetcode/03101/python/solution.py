from __future__ import annotations

# Created by shiyang07ca at 2024/07/06 00:02
# leetgo: dev
# https://leetcode.cn/problems/count-alternating-subarrays/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/count-alternating-subarrays/solutions/2716871/jian-ji-xie-fa-pythonjavacgo-by-endlessc-tcc9/
    def countAlternatingSubarrays(self, nums: list[int]) -> int:
        ans = cnt = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] != nums[i - 1]:
                cnt += 1
            else:
                cnt = 1
            ans += cnt  # 有 cnt 个右端点下标为 i 的交替子数组
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().countAlternatingSubarrays(nums)
    print("\noutput:", serialize(ans, "long"))
