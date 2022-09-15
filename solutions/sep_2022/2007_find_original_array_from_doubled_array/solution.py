from collections import defaultdict
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []

        index_map: defaultdict[int, list[int]] = defaultdict(list)
        result: list[int] = []
        seen = [False] * len(changed)
        changed.sort()

        for i, num in enumerate(changed):
            index_map[num].append(i)

        for i, num in enumerate(changed):
            if seen[i]:
                continue

            double = num * 2

            if not len(index_map[double]):
                return []

            idx = index_map[double].pop()
            seen[i] = True
            seen[idx] = True
            result.append(num)

        return result
