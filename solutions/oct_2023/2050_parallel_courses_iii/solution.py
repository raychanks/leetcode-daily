from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj_list = defaultdict(list)
        in_degrees = Counter()

        for u, v in relations:
            adj_list[u].append(v)
            in_degrees[v] += 1

        prerequisite_time = Counter()
        zero_in_degrees = deque([])
        for i in range(1, n + 1):
            if in_degrees[i] == 0:
                zero_in_degrees.append(i)

        min_time = 0

        while zero_in_degrees:
            node = zero_in_degrees.popleft()

            if not adj_list[node]:
                min_time = max(min_time, prerequisite_time[node] + time[node - 1])

            for adj in adj_list[node]:
                prerequisite_time[adj] = max(
                    prerequisite_time[adj], prerequisite_time[node] + time[node - 1]
                )
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    zero_in_degrees.append(adj)

        return min_time
