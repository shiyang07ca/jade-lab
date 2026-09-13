from __future__ import annotations

# Created by shiyang07ca at 2023/08/06 00:02
# leetgo: dev
# https://leetcode.cn/problems/swap-nodes-in-pairs/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        ans = head.next
        head.next = self.swapPairs(ans.next)
        ans.next = head
        return ans


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().swapPairs(head)

    print("\noutput:", serialize(ans))
