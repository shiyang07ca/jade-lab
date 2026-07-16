# Created by shiyang07ca at 2024/11/05 13:36
# leetgo: 1.4.10
# https://leetcode.cn/problems/find-the-winning-player-in-coin-game/

from typing import *
from leetgo_py import *

# @lc code=begin

class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        pass

# @lc code=end

if __name__ == "__main__":
    x: int = deserialize("int", read_line())
    y: int = deserialize("int", read_line())
    ans = Solution().losingPlayer(x, y)
    print("\noutput:", serialize(ans, "string"))
