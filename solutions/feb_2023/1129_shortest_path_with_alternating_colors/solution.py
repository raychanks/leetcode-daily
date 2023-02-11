from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(
        self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]
    ) -> List[int]:
        adj_list_red = defaultdict(list)
        adj_list_blue = defaultdict(list)
        answer = [-1] * n
        answer[0] = 0
        for a, b in redEdges:
            adj_list_red[a].append(b)

        for a, b in blueEdges:
            adj_list_blue[a].append(b)

        queue: deque[tuple[int, str, int]] = deque([(0, "red", 0), (0, "blue", 0)])
        visited_red = {0}
        visited_blue = {0}
        count = len(queue)

        while queue:
            for _ in range(count):
                node, color, distance = queue.popleft()

                if answer[node] == -1:
                    answer[node] = distance
                else:
                    answer[node] = min(answer[node], distance)

                if color == "red":
                    visited_red.add(node)

                    for adj in adj_list_blue[node]:
                        if adj in visited_blue:
                            continue

                        queue.append((adj, "blue", distance + 1))
                elif color == "blue":
                    visited_blue.add(node)

                    for adj in adj_list_red[node]:
                        if adj in visited_red:
                            continue

                        queue.append((adj, "red", distance + 1))

            count = len(queue)

        return answer
