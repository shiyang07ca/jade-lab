# Created by shiyang07ca at 2024/05/28 00:03
# leetgo: dev
# https://leetcode.cn/problems/find-the-peaks/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def findPeaks(self, m: List[int]) -> List[int]:
        ans = []
        for i in range(1, len(m) - 1):
            if m[i - 1] < m[i] > m[i + 1]:
                ans.append(i)
        return ans


# @lc code=end

if __name__ == "__main__":
    mountain: List[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeaks(mountain)
    print("\noutput:", serialize(ans, "integer[]"))
