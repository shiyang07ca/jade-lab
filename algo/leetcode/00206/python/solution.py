from __future__ import annotations

# Created by shiyang07ca at 2026/09/13 15:24
# leetgo: 1.4.17
# https://leetcode.cn/problems/reverse-linked-list/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def reverseIterative(head):
            pre = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = pre  # 反转当前节点
                pre = cur  # 更新前一个节点
                cur = nxt  # 移动到下一个节点

            return pre

        return reverseIterative(head)


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().reverseList(head)
    print("\noutput:", serialize(ans, "ListNode"))
