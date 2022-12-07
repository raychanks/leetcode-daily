# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def solve(node):
            if not node:
                return 0

            if low <= node.val <= high:
                return node.val + solve(node.left) + solve(node.right)

            if node.val < low:
                return solve(node.right)

            return solve(node.left)

        return solve(root)
