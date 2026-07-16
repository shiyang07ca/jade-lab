# Created by shiyang07ca at 2024/01/21 21:38
# leetgo: dev
# https://leetcode.cn/problems/split-array-largest-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:
# tag: Binary Search


class Solution:
    # https://leetcode.cn/problems/split-array-largest-sum/solutions/2613046/er-fen-da-an-fu-ti-dan-pythonjavacgojsru-n5la/
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx):
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                else:
                    if cnt == k:
                        return False
                    cnt += 1
                    s = x

            return True

        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) >> 1
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().splitArray(nums, k)

    print("\noutput:", serialize(ans))
