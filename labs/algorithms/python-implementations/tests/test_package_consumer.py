from jade_algorithms import DisjointSet, MatrixPrefixSum, sliding_window_max


def test_lab_consumes_only_the_package_public_interface() -> None:
    groups = DisjointSet(4)
    groups.union(0, 1)

    assert groups.connected(0, 1)
    assert sliding_window_max([4, 3, 5, 2], 2) == [4, 5, 5]
    assert MatrixPrefixSum([[1, 2], [3, 4]]).query(0, 0, 2, 2) == 10
