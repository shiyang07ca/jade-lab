"""Manacher's linear-time longest-palindromic-substring algorithm."""


def _longest_bounds(text: str) -> tuple[int, int]:
    transformed: list[str | None] = [None]
    for character in text:
        transformed.extend((character, None))
    radii = [0] * len(transformed)
    center = right = 0
    best_center = best_radius = 0
    for index in range(len(transformed)):
        if index < right:
            radii[index] = min(right - index, radii[2 * center - index])
        while (
            index - radii[index] - 1 >= 0
            and index + radii[index] + 1 < len(transformed)
            and transformed[index - radii[index] - 1] == transformed[index + radii[index] + 1]
        ):
            radii[index] += 1
        if index + radii[index] > right:
            center, right = index, index + radii[index]
        if radii[index] > best_radius:
            best_center, best_radius = index, radii[index]
    start = (best_center - best_radius) // 2
    return start, best_radius


def longest_palindrome(text: str) -> str:
    """Return the first longest palindromic substring."""
    start, length = _longest_bounds(text)
    return text[start : start + length]


def longest_palindrome_length(text: str) -> int:
    return _longest_bounds(text)[1]
