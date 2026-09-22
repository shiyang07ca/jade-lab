# Created by shiyang07ca at 2026/09/22 19:41
# leetgo: 1.4.17
# https://leetcode.cn/problems/longest-palindromic-substring/

from typing import *

from leetgo_py import *

# @lc code=begin

# TODO
# https://leetcode.cn/problems/longest-palindromic-substring/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        # 奇数
        for i in range(len(s)):
            lo = hi = i
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > right - left:
                left, right = lo + 1, hi  # 左闭右开区间

        # 偶数
        for i in range(len(s) - 1):
            lo, hi = i, i + 1
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            if hi - lo - 1 > right - left:
                left, right = lo + 1, hi  # 左闭右开区间

        return s[left:right]

# @lc code=end

if __name__ == "__main__":
    s: str = deserialize("str", read_line())
    ans = Solution().longestPalindrome(s)
    print("\noutput:", serialize(ans, "string"))
