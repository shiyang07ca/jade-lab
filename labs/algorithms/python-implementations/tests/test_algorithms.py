from __future__ import annotations

import pytest

from algorithms import (
    DisjointSet,
    MatrixPrefixSum,
    MinHeap,
    apply_range_additions,
    distinct_prime_factor_counts,
    eratosthenes,
    fibonacci_sequence,
    linear_sieve,
    sliding_window_max,
    zero_one_knapsack,
)


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


def test_prime_factor_counts_and_input_types() -> None:
    counts = distinct_prime_factor_counts(12)
    assert counts[1] == 0
    assert counts[6] == 2
    assert counts[12] == 2
    with pytest.raises(ValueError):
        distinct_prime_factor_counts(-1)
    with pytest.raises(TypeError):
        eratosthenes(True)


def test_disjoint_set_tracks_components_and_sizes() -> None:
    groups = DisjointSet(6)
    assert len(groups) == 6
    assert groups.union(0, 1)
    assert groups.union(1, 2)
    assert not groups.union(0, 2)
    assert groups.connected(0, 2)
    assert not groups.connected(0, 3)
    assert groups.component_size(1) == 3
    assert groups.components == 4
    with pytest.raises(IndexError):
        groups.find(6)


def test_min_heap_exposes_only_heap_operations() -> None:
    values = [4, 50, 7, 55, 90, 87, 2]
    queue = MinHeap(values)
    assert queue.peek() == 2
    assert [queue.pop() for _ in values] == sorted(values)
    with pytest.raises(IndexError):
        queue.pop()


def test_sliding_window_max_and_invalid_windows() -> None:
    values = [4, 3, 5, 4, 3, 3, 6, 7]
    assert sliding_window_max(values, 3) == [5, 5, 5, 4, 6, 7]
    assert sliding_window_max(values, len(values)) == [7]
    with pytest.raises(ValueError):
        sliding_window_max([], 1)


def test_matrix_prefix_sum_uses_half_open_coordinates() -> None:
    prefix = MatrixPrefixSum([[1, 2], [3, 4]])
    assert prefix.query(0, 0, 2, 2) == 10
    assert prefix.query(1, 0, 2, 2) == 7
    assert prefix.query(1, 1, 1, 2) == 0
    with pytest.raises(ValueError):
        prefix.query(0, 0, 3, 2)


def test_range_additions_validate_boundaries() -> None:
    assert apply_range_additions(4, [(0, 1, 2), (1, 3, 1)]) == [2, 3, 1, 1]
    assert apply_range_additions(0, []) == []
    with pytest.raises(ValueError):
        apply_range_additions(4, [(0, 4, 1)])


def test_zero_one_knapsack_uses_each_item_once() -> None:
    assert zero_one_knapsack(5, [2, 3, 4], [3, 4, 5]) == 7
    assert zero_one_knapsack(5, [], []) == 0
    with pytest.raises(ValueError):
        zero_one_knapsack(5, [1], [1, 2])
