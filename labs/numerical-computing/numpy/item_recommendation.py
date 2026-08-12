"""Small, deterministic item-to-item collaborative-filtering experiment."""

from __future__ import annotations

import numpy as np
from numpy.typing import NDArray


FloatMatrix = NDArray[np.float64]


def item_cosine_similarity(ratings: FloatMatrix) -> FloatMatrix:
    """Return pairwise cosine similarity using users who rated both items.

    Zero means "not rated". Ratings must be a finite, non-negative 2-D matrix.
    """
    matrix = np.asarray(ratings, dtype=np.float64)
    if matrix.ndim != 2:
        raise ValueError("ratings must be a 2-D matrix")
    if not np.all(np.isfinite(matrix)) or np.any(matrix < 0):
        raise ValueError("ratings must contain finite, non-negative values")

    item_count = matrix.shape[1]
    similarities = np.zeros((item_count, item_count), dtype=np.float64)
    for left in range(item_count):
        for right in range(left, item_count):
            observed = (matrix[:, left] > 0) & (matrix[:, right] > 0)
            if not np.any(observed):
                continue
            left_values = matrix[observed, left]
            right_values = matrix[observed, right]
            denominator = np.linalg.norm(left_values) * np.linalg.norm(right_values)
            score = float(np.dot(left_values, right_values) / denominator)
            similarities[left, right] = score
            similarities[right, left] = score
    return similarities


def recommend(
    user_id: int,
    ratings: FloatMatrix,
    similarities: FloatMatrix,
    limit: int = 2,
) -> tuple[NDArray[np.int64], FloatMatrix]:
    """Rank only unrated items by a weighted sum of the user's known ratings."""
    matrix = np.asarray(ratings, dtype=np.float64)
    similarity_matrix = np.asarray(similarities, dtype=np.float64)
    if matrix.ndim != 2:
        raise ValueError("ratings must be a 2-D matrix")
    if user_id < 0 or user_id >= matrix.shape[0]:
        raise IndexError("user_id is outside ratings")
    if similarity_matrix.shape != (matrix.shape[1], matrix.shape[1]):
        raise ValueError("similarities shape must match the number of items")
    if limit < 1:
        raise ValueError("limit must be positive")

    user_ratings = matrix[user_id]
    candidate_items = np.flatnonzero(user_ratings == 0)
    candidate_scores = similarity_matrix[candidate_items] @ user_ratings
    order = np.argsort(-candidate_scores, kind="stable")[:limit]
    return candidate_items[order], candidate_scores[order]
