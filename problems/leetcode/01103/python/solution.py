# Created by shiyang07ca at 2024/06/03 23:29
# leetgo: dev
# https://leetcode.cn/problems/distribute-candies-to-people/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        c = i = 0
        ans = [0] * num_people
        while candies > 0:
            c += 1
            if c <= candies:
                ans[i] += c
                candies -= c
            else:
                ans[i] += candies
                candies = 0
            i = (i + 1) % num_people
        return ans


# @lc code=end

if __name__ == "__main__":
    candies: int = deserialize("int", read_line())
    num_people: int = deserialize("int", read_line())
    ans = Solution().distributeCandies(candies, num_people)
    print("\noutput:", serialize(ans, "integer[]"))
