"""

翻转链表

"""


def reverse_iter(head):
    if not head or not head.next:
        return head

    pre = None
    while head:
        cur = head
        cur.next = pre
        pre = cur
        head = head.next

    return pre


def reverse_recur(head):
    if not head or not head.next:
        return head

    last = reverse_recur(head.next)
    head.next.next = head
    head.next = None
    return last
