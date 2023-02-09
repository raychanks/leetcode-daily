from collections import defaultdict
from typing import List


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        idea_set = set(ideas)
        groups = defaultdict(list)
        result = 0
        processed = set()

        for idea in ideas:
            group = idea[0]
            groups[group].append(idea)

        for k1, v1 in groups.items():
            processed.add(k1)

            for k2, v2 in groups.items():
                if k2 in processed:
                    continue

                c1, c2 = 0, 0

                for idea1 in v1:
                    swapped1 = k2 + idea1[1:]

                    if swapped1 in idea_set:
                        continue

                    c1 += 1

                for idea2 in v2:
                    swapped2 = k1 + idea2[1:]

                    if swapped2 in idea_set:
                        continue

                    c2 += 1

                result += c1 * c2

        return result * 2
