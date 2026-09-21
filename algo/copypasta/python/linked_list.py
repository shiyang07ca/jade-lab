"""Singly linked-list reversal."""

from dataclasses import dataclass


@dataclass(slots=True)
class ListNode[T]:
    value: T
    next: "ListNode[T] | None" = None


def reverse_iterative[T](head: ListNode[T] | None) -> ListNode[T] | None:
    previous = None
    current = head
    while current is not None:
        following = current.next
        current.next = previous
        previous = current
        current = following
    return previous


def reverse_recursive[T](head: ListNode[T] | None) -> ListNode[T] | None:
    if head is None or head.next is None:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def to_list[T](head: ListNode[T] | None) -> list[T]:
    values: list[T] = []
    while head is not None:
        values.append(head.value)
        head = head.next
    return values
