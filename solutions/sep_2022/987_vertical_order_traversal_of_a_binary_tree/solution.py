from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        verticals = defaultdict(list)
        min_col, max_col = 0, 0

        def dfs(node, row, col):
            if not node:
                return

            nonlocal min_col, max_col
            min_col = min(min_col, col)
            max_col = max(max_col, col)

            verticals[col].append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        answer = []
        for col_idx in range(min_col, max_col + 1):
            sorted_col = sorted(verticals[col_idx], key=lambda x: (x[0], x[1]))
            answer.append([x[1] for x in sorted_col])

        return answer
