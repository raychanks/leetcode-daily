from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # -----
        # dfs
        # -----
        # def dfs(node):
        #     if node is None:
        #         return 0

        #     return 1 + max(dfs(node.left), dfs(node.right))

        # return dfs(root)

        # -----
        # bfs
        # -----
        if root is None:
            return 0

        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth
