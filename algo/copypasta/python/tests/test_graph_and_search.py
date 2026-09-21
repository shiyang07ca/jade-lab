from __future__ import annotations

from math import inf

import pytest

from binary_search import binary_search, lower_bound, upper_bound
from graph import adjacency_list, bfs_order, dijkstra
from lca import LowestCommonAncestor
from manacher import longest_palindrome, longest_palindrome_length
from sorting import merge_sort, quick_sort
from topological_sort import topological_sort


def test_graph_representation_bfs_and_dijkstra() -> None:
    graph = adjacency_list(
        5,
        [(0, 1, 4), (0, 2, 1), (2, 1, 2), (1, 3, 1)],
        directed=True,
    )
    assert graph[0] == [(1, 4), (2, 1)]
    assert bfs_order([[1, 2], [3], [1], [], []], 0) == [0, 1, 2, 3]
    assert dijkstra(graph, 0) == [0, 3, 1, 4, inf]
    assert adjacency_list(2, [(0, 1, 3)], directed=False) == [[(1, 3)], [(0, 3)]]
    with pytest.raises(IndexError):
        adjacency_list(2, [(0, 2, 1)])
    with pytest.raises(ValueError):
        dijkstra([[(1, -1)], []], 0)


def test_binary_search_boundaries_and_empty_input() -> None:
    values = [1, 3, 3, 3, 8]
    assert lower_bound(values, 3) == 1
    assert upper_bound(values, 3) == 4
    assert binary_search(values, 3) == 1
    assert binary_search(values, 2) is None
    assert lower_bound([], 10) == 0


def test_sorting_returns_sorted_copies() -> None:
    values = [5, -1, 3, 3, 0]
    assert merge_sort(values) == [-1, 0, 3, 3, 5]
    assert quick_sort(values) == [-1, 0, 3, 3, 5]
    assert values == [5, -1, 3, 3, 0]
    assert quick_sort([]) == []


def test_manacher_handles_even_odd_and_separator_characters() -> None:
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("cabcba") == "abcba"
    assert longest_palindrome("a#a") == "a#a"
    assert longest_palindrome_length("") == 0


def test_topological_sort_detects_cycles() -> None:
    order = topological_sort(4, [(0, 1), (0, 2), (1, 3), (2, 3)])
    assert order is not None
    positions = {vertex: index for index, vertex in enumerate(order)}
    assert all(
        positions[source] < positions[target] for source, target in [(0, 1), (0, 2), (1, 3), (2, 3)]
    )
    assert topological_sort(2, [(0, 1), (1, 0)]) is None


def test_lowest_common_ancestor_and_kth_ancestor() -> None:
    tree = LowestCommonAncestor(7, [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)])
    assert tree.query(3, 4) == 1
    assert tree.query(3, 6) == 0
    assert tree.query(2, 6) == 2
    assert tree.kth_ancestor(4, 2) == 0
    assert tree.kth_ancestor(4, 3) is None
    rerooted = LowestCommonAncestor(4, [(2, 0), (2, 1), (1, 3)], root=2)
    assert rerooted.query(0, 3) == 2
    with pytest.raises(ValueError):
        LowestCommonAncestor(3, [(0, 1)])
