from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root)

    def recurse(
        self,
        node,
        min_val=float("-inf"),
        max_val=float("inf"),
    ):
        if node is None:
            return True

        if node.val <= min_val or node.val >= max_val:
            return False

        return self.recurse(node.left, min_val, node.val) and self.recurse(
            node.right, node.val, max_val
        )
