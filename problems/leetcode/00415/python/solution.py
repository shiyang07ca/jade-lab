# Created by shiyang07ca at 2023/07/17 07:35
# leetgo: dev
# https://leetcode.cn/problems/add-strings/

from typing import *
from leetgo_py import *

# @lc code=begin


# 链接：https://leetcode.cn/problems/add-strings/solutions/12250/add-strings-shuang-zhi-zhen-fa-by-jyd/
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


# @lc code=end

if __name__ == "__main__":
    num1: str = deserialize("str", read_line())
    num2: str = deserialize("str", read_line())
    ans = Solution().addStrings(num1, num2)

    print("\noutput:", serialize(ans))
