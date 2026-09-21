from __future__ import annotations

import pytest

from disjoint_set import DisjointSet
from heap import MinHeap
from knapsack import zero_one_knapsack
from number_theory import (
    distinct_prime_factor_counts,
    eratosthenes,
    linear_sieve,
    prime_factorization,
)
from range_queries import MatrixPrefixSum, apply_range_additions
from sequences import fibonacci_sequence
from windows import sliding_window_max


def test_fibonacci_sequence_validates_length() -> None:
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(8) == [1, 1, 2, 3, 5, 8, 13, 21]
    with pytest.raises(ValueError):
        fibonacci_sequence(-1)
    with pytest.raises(TypeError):
        fibonacci_sequence(True)


@pytest.mark.parametrize("limit", [-1, 0, 1, 2, 30, 120])
def test_prime_sieves_agree(limit: int) -> None:
    assert eratosthenes(limit) == linear_sieve(limit)


def test_prime_preprocessing_and_factorization() -> None:
    counts = distinct_prime_factor_counts(12)
    assert counts[1] == 0
    assert counts[6] == counts[12] == 2
    assert prime_factorization(1) == []
    assert prime_factorization(360) == [(2, 3), (3, 2), (5, 1)]
    assert prime_factorization(97) == [(97, 1)]
    with pytest.raises(ValueError):
        prime_factorization(0)
    with pytest.raises(TypeError):
        eratosthenes(True)


def test_disjoint_set_tracks_components_and_sizes() -> None:
    groups = DisjointSet(6)
    assert groups.union(0, 1)
    assert groups.union(1, 2)
    assert not groups.union(0, 2)
    assert groups.connected(0, 2)
    assert not groups.connected(0, 3)
    assert groups.component_size(1) == 3
    assert groups.components == 4
    with pytest.raises(IndexError):
        groups.find(6)


def test_min_heap_orders_duplicates_and_rejects_empty_access() -> None:
    values = [4, 50, 7, 4, 90, 87, 2]
    heap = MinHeap(values)
    assert heap.peek() == 2
    heap.push(1)
    assert heap.pop() == 1
    assert [heap.pop() for _ in values] == sorted(values)
    with pytest.raises(IndexError):
        heap.pop()


def test_sliding_window_max_and_invalid_windows() -> None:
    values = [4, 3, 5, 4, 3, 3, 6, 7]
    assert sliding_window_max(values, 3) == [5, 5, 5, 4, 6, 7]
    assert sliding_window_max(values, len(values)) == [7]
    with pytest.raises(ValueError):
        sliding_window_max([], 1)


def test_matrix_prefix_sum_and_range_additions() -> None:
    prefix = MatrixPrefixSum([[1, 2], [3, 4]])
    assert prefix.query(0, 0, 2, 2) == 10
    assert prefix.query(1, 0, 2, 2) == 7
    assert prefix.query(1, 1, 1, 2) == 0
    assert apply_range_additions(4, [(0, 1, 2), (1, 3, 1)]) == [2, 3, 1, 1]
    assert apply_range_additions(0, []) == []
    with pytest.raises(ValueError):
        prefix.query(0, 0, 3, 2)
    with pytest.raises(ValueError):
        apply_range_additions(4, [(0, 4, 1)])


def test_zero_one_knapsack_uses_each_item_once() -> None:
    assert zero_one_knapsack(5, [2, 3, 4], [3, 4, 5]) == 7
    assert zero_one_knapsack(5, [], []) == 0
    with pytest.raises(ValueError):
        zero_one_knapsack(5, [1], [1, 2])
