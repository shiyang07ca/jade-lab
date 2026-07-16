# Created by shiyang07ca at 2024/03/09 13:14
# leetgo: dev
# https://leetcode.cn/problems/find-the-k-sum-of-an-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/find-the-k-sum-of-an-array/solutions/1764389/zhuan-huan-dui-by-endlesscheng-8yiq/
    def kSum(self, nums: List[int], k: int) -> int:
        s = 0
        for i, x in enumerate(nums):
            if x >= 0:
                s += x
            else:
                nums[i] = -x
        nums.sort()

        def check(sum_limit: int) -> bool:
            cnt = 1  # 空子序列算一个

            def dfs(i: int, s: int) -> None:
                nonlocal cnt
                if cnt == k or i == len(nums) or s + nums[i] > sum_limit:
                    return
                cnt += 1  # s + nums[i] <= sum_limit
                dfs(i + 1, s + nums[i])  # 选
                dfs(i + 1, s)  # 不选

            dfs(0, 0)
            return cnt == k  # 找到 k 个元素和不超过 sum_limit 的子序列

        return s - bisect_left(range(sum(nums)), True, key=check)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kSum(nums, k)

    print("\noutput:", serialize(ans))
