# Created by shiyang07ca at 2024/03/10 00:33
# leetgo: dev
# https://leetcode.cn/problems/bulls-and-cows/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x = y = 0
        cnt1 = Counter(secret)
        cnt2 = Counter(guess)
        for i, s in enumerate(secret):
            if s == guess[i]:
                x += 1
                cnt1[s] -= 1
                cnt2[s] -= 1
        for s, cnt in cnt1.items():
            if cnt > 0 and cnt2[s] > 0:
                y += min(cnt, cnt2[s])
        return f"{x}A{y}B"


# @lc code=end

if __name__ == "__main__":
    secret: str = deserialize("str", read_line())
    guess: str = deserialize("str", read_line())
    ans = Solution().getHint(secret, guess)

    print("\noutput:", serialize(ans))
