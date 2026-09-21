from __future__ import annotations

# Created by shiyang07ca at 2023/08/05 00:09
# leetgo: dev
# https://leetcode.cn/problems/merge-two-sorted-lists/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: ListNode | None, list2: ListNode | None
    ) -> ListNode | None:
        cur = ans = ListNode()
        while list1 or list2:
            if not list1:
                assert list2 is not None
                cur.next = list2
                list2 = list2.next
            elif not list2:
                assert list1 is not None
                cur.next = list1
                list1 = list1.next
            elif list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        return ans.next

    def mergeTwoLists1(
        self, l1: ListNode | None, l2: ListNode | None
    ) -> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# @lc code=end

if __name__ == "__main__":
    list1: ListNode = deserialize("ListNode", read_line())
    list2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().mergeTwoLists(list1, list2)

    print("\noutput:", serialize(ans, "ListNode"))
