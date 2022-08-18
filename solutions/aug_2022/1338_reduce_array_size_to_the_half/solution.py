from collections import Counter
import heapq
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        freq_list = [num * -1 for num in counter.values()]
        heapq.heapify(freq_list)

        removed_len = 0
        result = 0
        while removed_len < len(arr) / 2:
            removed_len += heapq.heappop(freq_list) * -1
            result += 1

        return result
