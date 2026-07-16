# Created by shiyang07ca at 2023/08/22 08:34
# leetgo: dev
# https://leetcode.cn/problems/maximize-distance-to-closest-person/

from typing import *
from leetgo_py import *

# @lc code=begin

# tag: 前后缀分解


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        li, ri = 0, n - 1
        l, r = [inf] * n, [inf] * n
        for i, s in enumerate(seats):
            if s == 0 and i != li:
                l[i] = i - li
            elif s == 1:
                li = i
        for i in range(n - 1, -1, -1):
            if seats[i] == 0 and i != ri:
                r[i] = ri - i
            elif seats[i] == 1:
                ri = i

        return max(min(a, b) for i, (a, b) in enumerate(zip(l, r)) if seats[i] == 0)

    # 链接：https://leetcode.cn/problems/maximize-distance-to-closest-person/solutions/2399061/python3javago-qian-hou-zhui-fen-jie-by-x-1k2b/
    def maxDistToClosest2(self, seats: List[int]) -> int:
        n = len(seats)
        suffix = [inf] * (n + 1)
        for i in range(n - 1, -1, -1):
            x = seats[i]
            if x == 1:
                suffix[i] = i
            else:
                suffix[i] = suffix[i + 1]

        j = -inf
        res = 0
        for i, x in enumerate(seats):
            if x == 1:
                j = i
                continue
            res = max(res, min(i - j, suffix[i] - i))
        return res


# @lc code=end

if __name__ == "__main__":
    seats: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxDistToClosest(seats)

    print("\noutput:", serialize(ans))
