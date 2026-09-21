"""Prime sieves and factorization."""

from math import isqrt


def _validate_limit(limit: int) -> None:
    if not isinstance(limit, int) or isinstance(limit, bool):
        raise TypeError("limit must be an integer")


def eratosthenes(limit: int) -> list[int]:
    """Return primes at most ``limit`` in O(n log log n) time."""
    _validate_limit(limit)
    if limit < 2:
        return []
    is_prime = bytearray(b"\x01") * (limit + 1)
    is_prime[:2] = b"\x00\x00"
    for candidate in range(2, isqrt(limit) + 1):
        if is_prime[candidate]:
            start = candidate * candidate
            is_prime[start : limit + 1 : candidate] = b"\x00" * ((limit - start) // candidate + 1)
    return [value for value in range(2, limit + 1) if is_prime[value]]


def linear_sieve(limit: int) -> list[int]:
    """Return primes at most ``limit``, marking every composite once."""
    _validate_limit(limit)
    if limit < 2:
        return []
    smallest_factor = [0] * (limit + 1)
    primes: list[int] = []
    for value in range(2, limit + 1):
        if smallest_factor[value] == 0:
            smallest_factor[value] = value
            primes.append(value)
        for prime in primes:
            composite = value * prime
            if composite > limit or prime > smallest_factor[value]:
                break
            smallest_factor[composite] = prime
    return primes


def distinct_prime_factor_counts(limit: int) -> list[int]:
    """Return ``counts`` where ``counts[n]`` is n's distinct factor count."""
    _validate_limit(limit)
    if limit < 0:
        raise ValueError("limit must be non-negative")
    counts = [0] * (limit + 1)
    for prime in range(2, limit + 1):
        if counts[prime] == 0:
            for multiple in range(prime, limit + 1, prime):
                counts[multiple] += 1
    return counts


def prime_factorization(number: int) -> list[tuple[int, int]]:
    """Return the prime factors of a positive integer as ``(prime, exponent)``."""
    if not isinstance(number, int) or isinstance(number, bool):
        raise TypeError("number must be an integer")
    if number < 1:
        raise ValueError("number must be positive")
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= number:
        exponent = 0
        while number % divisor == 0:
            number //= divisor
            exponent += 1
        if exponent:
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if number > 1:
        factors.append((number, 1))
    return factors
