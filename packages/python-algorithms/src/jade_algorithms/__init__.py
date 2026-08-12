"""Public interface for the Jade Algorithms package."""

from jade_algorithms.disjoint_set import DisjointSet
from jade_algorithms.heap import MinHeap
from jade_algorithms.knapsack import zero_one_knapsack
from jade_algorithms.primes import (
    distinct_prime_factor_counts,
    eratosthenes,
    linear_sieve,
)
from jade_algorithms.range_queries import MatrixPrefixSum, apply_range_additions
from jade_algorithms.sequences import fibonacci_sequence
from jade_algorithms.windows import sliding_window_max

__all__ = [
    "DisjointSet",
    "MatrixPrefixSum",
    "MinHeap",
    "apply_range_additions",
    "distinct_prime_factor_counts",
    "eratosthenes",
    "fibonacci_sequence",
    "linear_sieve",
    "sliding_window_max",
    "zero_one_knapsack",
]
