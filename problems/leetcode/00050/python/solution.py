# Created by shiyang07ca at 2024/11/09 16:12
# leetgo: 1.4.10
# https://leetcode.cn/problems/powx-n/

from typing import *
from leetgo_py import *

# @lc code=begin


# TODO
# tag: math, 快速幂
class Solution:
    # 链接：https://leetcode.cn/problems/powx-n/solutions/2858114/tu-jie-yi-zhang-tu-miao-dong-kuai-su-mi-ykp3i/
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:  # x^-n = (1/x)^n
            n = -n
            x = 1 / x
        while n:  # 从低到高枚举 n 的每个比特位
            if n & 1:  # 这个比特位是 1
                ans *= x  # 把 x 乘到 ans 中
            x *= x  # x 自身平方
            n >>= 1  # 继续枚举下一个比特位
        return ans


# @lc code=end

if __name__ == "__main__":
    x: float = deserialize("float", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().myPow(x, n)
    print("\noutput:", serialize(ans, "double"))
