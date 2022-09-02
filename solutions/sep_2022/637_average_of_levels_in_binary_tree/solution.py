# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = [root]
        num_node_in_lv = len(queue)
        remaining_count = num_node_in_lv
        level_sum = 0
        lv_averages = []

        while len(queue):
            node = queue.pop(0)
            remaining_count -= 1
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if remaining_count == 0:
                lv_averages.append(level_sum / num_node_in_lv)
                num_node_in_lv = len(queue)
                remaining_count = num_node_in_lv
                level_sum = 0

        return lv_averages
