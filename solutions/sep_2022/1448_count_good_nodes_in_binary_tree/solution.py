# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def traverse(node: Optional[TreeNode], local_max: int) -> None:
            if not node:
                return

            nonlocal count

            if node.val >= local_max:
                count += 1

            local_max = max(local_max, node.val)
            traverse(node.left, local_max)
            traverse(node.right, local_max)

        traverse(root, root.val)

        return count
