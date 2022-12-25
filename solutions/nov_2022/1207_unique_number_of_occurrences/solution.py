from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_counter = Counter(arr)
        freq_set = set()

        for f in freq_counter.values():
            freq_set.add(f)

        return len(freq_counter) == len(freq_set)
