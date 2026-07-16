# Created by shiyang07ca at 2023/07/06 09:21
# leetgo: dev
# https://leetcode.cn/problems/maximum-split-of-positive-even-integers/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: greedy


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2:
            return []
        ans = []
        i = 2
        while i <= finalSum:
            finalSum -= i
            ans.append(i)
            i += 2
        ans[-1] += finalSum
        return ans


# @lc code=end

if __name__ == "__main__":
    finalSum: int = deserialize("int", read_line())
    ans = Solution().maximumEvenSplit(finalSum)

    print("\noutput:", serialize(ans))
