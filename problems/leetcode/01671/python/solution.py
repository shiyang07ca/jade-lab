# Created by shiyang07ca at 2023/12/22 11:57
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/solutions/2575540/python3javacgorust-yi-ti-yi-jie-dong-tai-wtkr/?envType=daily-question&envId=2023-12-22
    def minimumMountainRemovals1(self, nums: List[int]) -> int:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)
        return n - max(a + b - 1 for a, b in zip(left, right) if a > 1 and b > 1)

    # 链接：https://leetcode.cn/problems/minimum-number-of-removals-to-make-mountain-array/solutions/2575527/qian-hou-zhui-fen-jie-zui-chang-di-zeng-9vowl/
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        suf = [0] * n
        g = []
        for i in range(n - 1, 0, -1):
            x = nums[i]
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            suf[i] = j + 1  # 从 nums[i] 开始的最长严格递减子序列的长度

        mx = 0  # 最长山形子序列的长度
        g = []
        for i, x in enumerate(nums):
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            pre = j + 1  # 在 nums[i] 结束的最长严格递增子序列的长度
            if pre >= 2 and suf[i] >= 2:
                mx = max(mx, pre + suf[i] - 1)  # 减去重复的 nums[i]
        return n - mx


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minimumMountainRemovals(nums)

    print("\noutput:", serialize(ans))
