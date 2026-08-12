import numpy as np
import pytest

from item_recommendation import item_cosine_similarity, recommend


RATINGS = np.array(
    [
        [5, 3, 0, 1],
        [4, 0, 0, 1],
        [1, 1, 0, 5],
        [1, 0, 0, 4],
        [0, 1, 5, 4],
    ],
    dtype=np.float64,
)


def test_similarity_is_symmetric_and_keeps_unobserved_pair_at_zero() -> None:
    similarities = item_cosine_similarity(RATINGS)

    np.testing.assert_allclose(similarities, similarities.T)
    np.testing.assert_allclose(np.diag(similarities), np.ones(4))
    assert similarities[0, 2] == 0


def test_recommendation_never_returns_an_item_already_rated() -> None:
    similarities = item_cosine_similarity(RATINGS)

    items, scores = recommend(0, RATINGS, similarities)

    assert items.tolist() == [2]
    assert scores.shape == (1,)


@pytest.mark.parametrize(
    "ratings",
    [np.array([1, 2, 3]), np.array([[1, -1]]), np.array([[1, np.nan]])],
)
def test_rejects_invalid_rating_matrices(ratings: np.ndarray) -> None:
    with pytest.raises(ValueError):
        item_cosine_similarity(ratings)


def test_rejects_similarity_shape_mismatch() -> None:
    with pytest.raises(ValueError, match="shape"):
        recommend(0, RATINGS, np.eye(3))
