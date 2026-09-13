from __future__ import annotations

# Created by shiyang07ca at 2023/08/21 00:28
# leetgo: dev
# https://leetcode.cn/problems/move-pieces-to-obtain-a-string/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        t = 0
        if start.count("L") != target.count("L") or start.count("R") != target.count(
            "R"
        ):
            return False

        for i, c in enumerate(start):
            if c == "_":
                continue
            while target[t] == "_":
                t += 1

            if (
                target[t] != start[i]
                or target[t] == "R"
                and i > t
                or target[t] == "L"
                and i < t
            ):
                return False
            t += 1

        return True


# @lc code=end

if __name__ == "__main__":
    start: str = deserialize("str", read_line())
    target: str = deserialize("str", read_line())
    ans = Solution().canChange(start, target)

    print("\noutput:", serialize(ans))
