from collections import defaultdict
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # [in-degree, out-degree]
        degree_mapping = defaultdict(lambda: [0, 0])

        for a, b in trust:
            degree_mapping[a][1] += 1
            degree_mapping[b][0] += 1

        for i in range(1, n + 1):
            if degree_mapping[i] == [n - 1, 0]:
                return i

        return -1
