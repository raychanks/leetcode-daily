from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        result = []

        for char, freq in counter.most_common():
            result.append(char * freq)

        return "".join(result)
