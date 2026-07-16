# Created by shiyang07ca at 2024/03/20 19:02
# leetgo: dev
# https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# [50. Pow (x, n) - 力扣（LeetCode）](https://leetcode.cn/problems/powx-n/description/)


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/solutions/936621/tan-xin-ji-qi-shu-xue-zheng-ming-by-endl-uumv/
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1_000_000_007
        k = (1 << p) - 1
        return k * pow(k - 1, k >> 1, MOD) % MOD


# @lc code=end

if __name__ == "__main__":
    p: int = deserialize("int", read_line())
    ans = Solution().minNonZeroProduct(p)

    print("\noutput:", serialize(ans))
