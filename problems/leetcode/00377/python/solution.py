# Created by shiyang07ca at 2024/04/22 00:02
# leetgo: dev
# https://leetcode.cn/problems/combination-sum-iv/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    # 链接：https://leetcode.cn/problems/combination-sum-iv/solutions/2706336/ben-zhi-shi-pa-lou-ti-cong-ji-yi-hua-sou-y52j/
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果
        def dfs(i: int) -> int:
            if i == 0:  # 爬完了
                return 1
            return sum(dfs(i - x) for x in nums if x <= i)  # 枚举所有可以爬的台阶数

        return dfs(target)


# @lc code=end

if __name__ == "__main__":
    nums: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum4(nums, target)
    print("\noutput:", serialize(ans, "integer"))
