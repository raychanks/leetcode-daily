from collections import deque
from typing import List


class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.children = []


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        nodes = [Node(node_id) for node_id in range(n)]

        for i, manager_id in enumerate(manager):
            if manager_id != -1:
                nodes[manager_id].children.append(i)

        queue: deque[tuple[Node, int]] = deque([(nodes[headID], 0)])
        time_needed = 0

        while queue:
            node, time_taken = queue.popleft()
            time_needed = max(time_needed, time_taken)

            for child_id in nodes[node.id].children:
                queue.append((nodes[child_id], time_taken + informTime[node.id]))

        return time_needed
