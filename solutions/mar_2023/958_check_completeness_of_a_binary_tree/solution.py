from typing import Deque, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = Deque([root])
        has_seen_none = False

        while queue:
            node = queue.popleft()

            if has_seen_none and node is not None:
                return False

            if not node:
                has_seen_none = True
                continue

            queue.append(node.left)
            queue.append(node.right)

        return True
