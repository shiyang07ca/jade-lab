# Created by shiyang07ca at 2024/05/27 00:01
# leetgo: dev
# https://leetcode.cn/problems/find-missing-observations/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        tot = mean * (len(rolls) + n)
        diff = tot - sum(rolls)
        if diff < n or diff > n * 6:
            return []

        ans = [diff // n] * n
        diff = diff - sum(ans)
        i = 0
        while diff:
            ans[i] += 1
            diff -= 1
            i = (i + 1) % n
        return ans


# @lc code=end

if __name__ == "__main__":
    rolls: List[int] = deserialize("List[int]", read_line())
    mean: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().missingRolls(rolls, mean, n)
    print("\noutput:", serialize(ans, "integer[]"))
