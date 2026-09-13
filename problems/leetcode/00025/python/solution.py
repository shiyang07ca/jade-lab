# Created by shiyang07ca at 2026/09/13 16:23
# leetgo: 1.4.17
# https://leetcode.cn/problems/reverse-nodes-in-k-group/

from typing import *

from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 链接：https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/1992228/you-xie-cuo-liao-yi-ge-shi-pin-jiang-tou-plfs/
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # 统计节点个数
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # last_tail 是上一组翻转后的尾节点
        last_tail = dummy = ListNode(next=head)

        # k 个一组处理
        while n >= k:
            n -= k

            pre = None  # 前一个节点, 循环结束时为新的头节点
            cur = last_tail.next  # 当前节点, 循环结束时为新的尾节点
            for _ in range(k):  # 同 92 题
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            # 翻转后：
            # pre 是当前组的头节点
            # cur 是下一组的起始节点
            # last_tail 是上一组的尾节点
            # last_tail.next 是当前组的尾节点
            tail = last_tail.next
            tail.next = cur  # 当前组的尾节点指向下一组的起始节点
            last_tail.next = pre  # 上一组的尾节点指向当前组的头节点
            last_tail = tail

        return dummy.next


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    k: int = deserialize("int", read_line())
    ans = Solution().reverseKGroup(head, k)
    print("\noutput:", serialize(ans, "ListNode"))
