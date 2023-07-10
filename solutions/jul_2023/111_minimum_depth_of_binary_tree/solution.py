from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, depth):
            if not node.left and not node.right:
                return depth

            min_depth = 10**9

            if node.left:
                min_depth = min(min_depth, dfs(node.left, depth + 1))

            if node.right:
                min_depth = min(min_depth, dfs(node.right, depth + 1))

            return min_depth

        return dfs(root, 1)
