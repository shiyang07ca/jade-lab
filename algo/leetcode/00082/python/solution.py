from __future__ import annotations

# Created by shiyang07ca at 2024/01/15 00:02
# leetgo: dev
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/
from typing import Counter

from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates1(self, head: ListNode | None) -> ListNode | None:
        dummy = pre = ListNode()
        dummy.next = cur = head
        cnt = Counter()
        while cur:
            cnt[cur.val] += 1
            cur = cur.next

        while head:
            if cnt[head.val] > 1:
                pre.next = head.next
            else:
                pre = head
            head = head.next

        return dummy.next

    # 链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/solutions/2604688/python3javacgotypescript-yi-ti-yi-jie-yi-gzbt/
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        dummy = pre = ListNode(next=head)
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if pre.next == cur:
                pre = cur
            else:
                pre.next = cur.next
            cur = cur.next
        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().deleteDuplicates(head)

    print("\noutput:", serialize(ans))
