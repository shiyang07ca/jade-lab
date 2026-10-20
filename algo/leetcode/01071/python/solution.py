# Created by shiyang07ca at 2026/10/21 00:49
# leetgo: 1.4.17
# https://leetcode.cn/problems/greatest-common-divisor-of-strings/

from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 拼接顺序不影响结果，才存在公共重复单位。
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(a: int, b: int) -> int:
            # 辗转相除法：gcd(a, b) = gcd(b, a % b)。
            while b != 0:
                a, b = b, a % b
            return a

        # 最长公共因子的长度等于两串长度的最大公约数。
        return str1[:gcd(len(str1), len(str2))]


# @lc code=end

if __name__ == "__main__":
    str1: str = deserialize("str", read_line())
    str2: str = deserialize("str", read_line())
    ans = Solution().gcdOfStrings(str1, str2)
    print("\noutput:", serialize(ans, "string"))
