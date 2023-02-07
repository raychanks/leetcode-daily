from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counter = Counter()
        max_len = 0
        length = 0
        left, right = 0, 0

        while right < len(fruits):
            if len(counter) < 2 or fruits[right] in counter:
                counter[fruits[right]] += 1
                right += 1
                length += 1
                max_len = max(max_len, length)
                continue

            while len(counter) == 2:
                fruit = fruits[left]
                counter[fruit] -= 1
                length -= 1

                if counter[fruit] == 0:
                    del counter[fruit]

                left += 1

        return max_len
