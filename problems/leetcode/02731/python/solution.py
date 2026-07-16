# Created by shiyang07ca at 2023/10/10 00:02
# leetgo: dev
# https://leetcode.cn/problems/movement-of-robots/

from itertools import *
from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def sumDistance1(self, nums: List[int], s: str, d: int) -> int:
        MOD = 10**9 + 7
        pos = []
        for i, n in enumerate(nums):
            if s[i] == "L":
                pos.append(n - d)
            else:
                pos.append(n + d)
        pos.sort()
        ans = 0
        n = len(nums)
        for i, (a, b) in zip(range(n), pairwise(pos)):
            ans = (ans + (i + 1) * (n - i - 1) * (b - a)) % MOD
        return ans

    # 链接：https://leetcode.cn/problems/movement-of-robots/description/
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        mod = 10**9 + 7
        for i, c in enumerate(s):
            nums[i] += d if c == "R" else -d
        nums.sort()
        ans = pre = 0
        for i, x in enumerate(nums):
            ans += i * x - pre
            pre += x
        return ans % mod


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    s: str = deserialize("str", read_line())
    d: int = deserialize("int", read_line())
    ans = Solution().sumDistance(nums, s, d)

    print("\noutput:", serialize(ans))
