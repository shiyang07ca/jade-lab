# Created by shiyang07ca at 2024/04/20 13:54
# leetgo: dev
# https://leetcode.cn/problems/combination-sum/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i, target):
            if target == 0:  # 找到答案
                ans.append(path[:])
                return

            if i == len(candidates) or target < candidates[i]:
                return

            path.append(candidates[i])  # 选
            dfs(i, target - candidates[i])
            path.pop()  # 恢复现场

            dfs(i + 1, target)  # 不选

        dfs(0, target)
        return ans

    # 链接：https://leetcode.cn/problems/combination-sum/solutions/2747858/liang-chong-fang-fa-xuan-huo-bu-xuan-mei-mhf9/
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(i: int, left: int) -> None:
            if left == 0:
                # 找到一个合法组合
                ans.append(path.copy())
                return

            if left < candidates[i]:
                return

            # 枚举选哪个
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                dfs(j, left - candidates[j])
                path.pop()  # 恢复现场

        dfs(0, target)
        return ans


# @lc code=end

if __name__ == "__main__":
    candidates: List[int] = deserialize("List[int]", read_line())
    target: int = deserialize("int", read_line())
    ans = Solution().combinationSum(candidates, target)
    print("\noutput:", serialize(ans, "integer[][]"))
