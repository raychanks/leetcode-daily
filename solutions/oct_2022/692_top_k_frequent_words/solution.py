from collections import Counter
import heapq
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequencies = Counter(words)
        max_heap = [(-freq, word) for word, freq in frequencies.items()]
        res = []

        heapq.heapify(max_heap)

        for _ in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res
