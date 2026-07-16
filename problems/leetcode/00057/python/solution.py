# Created by shiyang07ca at 2023/08/28 13:01
# leetgo: dev
# https://leetcode.cn/problems/insert-interval/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def insert1(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        ans = [intervals[0]]
        for a, b in intervals[1:]:
            if a <= ans[-1][1]:
                ans[-1] = [ans[-1][0], max(ans[-1][1], b)]
            else:
                ans.append([a, b])
        return ans

    # 链接：https://leetcode.cn/problems/insert-interval/solutions/2414501/python3javacgotypescript-yi-ti-shuang-ji-2fsw/
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        st, ed = newInterval
        ans = []
        insert = False
        for s, e in intervals:
            if ed < s:
                if not insert:
                    ans.append([st, ed])
                    insert = True
                ans.append([s, e])
            elif e < st:
                ans.append([s, e])
            else:
                st = min(st, s)
                ed = max(ed, e)
        if not insert:
            ans.append([st, ed])
        return ans


# @lc code=end

if __name__ == "__main__":
    intervals: List[List[int]] = deserialize("List[List[int]]", read_line())
    newInterval: List[int] = deserialize("List[int]", read_line())
    ans = Solution().insert(intervals, newInterval)

    print("\noutput:", serialize(ans))
