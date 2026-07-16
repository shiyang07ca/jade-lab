# Created by shiyang07ca at 2023/08/01 13:29
# leetgo: dev
# https://leetcode.cn/problems/power-of-heroes/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO


class Solution:
    # 链接：https://leetcode.cn/problems/power-of-heroes/solutions/2268792/gong-xian-fa-pythonjavacgo-by-endlessche-d4jx/
    def sumOfPower(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        nums.sort()
        ans = s = 0
        for x in nums:  # x 作为最大值
            ans = (ans + x * x * (x + s)) % MOD
            s = (s * 2 + x) % MOD  # 递推计算下一个 s
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().sumOfPower(nums)

    print("\noutput:", serialize(ans))
