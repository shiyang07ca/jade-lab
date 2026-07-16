# Created by shiyang07ca at 2023/07/29 12:58
# leetgo: dev
# https://leetcode.cn/problems/linked-list-cycle/

from typing import *
from leetgo_py import *

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False
        a = b = head
        while b and b.next:
            a, b = a.next, b.next.next
            if a is b:
                return True
        return False


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    pos: int = deserialize("int", read_line())
    ans = Solution().hasCycle(head, pos)

    print("\noutput:", serialize(ans))
