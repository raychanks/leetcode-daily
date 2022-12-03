from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)

        freq1 = [v for v in counter1.values()]
        freq2 = [v for v in counter2.values()]

        return sorted(freq1) == sorted(freq2) and counter1.keys() == counter2.keys()
