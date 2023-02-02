from collections import defaultdict
from typing import List


class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        similar_map = defaultdict(set)

        for a, b in similarPairs:
            similar_map[a].add(b)
            similar_map[b].add(a)

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2:
                continue

            if word2 not in similar_map[word1]:
                return False

        return True
