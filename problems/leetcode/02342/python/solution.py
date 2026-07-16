# Created by shiyang07ca at 2023/11/18 00:22
# leetgo: dev
# https://leetcode.cn/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def compute(n):
            ans = 0
            while n:
                ans += n % 10
                n //= 10
            return ans

        cnt = defaultdict(list)
        for n in nums:
            c = compute(n)
            heappush(cnt[c], -n)

        ans = -1
        for h in cnt.values():
            if len(h) >= 2:
                ans = max(ans, -heappop(h) - heappop(h))
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maximumSum(nums)

    print("\noutput:", serialize(ans))
