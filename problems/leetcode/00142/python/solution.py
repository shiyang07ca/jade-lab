from __future__ import annotations

# Created by shiyang07ca at 2023/07/30 00:07
# leetgo: dev
# https://leetcode.cn/problems/linked-list-cycle-ii/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle1(self, head: ListNode | None) -> ListNode | None:
        slow = fast = head
        while fast and fast.next:
            assert slow is not None
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                while head != slow:
                    assert head is not None
                    assert slow is not None
                    head, slow = head.next, slow.next
                return slow
        return None

    def detectCycle(self, head: ListNode | None) -> ListNode | None:
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
    _ = deserialize("int", read_line())
    ans = Solution().detectCycle(head)

    print("\noutput:", serialize(ans))
