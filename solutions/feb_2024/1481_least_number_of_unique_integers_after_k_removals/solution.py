from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        frequencies = sorted(counter.items(), key=lambda item: item[1])
        removed_count = 0

        for _, freq in frequencies:
            if k >= freq:
                k -= freq
                removed_count += 1
            else:
                break

        return len(frequencies) - removed_count
