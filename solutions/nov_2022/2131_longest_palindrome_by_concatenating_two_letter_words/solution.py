from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counter = Counter(words)
        length = 0
        same_taken = False

        for word in words:
            if word_counter[word] == 0:
                continue

            rev = word[::-1]
            word_counter[word] -= 1

            if word_counter[rev] > 0:
                length += 4
                word_counter[rev] -= 1
            elif word == rev and not same_taken:
                length += 2
                same_taken = True

        return length
