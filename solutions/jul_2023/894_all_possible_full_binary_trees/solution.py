from functools import cache
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode(0)]

        result = []

        for i in range(2, n, 2):
            for left_sub_tree in self.allPossibleFBT(n - i):
                for right_sub_tree in self.allPossibleFBT(i - 1):
                    result.append(TreeNode(0, left_sub_tree, right_sub_tree))

        return result
