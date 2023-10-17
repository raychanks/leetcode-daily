from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        possible_root = set(range(n))
        for child in leftChild:
            possible_root.discard(child)
        for child in rightChild:
            possible_root.discard(child)

        if len(possible_root) != 1:
            return False

        seen = [False] * n

        def dfs(node):
            if node == -1:
                return True
            if seen[node]:
                return False

            seen[node] = True

            return dfs(leftChild[node]) and dfs(rightChild[node])

        return dfs(possible_root.pop()) and all(seen)
