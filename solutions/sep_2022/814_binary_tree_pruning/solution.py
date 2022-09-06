# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return True

            left_prunable = dfs(node.left)
            right_prunable = dfs(node.right)

            if left_prunable:
                node.left = None
            if right_prunable:
                node.right = None

            return left_prunable and right_prunable and node.val == 0

        prunable = dfs(root)

        if prunable:
            return None

        return root
