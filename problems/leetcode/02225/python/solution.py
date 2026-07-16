# Created by shiyang07ca at 2024/05/22 23:50
# leetgo: dev
# https://leetcode.cn/problems/find-players-with-zero-or-one-losses/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/find-players-with-zero-or-one-losses/solutions/1391108/ha-xi-biao-mo-ni-by-endlesscheng-6p09/
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set(x for m in matches for x in m)
        loss_count = Counter(loser for _, loser in matches)
        return [
            sorted(x for x in players if x not in loss_count),
            sorted(x for x, c in loss_count.items() if c == 1),
        ]


# @lc code=end

if __name__ == "__main__":
    matches: List[List[int]] = deserialize("List[List[int]]", read_line())
    ans = Solution().findWinners(matches)
    print("\noutput:", serialize(ans, "integer[][]"))
