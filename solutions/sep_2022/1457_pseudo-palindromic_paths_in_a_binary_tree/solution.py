# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        num_path = 0
        counts = [0] * 10

        def dfs(node: Optional[TreeNode]):
            if not node:
                return

            nonlocal num_path

            counts[node.val] += 1

            if not node.left and not node.right:
                odd_count = len([num for num in counts if num % 2 != 0])

                if odd_count <= 1:
                    num_path += 1

                counts[node.val] -= 1
                return

            dfs(node.left)
            dfs(node.right)
            counts[node.val] -= 1

        dfs(root)

        return num_path
