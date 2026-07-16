# Created by shiyang07ca at 2024/01/02 00:13
# leetgo: dev
# https://leetcode.cn/problems/count-the-repetitions/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/count-the-repetitions/solutions/210588/yi-kan-jiu-neng-dong-de-ji-shu-fa-you-tu-you-zhen-/
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        dp = []
        for i in range(len(s2)):
            start = i
            end = 0
            for j in range(len(s1)):
                if s1[j] == s2[start]:
                    start += 1
                    if start == len(s2):
                        start = 0
                        end += 1
            dp.append((start, end))
        res = 0
        next = 0
        for _ in range(n1):
            res += dp[next][1]
            next = dp[next][0]
        return res // n2


# @lc code=end

if __name__ == "__main__":
    s1: str = deserialize("str", read_line())
    n1: int = deserialize("int", read_line())
    s2: str = deserialize("str", read_line())
    n2: int = deserialize("int", read_line())
    ans = Solution().getMaxRepetitions(s1, n1, s2, n2)

    print("\noutput:", serialize(ans))
