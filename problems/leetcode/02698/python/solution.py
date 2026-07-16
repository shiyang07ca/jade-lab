# Created by shiyang07ca at 2023/10/25 13:15
# leetgo: dev
# https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/

from typing import *
from leetgo_py import *

# @lc code=begin


def find(n):
    @cache
    def dfs(i, t):
        if t < 0 or int(ns[i:]) < t:
            return 0
        if int(ns[i:]) == t:
            return 1

        for j in range(i + 1, len(ns)):
            if dfs(j, t - int(ns[i:j])):
                return 1
        return 0

    ns = str(n * n)
    return dfs(0, n)


ans = [0] * 1001
for i in range(1, 1001):
    ans[i] = i * i if find(i) else 0


class Solution:
    def punishmentNumber(self, n: int) -> int:
        return sum(ans[: n + 1])


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().punishmentNumber(n)

    print("\noutput:", serialize(ans))
