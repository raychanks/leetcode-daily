# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(
            root.right, targetSum - root.val
        )

    def hasPathSum_bfs(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue: list[tuple[TreeNode, int]] = [(root, 0)]
        while queue:
            node, acc = queue.pop(0)
            if not node.left and not node.right and acc + node.val == targetSum:
                return True
            if node.left:
                queue.append((node.left, acc + node.val))
            if node.right:
                queue.append((node.right, acc + node.val))

        return False
