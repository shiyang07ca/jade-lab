from __future__ import annotations

# Created by shiyang07ca at 2024/06/10 23:57
# leetgo: dev
# https://leetcode.cn/problems/boats-to-save-people/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort(reverse=True)
        left = 0
        right = len(people) - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                right -= 1
            ans += 1
            left += 1

        return ans


# @lc code=end

if __name__ == "__main__":
    people: list[int] = deserialize("List[int]", read_line())
    limit: int = deserialize("int", read_line())
    ans = Solution().numRescueBoats(people, limit)
    print("\noutput:", serialize(ans, "integer"))
