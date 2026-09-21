from __future__ import annotations

# Created by shiyang07ca at 2024/04/23 00:14
# leetgo: dev
# https://leetcode.cn/problems/grumpy-bookstore-owner/
from leetgo_py import deserialize, read_line, serialize

# @lc code=begin

# TODO:
# tag: Sliding Window


class Solution:
    # 链接：https://leetcode.cn/problems/grumpy-bookstore-owner/solutions/
    def maxSatisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        s = [0, 0]
        max_s1 = 0
        for i, (c, g) in enumerate(zip(customers, grumpy)):
            s[g] += c
            if i < minutes - 1:  # 窗口长度不足 minutes
                continue
            max_s1 = max(max_s1, s[1])
            if grumpy[i - minutes + 1]:
                s[1] -= customers[i - minutes + 1]  # 窗口最左边元素离开窗口
        return s[0] + max_s1


# @lc code=end

if __name__ == "__main__":
    customers: list[int] = deserialize("List[int]", read_line())
    grumpy: list[int] = deserialize("List[int]", read_line())
    minutes: int = deserialize("int", read_line())
    ans = Solution().maxSatisfied(customers, grumpy, minutes)
    print("\noutput:", serialize(ans, "integer"))
