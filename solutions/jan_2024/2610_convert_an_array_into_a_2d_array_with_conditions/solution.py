from collections import defaultdict
from typing import List


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        seen = defaultdict(int)
        result = []

        for num in nums:
            idx = seen[num]
            seen[num] += 1

            if idx < len(result):
                result[idx].append(num)
            else:
                result.append([num])

        return result
