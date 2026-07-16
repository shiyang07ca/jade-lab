# Created by shiyang07ca at 2023/10/13 00:01
# leetgo: dev
# https://leetcode.cn/problems/avoid-flood-in-the-city/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: binary search

from sortedcontainers import SortedList


class Solution:
    # 链接：https://leetcode.cn/problems/avoid-flood-in-the-city/
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        sunny = SortedList()
        rainy = {}
        for i, v in enumerate(rains):
            if v:
                if v in rainy:
                    idx = sunny.bisect_right(rainy[v])
                    if idx == len(sunny):
                        return []
                    ans[sunny[idx]] = v
                    sunny.discard(sunny[idx])
                rainy[v] = i
            else:
                sunny.add(i)
                ans[i] = 1
        return ans


# @lc code=end

if __name__ == "__main__":
    rains: List[int] = deserialize("List[int]", read_line())
    ans = Solution().avoidFlood(rains)

    print("\noutput:", serialize(ans))
