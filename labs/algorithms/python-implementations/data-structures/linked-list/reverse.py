"""

反转链表

"""


def reverse_iter(head):
    pre = None  # 翻转后的头节点, 负责当前已经翻转的部分
    cur = head  # 当前正在处理的节点, 负责当前还没翻转的部分
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
