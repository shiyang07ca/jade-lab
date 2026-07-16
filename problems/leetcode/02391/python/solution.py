# Created by shiyang07ca at 2024/05/11 00:10
# leetgo: dev
# https://leetcode.cn/problems/minimum-amount-of-time-to-collect-garbage/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = 0
        p_i, m_i, g_i = 0, 0, 0
        for index, gar in enumerate(garbage):
            cp = gar.count("P")
            cm = gar.count("M")
            cg = gar.count("G")
            if cp:
                ans += sum(travel[p_i:index]) + cp
                p_i = index
            if cm:
                ans += sum(travel[m_i:index]) + cm
                m_i = index
            if cg:
                ans += sum(travel[g_i:index]) + cg
                g_i = index

        return ans


# @lc code=end

if __name__ == "__main__":
    garbage: List[str] = deserialize("List[str]", read_line())
    travel: List[int] = deserialize("List[int]", read_line())
    ans = Solution().garbageCollection(garbage, travel)
    print("\noutput:", serialize(ans, "integer"))
