from __future__ import annotations

# Created by shiyang07ca at 2024/02/04 21:10
# leetgo: dev
# https://leetcode.cn/problems/nim-game/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def canWinNim(self, n: int) -> bool:
        return not (n % 4 == 0)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().canWinNim(n)

    print("\noutput:", serialize(ans))
