from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node, cur_val):
            nonlocal answer

            if node.left is None and node.right is None:
                answer += cur_val * 10 + node.val
                return

            next_val = cur_val * 10 + node.val

            if node.left:
                dfs(node.left, next_val)

            if node.right:
                dfs(node.right, next_val)

        dfs(root, 0)

        return answer
