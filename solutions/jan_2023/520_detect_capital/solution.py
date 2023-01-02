class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upper_count = 0
        lower_count = 0

        for char in word:
            if char.isupper():
                upper_count += 1
            else:
                lower_count += 1

        if upper_count == len(word) or lower_count == len(word):
            return True

        if upper_count == 1 and word[0].isupper():
            return True

        return False
