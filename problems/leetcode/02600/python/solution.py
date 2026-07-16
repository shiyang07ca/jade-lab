# Created by shiyang07ca at 2023/07/05 13:19
# leetgo: dev
# https://leetcode.cn/problems/k-items-with-the-maximum-sum/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        return sum(([1] * numOnes + [0] * numZeros + [-1] * numNegOnes)[:k])


# @lc code=end

if __name__ == "__main__":
    numOnes: int = deserialize("int", read_line())
    numZeros: int = deserialize("int", read_line())
    numNegOnes: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k)

    print("\noutput:", serialize(ans))
