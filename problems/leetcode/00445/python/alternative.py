from __future__ import annotations

# Created by shiyang07ca at 2023/07/03 13:00
# leetgo: dev
# https://leetcode.cn/problems/add-two-numbers-ii/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        raise NotImplementedError

# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)

    print("\noutput:", serialize(ans))
