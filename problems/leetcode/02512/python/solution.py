from __future__ import annotations

# Created by shiyang07ca at 2023/10/11 12:53
# leetgo: dev
# https://leetcode.cn/problems/reward-top-k-students/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def topStudents(
        self,
        positive_feedback: list[str],
        negative_feedback: list[str],
        report: list[str],
        student_id: list[int],
        k: int,
    ) -> list[int]:
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
    positive_feedback: list[str] = deserialize("List[str]", read_line())
    negative_feedback: list[str] = deserialize("List[str]", read_line())
    report: list[str] = deserialize("List[str]", read_line())
    student_id: list[int] = deserialize("List[int]", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().topStudents(
        positive_feedback, negative_feedback, report, student_id, k
    )

    print("\noutput:", serialize(ans))
