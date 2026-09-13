from __future__ import annotations

# Created by shiyang07ca at 2023/07/31 00:00
# leetgo: dev
# https://leetcode.cn/problems/reorder-list/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin

# TODO

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse(head: ListNode | None) -> ListNode | None:
            if not head or not head.next:
                return head
            ans = None
            while head:
                cur = head
                head = head.next
                cur.next = ans
                ans = cur
            return ans

        slow = fast = head
        while fast and fast.next:
            assert slow is not None
            slow, fast = slow.next, fast.next.next
        mid = reverse(slow)
        dummy = ListNode()
        # print(serialize(slow), serialize(head), serialize(mid))
        while (head is not None and head is not slow) or mid:
            if head is not None and head is not slow:
                dummy.next = head
                head = head.next
                dummy = dummy.next
            if mid:
                dummy.next = mid
                mid = mid.next
                dummy = dummy.next

    # 链接：https://leetcode.cn/problems/reorder-list/solutions/2365667/python3javacgo-yi-ti-yi-jie-kuai-man-zhi-t9u2/
    def reorderList2(self, head: ListNode | None) -> None:
        # 快慢指针找到链表中点
        if head is None:
            return
        fast = slow = head
        while fast is not None:
            next_fast = fast.next
            if next_fast is None or next_fast.next is None:
                break
            assert slow is not None
            slow = slow.next
            fast = next_fast.next

        # cur 指向右半部分链表
        assert slow is not None
        cur = slow.next
        slow.next = None

        # 反转右半部分链表
        pre = None
        while cur:
            t = cur.next
            cur.next = pre
            pre, cur = cur, t
        cur = head

        # 此时 cur, pre 分别指向链表左右两半的第一个节点
        # 合并
        while pre:
            t = pre.next
            assert cur is not None
            pre.next = cur.next
            cur.next = pre
            cur, pre = pre.next, t


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    Solution().reorderList(head)
    ans = head

    print("\noutput:", serialize(ans))
