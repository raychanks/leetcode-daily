from collections import defaultdict
from typing import List


class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        index_map = defaultdict(list)

        for i, word in enumerate(wordsDict):
            index_map[word].append(i)

        word1_indices = index_map[word1]
        word2_indices = index_map[word2]
        idx1, idx2 = 0, 0
        min_dist = len(wordsDict)

        while idx1 < len(word1_indices) and idx2 < len(word2_indices):
            i1, i2 = word1_indices[idx1], word2_indices[idx2]

            if i1 == i2:
                idx1 += 1
                continue

            if i1 < i2:
                min_dist = min(min_dist, i2 - i1)
                idx1 += 1
            else:
                min_dist = min(min_dist, i1 - i2)
                idx2 += 1

        return min_dist
