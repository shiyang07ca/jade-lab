# Created by shiyang07ca at 2024/03/28 22:44
# leetgo: dev
# https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: dp


class Solution:
    # 链接：https://leetcode.cn/problems/first-day-where-you-have-been-in-all-the-rooms/solutions/979221/qian-zhui-he-you-hua-dp-by-endlesscheng-j10b/
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        s = [0] * len(nextVisit)
        for i, j in enumerate(nextVisit[:-1]):
            s[i + 1] = (s[i] * 2 - s[j] + 2) % 1_000_000_007
        return s[-1]


# @lc code=end

if __name__ == "__main__":
    nextVisit: List[int] = deserialize("List[int]", read_line())
    ans = Solution().firstDayBeenInAllRooms(nextVisit)

    print("\noutput:", serialize(ans))
