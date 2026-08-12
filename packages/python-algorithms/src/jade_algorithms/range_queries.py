"""Immutable range sums and batch range additions."""

from collections.abc import Sequence


class MatrixPrefixSum:
    """Answer half-open rectangular sum queries in constant time."""

    def __init__(self, matrix: Sequence[Sequence[int]]) -> None:
        if not matrix or not matrix[0]:
            raise ValueError("matrix must not be empty")
        rows, columns = len(matrix), len(matrix[0])
        if any(len(row) != columns for row in matrix):
            raise ValueError("matrix must be rectangular")

        prefix = [[0] * (columns + 1) for _ in range(rows + 1)]
        for row_index, row in enumerate(matrix):
            for column_index, value in enumerate(row):
                prefix[row_index + 1][column_index + 1] = (
                    prefix[row_index + 1][column_index]
                    + prefix[row_index][column_index + 1]
                    - prefix[row_index][column_index]
                    + value
                )
        self._prefix = prefix
        self._rows = rows
        self._columns = columns

    def query(self, top: int, left: int, bottom: int, right: int) -> int:
        """Return the sum in ``[top:bottom, left:right]``."""
        coordinates = (top, left, bottom, right)
        if any(not isinstance(value, int) or isinstance(value, bool) for value in coordinates):
            raise TypeError("query coordinates must be integers")
        if not (0 <= top <= bottom <= self._rows and 0 <= left <= right <= self._columns):
            raise ValueError("query rectangle is outside the matrix")

        prefix = self._prefix
        return (
            prefix[bottom][right]
            - prefix[bottom][left]
            - prefix[top][right]
            + prefix[top][left]
        )


def apply_range_additions(
    length: int,
    updates: Sequence[tuple[int, int, int]],
) -> list[int]:
    """Apply inclusive ``(left, right, delta)`` updates to a zero-filled array."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise TypeError("length must be an integer")
    if length < 0:
        raise ValueError("length must be non-negative")

    differences = [0] * length
    for update in updates:
        if len(update) != 3:
            raise ValueError("each update must contain left, right, and delta")
        left, right, delta = update
        if any(
            not isinstance(value, int) or isinstance(value, bool)
            for value in (left, right, delta)
        ):
            raise TypeError("update values must be integers")
        if not 0 <= left <= right < length:
            raise ValueError("update range is outside the array")
        differences[left] += delta
        if right + 1 < length:
            differences[right + 1] -= delta

    for index in range(1, length):
        differences[index] += differences[index - 1]
    return differences
