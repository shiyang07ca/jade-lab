from __future__ import annotations

# Created by shiyang07ca at 2023/12/18 00:23
# leetgo: dev
# https://leetcode.cn/problems/find-peak-element/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        # 与 binary_search.py 的 first_true 不同：这里不是找单调条件的第一个真。
        # 上下坡可以交替出现；只需保留至少一个峰值，不要求保留所有峰值。
        # 候选区间是闭区间 [left, right]，数组外的相邻值在数学上视为负无穷。
        # 不变量：左端比左邻居高，右端比右邻居高，因此区间内一定存在峰值。
        left, right = 0, len(nums) - 1
        while left < right:
            # 向下取整；left < right 保证 mid < right，所以 mid + 1 不越界。
            mid = (left + right) >> 1
            if nums[mid] > nums[mid + 1]:
                # 下坡：mid 成为新右端，仍满足右端比右邻居高。
                # [left, mid] 内一定有峰值，mid 本身也可能是峰值，不能排除。
                right = mid
            else:
                # 相邻元素不相等，因此这里必为上坡。
                # mid + 1 成为新左端，比左邻居高，右侧区间一定有峰值。
                # 左侧也可能有峰值，但题目只要求返回任意一个，可以舍弃。
                left = mid + 1

        return left


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    ans = Solution().findPeakElement(nums)

    print("\noutput:", serialize(ans))
