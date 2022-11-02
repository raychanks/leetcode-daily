from collections import deque
from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        if start == end:
            return 0

        def difference(a, b):
            d = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    d += 1
            return d

        queue: deque[tuple[str, int]] = deque([(start, 0)])
        seen = {start}

        while queue:
            s, step = queue.popleft()

            if s == end:
                return step

            for gene in bank:
                if gene not in seen and difference(gene, s) == 1:
                    queue.append((gene, step + 1))
                    seen.add(s)

        return -1
