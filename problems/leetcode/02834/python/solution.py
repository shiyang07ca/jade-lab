# Created by shiyang07ca at 2024/03/09 14:58
# leetgo: dev
# https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Math


class Solution:
    # 链接：https://leetcode.cn/problems/find-the-minimum-possible-sum-of-a-beautiful-array/solutions/
    def minimumPossibleSum(self, n: int, k: int) -> int:
        m = min(k // 2, n)
        return (m * (m + 1) + (k * 2 + n - m - 1) * (n - m)) // 2 % 1_000_000_007


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().minimumPossibleSum(n, target)

    print("\noutput:", serialize(ans))
