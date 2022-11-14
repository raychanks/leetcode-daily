from collections import defaultdict
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        groups = defaultdict(list)
        counter = 0

        for x, y in stones:
            lies_in_groups = []

            for group_idx, group in groups.items():
                for x2, y2 in group:
                    if x == x2 or y == y2:
                        lies_in_groups.append(group_idx)
                        break

            if not lies_in_groups:
                groups[counter].append((x, y))
                counter += 1
            elif len(lies_in_groups) == 1:
                idx = lies_in_groups[0]
                groups[idx].append((x, y))
            else:
                idx = lies_in_groups[0]
                for i in lies_in_groups[1:]:
                    groups[idx].extend(groups[i])
                    del groups[i]

        return len(stones) - len(groups)
