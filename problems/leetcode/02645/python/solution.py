# Created by shiyang07ca at 2024/01/11 21:30
# leetgo: dev
# https://leetcode.cn/problems/minimum-additions-to-make-valid-string/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def addMinimum1(self, word: str) -> int:
        ans = i = 0
        N = len(word)
        while True:
            if i >= N:
                break

            if i + 3 <= N:
                if word[i : i + 3] == "abc":
                    i += 3
                    continue

            if i + 2 <= N:
                if word[i : i + 2] in ("ab", "bc", "ac"):
                    i += 2
                    ans += 1
                    continue

            i += 1
            ans += 2

        return ans

    def addMinimum(self, s: str) -> int:
        t = 1 + sum(x >= y for x, y in pairwise(s))
        return t * 3 - len(s)


# @lc code=end

if __name__ == "__main__":
    word: str = deserialize("str", read_line())
    ans = Solution().addMinimum(word)

    print("\noutput:", serialize(ans))
