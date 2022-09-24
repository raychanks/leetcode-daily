# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        cur_path = []

        def dfs(node, remaining):
            if not node:
                return

            if not node.left and not node.right and remaining == node.val:
                result.append(cur_path + [node.val])
                return

            cur_path.append(node.val)
            dfs(node.left, remaining - node.val)
            dfs(node.right, remaining - node.val)
            cur_path.pop()

        dfs(root, targetSum)

        return result
