# Created by shiyang07ca at 2024/04/21 12:23
# leetgo: dev
# https://leetcode.cn/problems/combination-sum-iii/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def combinationSum31(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, left):
            if left == 0 and len(path) == k:
                ans.append(path[:])
                return

            if i == 10 or left < i:
                return

            path.append(i)
            dfs(i + 1, left - i)
            path.pop()

            dfs(i + 1, left)

        dfs(1, n)
        return ans

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(i, left):
            if left == 0 and len(path) == k:
                ans.append(path[:])
                return

            if len(path) > k or left < i:
                return

            for j in range(i + 1, 10):
                path.append(j)
                dfs(j, left - j)
                path.pop()

        dfs(0, n)
        return ans


# @lc code=end

if __name__ == "__main__":
    k: int = deserialize("int", read_line())
    n: int = deserialize("int", read_line())
    ans = Solution().combinationSum3(k, n)
    print("\noutput:", serialize(ans, "integer[][]"))
