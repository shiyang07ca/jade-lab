# Created by shiyang07ca at 2024/01/14 11:16
# leetgo: dev
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = pre = head
        s = set()
        while head:
            if head.val not in s:
                s.add(head.val)
                pre = head
            else:
                pre.next = head.next
            head = head.next

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)

    print("\noutput:", serialize(ans))
