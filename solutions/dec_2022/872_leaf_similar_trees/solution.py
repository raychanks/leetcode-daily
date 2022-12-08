# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_seq(root1) == self.get_seq(root2)

    def get_seq(self, node):
        seq = []

        def dfs(node):
            if node.left is None and node.right is None:
                seq.append(node.val)
                return

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

        dfs(node)

        return seq
