# Created by shiyang07ca at 2023/10/11 12:53
# leetgo: dev
# https://leetcode.cn/problems/reward-top-k-students/

from typing import *
from leetgo_py import *

# @lc code=begin


class Solution:
    def topStudents(
        self,
        positive_feedback: List[str],
        negative_feedback: List[str],
        report: List[str],
        student_id: List[int],
        k: int,
    ) -> List[int]:
        pos, neg = set(positive_feedback), set(negative_feedback)
        ans = []
        for m, i in zip(report, student_id):
            m = m.split(" ")
            ans.append(
                (sum([3 for s in m if s in pos]) - sum([1 for s in m if s in neg]), i)
            )
        ans.sort(key=lambda x: (-x[0], x[1]))
        return [item[1] for item in ans][:k]


# @lc code=end

if __name__ == "__main__":
    positive_feedback: List[str] = deserialize("List[str]", read_line())
    negative_feedback: List[str] = deserialize("List[str]", read_line())
    report: List[str] = deserialize("List[str]", read_line())
    student_id: List[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topStudents(
        positive_feedback, negative_feedback, report, student_id, k
    )

    print("\noutput:", serialize(ans))
