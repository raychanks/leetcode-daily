# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ---------
        # iterative
        # ---------
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                continue

            result.append(node.val)

            if node.right:
                queue.appendleft(node.right)
            if node.left:
                queue.appendleft(node.left)

        return result

        # ---------
        # recursive
        # ---------
        # result = []

        # def dfs(node):
        #     if not node:
        #         return

        #     result.append(node.val)

        #     dfs(node.left)
        #     dfs(node.right)

        # dfs(root)

        # return result
