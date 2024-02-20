from typing import List


class Solution:
    def removeInterval(
        self, intervals: List[List[int]], toBeRemoved: List[int]
    ) -> List[List[int]]:
        result = []
        s2, e2 = toBeRemoved

        for s1, e1 in intervals:
            if e1 <= s2 or s1 >= e2:
                result.append([s1, e1])
                continue

            if s1 < s2:
                result.append([s1, s2])
            if e2 < e1:
                result.append([e2, e1])

        return result
