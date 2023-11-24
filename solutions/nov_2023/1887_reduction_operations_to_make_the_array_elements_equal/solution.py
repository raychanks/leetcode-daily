from collections import Counter
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        items = sorted([(num, freq) for num, freq in counter.items()], reverse=True)
        n = len(items)
        op = 0

        for i in range(n - 1):
            freq = items[i][1]
            op += freq * (n - 1 - i)

        return op
