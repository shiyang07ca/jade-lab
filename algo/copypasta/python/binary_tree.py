"""Binary-tree construction and traversal."""

from collections import deque
from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(slots=True)
class TreeNode[T]:
    value: T
    left: "TreeNode[T] | None" = None
    right: "TreeNode[T] | None" = None


def build_level_order[T](values: Sequence[T | None]) -> TreeNode[T] | None:
    """Build a tree from level-order values where ``None`` means no node."""
    if not values or values[0] is None:
        if any(value is not None for value in values[1:]):
            raise ValueError("a tree without a root cannot contain descendants")
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    index = 1
    while queue and index < len(values):
        node = queue.popleft()
        left = values[index]
        index += 1
        if left is not None:
            node.left = TreeNode(left)
            queue.append(node.left)
        if index < len(values):
            right = values[index]
            index += 1
            if right is not None:
                node.right = TreeNode(right)
                queue.append(node.right)
    if index < len(values) and any(value is not None for value in values[index:]):
        raise ValueError("level-order input contains unreachable nodes")
    return root


def preorder[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    result: list[T] = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return result


def inorder[T](root: TreeNode[T] | None) -> list[T]:
    result: list[T] = []
    stack: list[TreeNode[T]] = []
    current = root
    while current is not None or stack:
        while current is not None:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


def postorder[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    result: list[T] = []
    stack = [(root, False)]
    while stack:
        node, expanded = stack.pop()
        if expanded:
            result.append(node.value)
            continue
        stack.append((node, True))
        if node.right is not None:
            stack.append((node.right, False))
        if node.left is not None:
            stack.append((node.left, False))
    return result


def level_order[T](root: TreeNode[T] | None) -> list[T]:
    if root is None:
        return []
    result: list[T] = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return result
