# Created by shiyang07ca at 2023/12/27 00:14
# leetgo: dev
# https://leetcode.cn/problems/determine-the-winner-of-a-bowling-game/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def count(p):
            ans = 0
            for i, x in enumerate(p):
                if (i > 0 and p[i - 1] == 10) or (i > 1 and p[i - 2] == 10):
                    ans += 2 * x
                else:
                    ans += x
            return ans

        c1, c2 = count(player1), count(player2)
        if c1 > c2:
            return 1
        elif c1 < c2:
            return 2
        else:
            return 0


# @lc code=end

if __name__ == "__main__":
    player1: List[int] = deserialize("List[int]", read_line())
    player2: List[int] = deserialize("List[int]", read_line())
    ans = Solution().isWinner(player1, player2)

    print("\noutput:", serialize(ans))
