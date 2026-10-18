from leetgo_py import TreeNode
from solution import Solution


def test_lowest_common_ancestor() -> None:
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)
    node_4 = TreeNode(4)
    node_2 = TreeNode(2, node_7, node_4)
    node_5 = TreeNode(5, node_6, node_2)
    node_1 = TreeNode(1)
    root = TreeNode(3, node_5, node_1)

    solution = Solution()
    assert solution.lowestCommonAncestor(root, node_5, node_1) is root
    assert solution.lowestCommonAncestor(root, node_5, node_4) is node_5

    child = TreeNode(2)
    small_root = TreeNode(1, child)
    assert solution.lowestCommonAncestor(small_root, small_root, child) is small_root
