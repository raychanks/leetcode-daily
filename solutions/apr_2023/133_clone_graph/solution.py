from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        if node is None:
            return None

        nodes = {1: Node(1)}
        queue = deque([node])
        visited = set()

        while queue:
            next_node = queue.popleft()

            if next_node.val in visited:
                continue

            visited.add(next_node.val)

            for neighbor in next_node.neighbors:
                if neighbor.val not in nodes:
                    nodes[neighbor.val] = Node(neighbor.val)

                nodes[next_node.val].neighbors.append(nodes[neighbor.val])
                queue.append(neighbor)

        return nodes[1]
