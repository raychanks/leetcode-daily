from typing import List


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        word_set = set(words)
        result = []

        for i in range(len(text)):
            for j in range(i + 1, len(text) + 1):
                s = text[i:j]

                if s in word_set:
                    result.append([i, j - 1])

        return result
