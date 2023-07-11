from collections import defaultdict, deque
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]

        adj_list = defaultdict(list)

        def dfs(node, prev):
            if not node:
                return

            if prev:
                adj_list[node.val].append(prev)
            if node.left:
                adj_list[node.val].append(node.left)
                dfs(node.left, node)
            if node.right:
                adj_list[node.val].append(node.right)
                dfs(node.right, node)

        dfs(root, None)

        seen = {target.val}
        queue = deque([target.val])
        distance = 1

        while queue:
            for _ in range(len(queue)):
                val = queue.popleft()

                for adj in adj_list[val]:
                    if adj.val not in seen:
                        seen.add(adj.val)
                        queue.append(adj.val)

            if distance == k:
                return list(queue)

            distance += 1

        return []
