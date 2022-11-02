# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root or (not root.left and not root.right):
            return False

        node_map = {}
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node_map[node.val] = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        queue.append(root)
        while queue:
            node = queue.popleft()
            complement = k - node.val
            if complement in node_map and k != node.val * 2:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False
