from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levels_min = {}
        levels_max = {}
        max_level = 0

        def dfs(node, level, val):
            if not node:
                return

            nonlocal levels_min, levels_max, max_level

            max_level = max(max_level, level)

            if level not in levels_min:
                levels_min[level] = val
            else:
                levels_min[level] = min(levels_min[level], val)

            if level not in levels_max:
                levels_max[level] = val
            else:
                levels_max[level] = max(levels_max[level], val)

            dfs(node.left, level + 1, val * 2)
            dfs(node.right, level + 1, val * 2 + 1)

        dfs(root, 1, 0)

        max_width = 0

        for level in range(1, max_level + 1):
            max_width = max(max_width, 1 + levels_max[level] - levels_min[level])

        return max_width
