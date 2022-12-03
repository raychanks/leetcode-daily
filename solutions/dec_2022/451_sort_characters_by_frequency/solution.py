from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        arr = []

        for char, count in freq.most_common():
            arr.append(char * count)

        return "".join(arr)
