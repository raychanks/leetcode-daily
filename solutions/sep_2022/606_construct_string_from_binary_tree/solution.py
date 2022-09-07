# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        s = str(root.val)
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)

        if not left and not right:
            return s
        if not left:
            return f"{s}()({right})"
        if not right:
            return f"{s}({left})"
        return f"{s}({left})({right})"
