from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node.left is None and node.right is None:
                # min, max, diff
                return (node.val, node.val, 0)

            min_val, max_val, diff = 10**5, 0, 0

            if node.left:
                res = dfs(node.left)
                min_val = min(node.val, min_val, res[0])
                max_val = max(node.val, max_val, res[1])
                diff = max(
                    diff, abs(node.val - min_val), abs(node.val - max_val), res[2]
                )

            if node.right:
                res = dfs(node.right)
                min_val = min(node.val, min_val, res[0])
                max_val = max(node.val, max_val, res[1])
                diff = max(
                    diff, abs(node.val - min_val), abs(node.val - max_val), res[2]
                )

            return (min_val, max_val, diff)

        return dfs(root)[2]
