# Created by shiyang07ca at 2026/09/19 01:31
# leetgo: 1.4.17
# https://leetcode.cn/problems/minimum-size-subarray-sum/

from typing import *

from leetgo_py import *

# @lc code=begin


# 链接：https://leetcode.cn/problems/minimum-size-subarray-sum/solutions/1959532/biao-ti-xia-biao-zong-suan-cuo-qing-kan-k81nh/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1  # 也可以写 inf
        s = left = 0
        for right, x in enumerate(nums):  # 枚举子数组右端点
            s += x
            while s - nums[left] >= target:  # 尽量缩小子数组长度
                s -= nums[left]
                left += 1  # 左端点右移
            if s >= target:
                ans = min(ans, right - left + 1)
        return ans if ans <= n else 0


# @lc code=end

if __name__ == "__main__":
    target: int = deserialize("int", read_line())
    nums: List[int] = deserialize("List[int]", read_line())
    ans = Solution().minSubArrayLen(target, nums)
    print("\noutput:", serialize(ans, "integer"))
