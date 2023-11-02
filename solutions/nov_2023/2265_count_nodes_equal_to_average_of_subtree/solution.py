from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return 0, 0

            left_subtree_sum, left_subtree_node_count = dfs(node.left)
            right_subtree_sum, right_subtree_node_count = dfs(node.right)

            subtree_sum = left_subtree_sum + right_subtree_sum + node.val
            node_count = left_subtree_node_count + right_subtree_node_count + 1

            if subtree_sum // node_count == node.val:
                count += 1

            return subtree_sum, node_count

        dfs(root)

        return count
