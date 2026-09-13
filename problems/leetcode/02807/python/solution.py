from __future__ import annotations

# Created by shiyang07ca at 2024/01/06 11:10
# leetgo: dev
# https://leetcode.cn/problems/insert-greatest-common-divisors-in-linked-list/
from math import gcd

from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: ListNode | None
    ) -> ListNode | None:
        if head is None:
            return None
        dummy = ListNode()
        dummy.next = head
        cur = head.next
        while head and cur:
            new = ListNode(gcd(head.val, cur.val))
            head.next = new
            new.next = cur
            head = cur
            cur = cur.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().insertGreatestCommonDivisors(head)

    print("\noutput:", serialize(ans))
