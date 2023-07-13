from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degrees = Counter()
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            in_degrees[a] += 1
            adj_list[b].append(a)

        finished_count = 0
        remove_candidates = deque()

        for i in range(numCourses):
            if in_degrees[i] == 0:
                remove_candidates.append(i)

        while remove_candidates:
            i = remove_candidates.popleft()
            finished_count += 1

            for adj in adj_list[i]:
                in_degrees[adj] -= 1
                if in_degrees[adj] == 0:
                    remove_candidates.append(adj)

        return finished_count == numCourses
