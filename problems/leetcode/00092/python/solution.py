from __future__ import annotations

# Created by shiyang07ca at 2026/09/13 15:22
# leetgo: 1.4.17
# https://leetcode.cn/problems/reverse-linked-list-ii/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(
        self, head: ListNode | None, left: int, right: int
    ) -> ListNode | None:
        # 把 p0 移到 left 的前一个节点
        dummy = ListNode(next=head)
        p0 = dummy
        for _ in range(left - 1):
            p0 = p0.next

        pre = None  # 当前这一组翻转后的头节点, 负责当前已经翻转的部分
        cur = p0.next  # 当前正在处理的节点, 负责当前还没翻转的部分
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur
        p0.next = pre

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    left: int = deserialize("int", read_line())
    right: int = deserialize("int", read_line())
    ans = Solution().reverseBetween(head, left, right)
    print("\noutput:", serialize(ans, "ListNode"))
