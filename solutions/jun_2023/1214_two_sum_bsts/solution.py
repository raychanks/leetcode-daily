from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def twoSumBSTs(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int
    ) -> bool:
        queue = deque([root1])

        while queue:
            node = queue.popleft()

            if not node:
                continue

            queue.append(node.left)
            queue.append(node.right)

            if search(root2, target - node.val):
                return True

        return False


def search(node: Optional[TreeNode], target: int) -> bool:
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return search(node.left, target)
    return search(node.right, target)
