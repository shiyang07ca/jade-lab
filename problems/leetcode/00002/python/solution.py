# Created by shiyang07ca at 2023/07/02 07:30
# https://leetcode.cn/problems/add-two-numbers/

"""
2. 两数相加 (Medium)
给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节
点只能存储 **一位** 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

**示例 1：**

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg)

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

```

**示例 2：**

```
输入：l1 = [0], l2 = [0]
输出：[0]

```

**示例 3：**

```
输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

```

**提示：**

- 每个链表中的节点数在范围 `[1, 100]` 内
- `0 <= Node.val <= 9`
- 题目数据保证列表表示的数字不含前导零

"""

from typing import *
from leetgo_py import *

# @lc code=begin


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers1(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans = dummy = ListNode()
        t = 0
        while l1 and l2:
            v = l1.val + l2.val + t
            dummy.next = ListNode(v % 10)
            dummy = dummy.next
            t = v // 10
            l1 = l1.next
            l2 = l2.next

        while l1:
            v = l1.val + t
            dummy.next = ListNode(v % 10)
            dummy = dummy.next
            t = v // 10
            l1 = l1.next
        while l2:
            v = l2.val + t
            dummy.next = ListNode(v % 10)
            dummy = dummy.next
            t = v // 10
            l2 = l2.next

        if t:
            dummy.next = ListNode(t)
        return ans.next

    # l1 和 l2 为当前遍历的节点，carry 为进位
    def addTwoNumbers2(
        self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0
    ) -> Optional[ListNode]:
        if l1 is None and l2 is None:  # 递归边界：l1 和 l2 都是空节点
            return ListNode(carry) if carry else None  # 如果进位了，就额外创建一个节点
        if l1 is None:  # 如果 l1 是空的，那么此时 l2 一定不是空节点
            l1, l2 = l2, l1  # 小技巧：交换 l1 与 l2，保证 l1 非空，从而简化代码
        carry += l1.val + (l2.val if l2 else 0)  # 节点值和进位加在一起
        l1.val = carry % 10  # 每个节点保存一个数位
        l1.next = self.addTwoNumbers(
            l1.next, l2.next if l2 else None, carry // 10
        )  # 进位
        return l1

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = dummy = ListNode()  # 哨兵节点
        carry = 0  # 进位
        while l1 or l2 or carry:  # 有一个不是空节点，或者还有进位，就继续迭代
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)  # 节点值和进位加在一起
            cur.next = ListNode(carry % 10)  # 每个节点保存一个数位
            carry //= 10  # 新的进位
            cur = cur.next  # 下一个节点
            if l1:
                l1 = l1.next  # 下一个节点
            if l2:
                l2 = l2.next  # 下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是头节点


# @lc code=end

if __name__ == "__main__":
    l1: ListNode = deserialize("ListNode", read_line())
    l2: ListNode = deserialize("ListNode", read_line())
    ans = Solution().addTwoNumbers(l1, l2)

    print("\noutput:", serialize(ans))
