"""Prime sieves and distinct-prime-factor preprocessing."""

from math import isqrt


def _validate_limit(limit: int) -> None:
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("limit must be an integer")


def eratosthenes(limit: int) -> list[int]:
    """Return every prime less than or equal to ``limit`` in O(n log log n)."""
    _validate_limit(limit)
    if limit < 2:
        return []

    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[0:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            is_prime[start : limit + 1 : candidate] = b"\x00" * (
                (limit - start) // candidate + 1
            )
    return [value for value in range(2, limit + 1) if is_prime[value]]


def linear_sieve(limit: int) -> list[int]:
    """Return primes up to ``limit`` while marking each composite once."""
    _validate_limit(limit)
    if limit < 2:
        return []

    smallest_prime_factor = [0] * (limit + 1)
    primes: list[int] = []
    for value in range(2, limit + 1):
        if smallest_prime_factor[value] == 0:
            smallest_prime_factor[value] = value
            primes.append(value)
        for prime in primes:
            composite = value * prime
            if composite > limit or prime > smallest_prime_factor[value]:
                break
            smallest_prime_factor[composite] = prime
    return primes


def distinct_prime_factor_counts(limit: int) -> list[int]:
    """Return ``counts`` where ``counts[n]`` is n's distinct prime-factor count."""
    _validate_limit(limit)
    if limit < 0:
        raise ValueError("limit must be non-negative")

    counts = [0] * (limit + 1)
    for candidate in range(2, limit + 1):
        if counts[candidate] == 0:
            for multiple in range(candidate, limit + 1, candidate):
                counts[multiple] += 1
    return counts
