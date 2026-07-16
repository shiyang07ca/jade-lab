# Created by shiyang07ca at 2023/07/30 00:07
# leetgo: dev
# https://leetcode.cn/problems/linked-list-cycle-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while head != slow:
                    head, slow = head.next, slow.next
                return slow
        return None

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vis = set()
        while head:
            if head in vis:
                return head
            vis.add(head)
            head = head.next
        return None


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().detectCycle(head, pos)

    print("\noutput:", serialize(ans))
