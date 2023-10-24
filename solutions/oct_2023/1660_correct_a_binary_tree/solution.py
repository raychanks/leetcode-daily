from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        parents = {}

        while queue:
            seen_in_level = {}

            for _ in range(len(queue)):
                node = queue.popleft()

                if node in seen_in_level:
                    from_node = seen_in_level[node]
                    from_node_parent = parents[from_node]

                    if from_node_parent.left is from_node:
                        from_node_parent.left = None
                    else:
                        from_node_parent.right = None

                    return root

                if node.left:
                    parents[node.left] = node
                    queue.append(node.left)

                if node.right:
                    parents[node.right] = node
                    seen_in_level[node.right] = node
                    queue.append(node.right)

        return root
