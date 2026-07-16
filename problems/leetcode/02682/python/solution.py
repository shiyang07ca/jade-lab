# Created by shiyang07ca at 2023/08/16 00:41
# leetgo: dev
# https://leetcode.cn/problems/find-the-losers-of-the-circular-game/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt = Counter([0])
        s = 0
        i = 1
        while cnt[s] <= 1:
            s = (s + i * k) % n
            cnt[s] += 1
            i += 1
        return [i + 1 for i in range(n) if cnt[i] == 0]


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().circularGameLosers(n, k)

    print("\noutput:", serialize(ans))
