# Created by shiyang07ca at 2023/12/13 23:31
# leetgo: dev
# https://leetcode.cn/problems/lexicographically-smallest-palindrome/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # https://leetcode.cn/problems/lexicographically-smallest-palindrome/solutions/2564425/python3javacgorust-yi-ti-yi-jie-tan-xin-yua0e/?envType=daily-question&envId=2023-12-13
    def makeSmallestPalindrome(self, s: str) -> str:
        cs = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            cs[i] = cs[j] = min(cs[i], cs[j])
            i, j = i + 1, j - 1
        return "".join(cs)


# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().makeSmallestPalindrome(s)

    print("\noutput:", serialize(ans))
