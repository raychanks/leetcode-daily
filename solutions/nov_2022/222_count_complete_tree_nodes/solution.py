from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        node_left = root.left
        depth_left = 0
        while node_left:
            node_left = node_left.left
            depth_left += 1

        node_right = root.right
        depth_right = 0
        while node_right:
            node_right = node_right.right
            depth_right += 1

        if depth_left == depth_right:
            return 2 ** (depth_left + 1) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
