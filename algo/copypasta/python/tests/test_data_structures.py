from __future__ import annotations

import pytest

from binary_tree import build_level_order, inorder, level_order, postorder, preorder
from fenwick_tree import FenwickTree
from linked_list import ListNode, reverse_iterative, reverse_recursive, to_list
from monotonic_stack import nearest_less_indices, next_greater_indices
from segment_tree import LazyMinSegmentTree, RangeAssignSumTree, SumSegmentTree
from stack import reverse_stack
from trie import Trie


def test_fenwick_tree_point_add_and_range_sum() -> None:
    tree = FenwickTree([2, 1, 4, 6, -1])
    assert tree.prefix_sum(4) == 13
    assert tree.range_sum(1, 4) == 11
    tree.add(2, 5)
    assert tree.range_sum(1, 4) == 16
    with pytest.raises(IndexError):
        tree.add(5, 1)


def test_segment_tree_sum_minimum_and_assignment_capabilities() -> None:
    sums = SumSegmentTree([1, 8, 3, 4, 7, 1, 6, 2])
    assert sums.range_sum(0, 3) == 12
    sums.assign(2, 10)
    assert sums.range_sum(0, 3) == 19

    minimums = LazyMinSegmentTree([5, 2, 7, 4])
    minimums.add(1, 4, -3)
    minimums.add(0, 2, 4)
    assert minimums.range_min(0, 4) == 1
    assert minimums.range_min(2, 4) == 1

    assignments = RangeAssignSumTree([1, 2, 3, 4, 5])
    assignments.assign(1, 4, 7)
    assert assignments.range_sum(0, 5) == 27
    assignments.assign(2, 5, 0)
    assert assignments.range_sum(0, 5) == 8
    assignments.assign(0, 3, -2)
    assert assignments.range_sum(0, 5) == -6
    with pytest.raises(IndexError):
        assignments.range_sum(2, 2)


def test_linked_list_reversal_variants() -> None:
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert to_list(reverse_iterative(head)) == [3, 2, 1]
    head = ListNode(1, ListNode(2, ListNode(3)))
    assert to_list(reverse_recursive(head)) == [3, 2, 1]
    assert reverse_iterative(None) is None


def test_monotonic_stack_with_and_without_duplicates() -> None:
    assert nearest_less_indices([3, 4, 1, 5, 2]) == [
        (None, 2),
        (0, 2),
        (None, None),
        (2, 4),
        (2, None),
    ]
    assert nearest_less_indices([2, 2, 1]) == [(None, 2), (None, 2), (None, None)]
    assert next_greater_indices([2, 1, 2, 4, 3]) == [3, 2, 3, None, None]


def test_recursive_stack_reversal() -> None:
    stack = [1, 5, 2]
    reverse_stack(stack)
    assert stack == [2, 5, 1]
    empty: list[int] = []
    reverse_stack(empty)
    assert empty == []


def test_binary_tree_build_and_traversals() -> None:
    root = build_level_order(["a", "b", "c", "d", "e", "f", "g"])
    assert preorder(root) == ["a", "b", "d", "e", "c", "f", "g"]
    assert inorder(root) == ["d", "b", "e", "a", "f", "c", "g"]
    assert postorder(root) == ["d", "e", "b", "f", "g", "c", "a"]
    assert level_order(root) == ["a", "b", "c", "d", "e", "f", "g"]
    assert build_level_order([]) is None
    with pytest.raises(ValueError):
        build_level_order([None, 1])


def test_trie_insert_prefix_and_remove() -> None:
    trie = Trie()
    for word in ["banana", "bananas", "band", "apple", ""]:
        trie.insert(word)
    assert trie.contains("banana")
    assert trie.starts_with("ban")
    assert not trie.contains("ban")
    assert trie.contains("")
    assert trie.remove("")
    assert not trie.contains("")
    assert trie.remove("banana")
    assert not trie.contains("banana")
    assert trie.contains("bananas")
    assert not trie.remove("missing")
