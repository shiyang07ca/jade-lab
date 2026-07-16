# Created by shiyang07ca at 2024/04/28 09:21
# leetgo: dev
# https://leetcode.cn/problems/convert-to-base-2/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # def baseNeg2(self, n: int) -> str:
    #     if n == 0: return '0'
    #     if n == 1: return '1'
    #     if n & 1:
    #         return self.baseNeg2((n - 1) // -2) + '1'
    #     else:
    #         return self.baseNeg2(n // -2) + '0'

    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"

        res = ""
        while n != 0:
            remainder = n % (-2)
            n //= -2
            if remainder < 0:
                remainder += 2
                n += 1
            res = str(remainder) + res

        return res


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().baseNeg2(n)
    print("\noutput:", serialize(ans, "string"))
