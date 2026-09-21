from __future__ import annotations

# Created by shiyang07ca at 2024/06/01 21:46
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies-among-children-i/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        ans += 1
        return ans


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(n, limit)
    print("\noutput:", serialize(ans, "integer"))
