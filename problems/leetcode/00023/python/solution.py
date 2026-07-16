# Created by shiyang07ca at 2023/08/12 00:22
# leetgo: dev
# https://leetcode.cn/problems/merge-k-sorted-lists/

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小


class Solution:
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = cur = ListNode()
        n = len(lists)
        if n == 0 or n == 1 and lists[0] is None:
            return None

        h = []
        for l in lists:
            while l:
                heappush(h, l.val)
                l = l.next
        while h:
            v = heappop(h)
            cur.next = ListNode(v)
            cur = cur.next

        return ans.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点


# @lc code=end

if __name__ == "__main__":
    lists: List[ListNode] = deserialize("List[ListNode]", read_line())
    ans = Solution().mergeKLists(lists)

    print("\noutput:", serialize(ans))
