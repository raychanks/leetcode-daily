from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        queue = [root]
        node_remaining = len(queue)
        level = 1

        while queue:
            node = queue.pop(0)
            node_remaining -= 1

            if level == depth - 1:
                left, right = node.left, node.right
                node.left = TreeNode(val, left)
                node.right = TreeNode(val, None, right)
                continue

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if node_remaining == 0:
                level += 1
                node_remaining = len(queue)

        return root
