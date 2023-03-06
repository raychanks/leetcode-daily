from typing import List


class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if len(words) != len(words[0]):
            return False

        for i in range(len(words)):
            for j in range(len(words[i])):
                if j >= len(words) or i >= len(words[j]):
                    return False

                if words[i][j] != words[j][i]:
                    return False

        return True
