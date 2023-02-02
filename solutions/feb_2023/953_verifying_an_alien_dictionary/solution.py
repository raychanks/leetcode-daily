from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {char: idx for idx, char in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            shorter_len = min(len(word1), len(word2))

            for j in range(shorter_len):
                char1, char2 = word1[j], word2[j]

                if order_map[char1] < order_map[char2]:
                    break

                if order_map[char1] > order_map[char2]:
                    return False
            else:
                if len(word1) > len(word2):
                    return False

        return True
