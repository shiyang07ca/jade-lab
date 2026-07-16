from log import log_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"<{self.val}>"

    # def __eq__(self, other):
    #     return self.val == other.val

    def log(self):
        # print("call log")
        log_tree(self, val="val", left="left", right="right")
