from __future__ import annotations

# Created by shiyang07ca at 2023/07/15 18:26
# leetgo: dev
# https://leetcode.cn/problems/4sum/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO


# 链接：https://leetcode.cn/problems/4sum/solutions/2344523/python3javacgo-yi-ti-yi-jie-pai-xu-shuan-wy6n/
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        ans = []
        if n < 4:
            return ans
        nums.sort()
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, n - 1
                while k < l:
                    x = nums[i] + nums[j] + nums[k] + nums[l]
                    if x < target:
                        k += 1
                    elif x > target:
                        l -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        k, l = k + 1, l - 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return ans


# @lc code=end

if __name__ == "__main__":
    nums: list[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().fourSum(nums, target)

    print("\noutput:", serialize(ans))
