from __future__ import annotations

# https://leetcode.cn/problems/odd-even-linked-list/
from leetgo_py import ListNode, deserialize, read_line, serialize

# @lc code=begin


class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        # 按原链表的位置分组：第 1、3、5……个节点在前，第 2、4、6……个在后。
        # 判断的是位置的奇偶，不是节点值的奇偶。
        if head is None or head.next is None:
            return head

        odd = head  # 已处理的最后一个奇数位置节点。
        even = head.next  # 已处理的最后一个偶数位置节点。
        even_head = even  # 保存偶数链入口，最后用于拼接。

        # even.next 是下一个待处理的奇数位置节点。
        while even is not None and even.next is not None:
            # 跳过当前偶数节点，接上下一个奇数节点，再移动 odd。
            odd.next = even.next
            odd = odd.next

            # odd 已移到新节点，其 next 是下一个偶数节点，也可能为 None。
            even.next = odd.next
            even = even.next

        # 两组内部均保持原顺序，将偶数链接到奇数链尾部。
        odd.next = even_head
        return head


# @lc code=end

if __name__ == "__main__":
    head: ListNode = deserialize("ListNode", read_line())
    ans = Solution().oddEvenList(head)
    print("\noutput:", serialize(ans, "ListNode"))
