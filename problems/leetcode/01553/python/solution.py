# Created by shiyang07ca at 2024/05/12 00:10
# leetgo: dev
# https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/solutions/2773476/liang-chong-fang-fa-ji-yi-hua-sou-suo-zu-18jv/
    def minDays(self, n: int) -> int:
        @cache  # 缓存装饰器，避免重复计算 dfs 的结果（记忆化）
        def dfs(i: int) -> int:
            if i <= 1:
                return i
            return min(dfs(i // 2) + i % 2, dfs(i // 3) + i % 3) + 1

        return dfs(n)


# @lc code=end

if __name__ == "__main__":
    n: int = deserialize("int", read_line())
    ans = Solution().minDays(n)
    print("\noutput:", serialize(ans, "integer"))
