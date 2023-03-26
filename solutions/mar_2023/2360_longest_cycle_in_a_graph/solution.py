from collections import Counter, deque
from typing import List


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        counter = Counter()

        for i, dest in enumerate(edges):
            if i not in counter:
                counter[i] = 0

            if dest != -1:
                counter[dest] += 1

        zero_in_deg = deque()
        non_cyclic = set()

        for node, v in counter.items():
            if v == 0:
                zero_in_deg.append(node)

        while zero_in_deg:
            node = zero_in_deg.popleft()
            non_cyclic.add(node)
            counter[node] -= 1
            destination = edges[node]
            counter[destination] -= 1

            if counter[destination] == 0:
                zero_in_deg.append(destination)

        cyclic_nodes = set(range(len(edges))) - non_cyclic

        if not cyclic_nodes:
            return -1

        queue = deque()
        max_count = 0
        seen = set()

        for node in cyclic_nodes:
            if node in seen:
                continue

            queue.append(node)
            count = 0

            while queue:
                n = queue.popleft()

                if n in seen:
                    continue

                destination = edges[n]
                seen.add(n)
                queue.append(destination)
                count += 1

            max_count = max(max_count, count)

        return max_count
