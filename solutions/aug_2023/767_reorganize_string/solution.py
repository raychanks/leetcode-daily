from collections import Counter
import math


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        frequencies = sorted(counter.items(), key=lambda x: x[1], reverse=True)

        if frequencies[0][1] > math.ceil(len(s) / 2):
            return ""

        result = [""] * len(s)
        idx = 0

        for char, freq in frequencies:
            for _ in range(freq):
                result[idx] = char

                idx += 2
                if idx >= len(s):
                    if len(s) % 2 == 0:
                        idx += 1
                    idx %= len(s)

        return "".join(result)
