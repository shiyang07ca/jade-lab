"""Knapsack algorithms."""

from collections.abc import Sequence


def zero_one_knapsack(
    capacity: int,
    weights: Sequence[int],
    values: Sequence[int],
) -> int:
    """Return the maximum value obtainable when each item is used at most once."""
    if not isinstance(capacity, int) or isinstance(capacity, bool):
        raise TypeError("capacity must be an integer")
    if capacity < 0:
        raise ValueError("capacity must be non-negative")
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if any(not isinstance(weight, int) or isinstance(weight, bool) for weight in weights):
        raise TypeError("weights must be integers")
    if any(not isinstance(value, int) or isinstance(value, bool) for value in values):
        raise TypeError("values must be integers")
    if any(weight <= 0 for weight in weights):
        raise ValueError("weights must be positive")

    best = [0] * (capacity + 1)
    for weight, value in zip(weights, values, strict=True):
        for remaining in range(capacity, weight - 1, -1):
            best[remaining] = max(best[remaining], best[remaining - weight] + value)
    return best[capacity]
