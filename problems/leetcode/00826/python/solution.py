# Created by shiyang07ca at 2024/05/17 00:02
# leetgo: dev
# https://leetcode.cn/problems/most-profit-assigning-work/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/most-profit-assigning-work/solutions/2780326/pai-xu-shuang-zhi-zhen-pythonjavacgojsru-gthg/
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        jobs = sorted(zip(difficulty, profit))
        worker.sort()
        ans = j = max_profit = 0
        for w in worker:
            while j < len(jobs) and jobs[j][0] <= w:
                max_profit = max(max_profit, jobs[j][1])
                j += 1
            ans += max_profit
        return ans


# @lc code=end

if __name__ == "__main__":
    difficulty: List[int] = deserialize("List[int]", read_line())
    profit: List[int] = deserialize("List[int]", read_line())
    worker: List[int] = deserialize("List[int]", read_line())
    ans = Solution().maxProfitAssignment(difficulty, profit, worker)
    print("\noutput:", serialize(ans, "integer"))
