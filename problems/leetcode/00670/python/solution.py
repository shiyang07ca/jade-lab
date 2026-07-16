# Created by shiyang07ca at 2024/01/22 12:38
# leetgo: dev
# https://leetcode.cn/problems/maximum-swap/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumSwap1(self, num: int) -> int:
        nums = []
        while num:
            nums.insert(0, num % 10)
            num //= 10

        sns = sorted(nums, reverse=True)
        ans = nums
        for i, n in enumerate(nums):
            if sns[i] != n:
                ans[i] = sns[i]
                for j in range(len(nums) - 1, i, -1):
                    if sns[i] == ans[j]:
                        ans[j] = n
                        return int("".join(str(n) for n in ans))
        return int("".join(str(n) for n in ans))

    def maximumSwap(self, num: int) -> int:
        s = str(num)
        max_idx = len(s) - 1
        p = q = -1
        for i in range(len(s) - 2, -1, -1):
            if s[i] > s[max_idx]:  # s[i] 是目前最大数字
                max_idx = i
            elif s[i] < s[max_idx]:  # s[i] 右边有比它大的
                p, q = i, max_idx  # 更新 p 和 q
        if p == -1:  # 这意味着 s 是降序的
            return num
        s = list(s)
        s[p], s[q] = s[q], s[p]  # 交换 s[p] 和 s[q]
        return int("".join(s))


# @lc code=end

if __name__ == "__main__":
    num: int = deserialize("int", read_line())
    ans = Solution().maximumSwap(num)

    print("\noutput:", serialize(ans))
