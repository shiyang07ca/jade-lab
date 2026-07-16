# Created by shiyang07ca at 2023/12/26 13:25
# leetgo: dev
# https://leetcode.cn/problems/longest-increasing-subsequence/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 作者：灵茶山艾府
    # 链接：https://leetcode.cn/problems/longest-increasing-subsequence/solutions/2147040/jiao-ni-yi-bu-bu-si-kao-dpfu-o1-kong-jia-4zma/
    def lengthOfLIS1(self, nums: List[int]) -> int:
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        return max(dfs(i) for i in range(len(nums)))

    def lengthOfLIS(self, nums: List[int]) -> int:
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):  # >=x 的 g[j] 不存在
                g.append(x)
            else:
                g[j] = x
        return len(g)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().lengthOfLIS(nums)

    print("\noutput:", serialize(ans))
