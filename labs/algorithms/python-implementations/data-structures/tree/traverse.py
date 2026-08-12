r"""

















"""


class Node:
    # value = None

    def __init__(self, data, left=None, right=None):
        self.value = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.value}>"


import unittest


def pre_order_recur(root, ans=[]):
    if root is None:
        return

    # print(root.value + " ")
    ans.append(root.value)
    pre_order_recur(root.left, ans)
    pre_order_recur(root.right, ans)

    return ans


def in_order_recur(root, ans=[]):
    if root is None:
        return

    in_order_recur(root.left, ans)
    # print(root.value + " ")
    ans.append(root.value)
    in_order_recur(root.right, ans)

    return ans


def pos_order_recur(root, ans=[]):
    if root is None:
        return

    pos_order_recur(root.left, ans)
    pos_order_recur(root.right, ans)
    # print(root.value + " ")
    ans.append(root.value)

    return ans


def pre_order_iter(root):
    if root is None:
        return

    stack = [root]
    ans = []
    while stack:
        cur = stack.pop()
        ans.append(cur.value)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)

    return ans


def in_order_iter(root):
    if root is None:
        return

    stack = []
    ans = []
    while root or stack:
        print(stack)
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            ans.append(node.value)
            root = node.right

    return ans


def pos_order_iter1(root):
    if root is None:
        return

    stack1, stack2 = [root], []

    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)

    ans = []
    while stack2:
        ans.append(stack2.pop().value)

    return ans


def pos_order_iter2(root):
    if root is None:
        return

    ans = []
    h = root
    c = None
    stack = [h]
    while stack:
        c = stack[-1]
        if c.left and h != c.left and h != c.right:
            stack.append(c.left)
        elif c.right and h != c.right:
            stack.append(c.right)
        else:
            ans.append(stack.pop().value)
            h = c

    return ans


# 层序遍历
# 广度优先遍历
def bfs(root):
    if root is None:
        return

    queue = [root]
    ans = []
    while queue:
        cur = queue.pop(0)
        ans.append(cur.value)
        if cur.left:
            queue.append(cur.left)
        if cur.right:
            queue.append(cur.right)

    return ans


def bfs2(root):
    if root is None:
        return

    queue = [root]
    ans = []
    while queue:
        for _ in range(len(queue)):
            cur = queue.pop(0)
            ans.append(cur.value)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

    return ans


r"""
         a
      /      \
     b         c
   /   \     /   \
  d     e   f      g

"""


class TestRecur(unittest.TestCase):
    def test(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        a.left = b
        a.right = c

        self.assertEqual(
            ["a", "b", "d", "e", "c", "f", "g"],
            pre_order_recur(a),
        )

        self.assertEqual(
            ["d", "b", "e", "a", "f", "c", "g"],
            in_order_recur(a),
        )

        self.assertEqual(
            ["d", "e", "b", "f", "g", "c", "a"],
            pos_order_recur(a),
        )


class TestIter(unittest.TestCase):
    def test(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")

        b.left = d
        b.right = e

        c.left = f
        c.right = g

        a.left = b
        a.right = c

        self.assertEqual(
            ["a", "b", "d", "e", "c", "f", "g"],
            pre_order_iter(a),
        )

        self.assertEqual(
            ["d", "b", "e", "a", "f", "c", "g"],
            in_order_iter(a),
        )

        self.assertEqual(
            ["d", "e", "b", "f", "g", "c", "a"],
            pos_order_iter1(a),
        )

        self.assertEqual(
            ["d", "e", "b", "f", "g", "c", "a"],
            pos_order_iter2(a),
        )

        self.assertEqual(
            ["a", "b", "c", "d", "e", "f", "g"],
            bfs(a),
        )
        self.assertEqual(
            ["a", "b", "c", "d", "e", "f", "g"],
            bfs2(a),
        )

        print(bfs2(a))


if __name__ == "__main__":
    unittest.main()
