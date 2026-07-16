# Created by shiyang07ca at 2023/11/02 13:45
# leetgo: dev
# https://leetcode.cn/problems/rings-and-rods/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def countPoints(self, rings: str) -> int:
        cnt = defaultdict(set)
        for i in range(0, len(rings), 2):
            c, p = rings[i], rings[i + 1]
            cnt[p].add(c)
        return sum(1 if len(c) == 3 else 0 for c in cnt.values())


# @lc code=end

if __name__ == "__main__":
    rings: str = deserialize("str", read_line())
    ans = Solution().countPoints(rings)

    print("\noutput:", serialize(ans))
