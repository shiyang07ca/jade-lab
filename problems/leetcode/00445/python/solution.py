# Created by shiyang07ca at 2023/07/03 13:09
# leetgo: dev
# https://leetcode.cn/problems/add-two-numbers-ii/

from typing import *
from leetgo_py import *

# @lc code=begin

# TODO
# tag: linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# 递归
# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/add-two-numbers-ii/solutions/2328330/fan-zhuan-lian-biao-liang-shu-xiang-jia-okw6q/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head  # 把下一个节点指向自己
        head.next = None  # 断开指向下一个节点的连接，保证最终链表的末尾节点的 next 是空节点
        return new_head

    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwo(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = carry % 10  # 每个节点保存一个数位
        l1.next = self.addTwo(l1.next, l2.next if l2 else None, carry // 10)  # 进位
        return l1

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)  # l1 和 l2 反转后，就变成【2. 两数相加】了
        l3 = self.addTwo(l1, l2)
        return self.reverseList(l3)


# 迭代
class Solution2:
    # 视频讲解 https://www.bilibili.com/video/BV1sd4y1x7KN/
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def addTwo(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            if l1:
                carry += l1.val  # 节点值和进位加在一起
            if l2:
                carry += l2.val  # 节点值和进位加在一起
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            if l1:
                l1 = l1.next  # 下一个节点
            if l2:
                l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)  # l1 和 l2 反转后，就变成【2. 两数相加】了
        l3 = self.addTwo(l1, l2)
        return self.reverseList(l3)  # 计算完毕后再反转


# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)

    print("\noutput:", serialize(ans))
