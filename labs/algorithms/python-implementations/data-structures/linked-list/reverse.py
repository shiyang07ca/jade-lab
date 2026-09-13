"""

反转链表

"""


def reverse_iter(head):
    pre = None  # 前一个节点, 循环结束时为新的头节点
    cur = head  # 当前节点, 循环结束时为新的尾节点
    while cur:
        nxt = cur.next  # 保持下一个节点
        cur.next = pre  # 反转当前节点
        pre = cur  # 更新前一个节点
        cur = nxt  # 移动到下一个节点

    return pre


def reverse_recur(head):
    if not head or not head.next:
        return head

    last = reverse_recur(head.next)
    head.next.next = head
    head.next = None
    return last
