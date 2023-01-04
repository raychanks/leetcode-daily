from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        step = 0
        counts = Counter(tasks)

        for val in counts.values():
            if val == 1:
                return -1

            step += val // 3

            if val % 3 != 0:
                step += 1

        return step
