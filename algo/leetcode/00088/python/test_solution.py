from solution import Solution


def test_merge_sorted_arrays() -> None:
    cases = [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
    ]
    for nums1, m, nums2, n, expected in cases:
        Solution().merge(nums1, m, nums2, n)
        assert nums1 == expected
