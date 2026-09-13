from __future__ import annotations

# Created by shiyang07ca at 2024/11/09 17:08
# leetgo: 1.4.10
# https://leetcode.cn/problems/sort-list/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# TODO:


class Solution:
    # 链接：https://leetcode.cn/problems/sort-list/solutions/13728/sort-list-gui-bing-pai-xu-lian-biao-by-jyd/
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        # cut the LinkedList at the mid index.
        slow, fast = head, head.next
        while fast and fast.next:
            assert slow is not None
            fast, slow = fast.next.next, slow.next
        assert slow is not None
        mid, slow.next = slow.next, None  # save and cut.

        left, right = self.sortList(head), self.sortList(mid)

        h = res = ListNode(0)
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right

        return res.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().sortList(head)
    print("\noutput:", serialize(ans, "ListNode"))
