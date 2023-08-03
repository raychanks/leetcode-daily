from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combinations = []
        letters = []

        def backtrack(idx):
            if idx == len(digits):
                combinations.append("".join(letters))
                return

            for letter in mapping[digits[idx]]:
                letters.append(letter)
                backtrack(idx + 1)
                letters.pop()

        backtrack(0)

        return combinations
