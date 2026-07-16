import pytest

from btree import BTree


@pytest.mark.parametrize(
    ("order", "values"),
    [
        (3, list(reversed(range(10)))),
        (3, list(range(10))),
        (3, [31, 7, 19, 3, 43, 11, 23, 5, 37, 13]),
        (8, [89, 13, 55, 2, 34, 21, 144, 8, 5, 3, 1, 233]),
    ],
)
def test_insert_preserves_sorted_order(order: int, values: list[int]) -> None:
    tree = BTree(order)

    for value in values:
        tree = tree.insert({"key": value, "value": value})

    assert [element["key"] for element in tree.list()] == sorted(values)


def test_contains_inserted_keys() -> None:
    tree = BTree(4)
    values = [17, 4, 29, 1, 9, 23]

    for value in values:
        tree = tree.insert({"key": value, "value": value})

    assert all(tree.contains(value) for value in values)
    assert not tree.contains(999)
