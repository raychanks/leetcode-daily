class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowel_count = 0
        half_len = len(s) // 2

        for i in range(half_len):
            if s[i] in vowels:
                vowel_count += 1

        for i in range(half_len, len(s)):
            if s[i] in vowels:
                vowel_count -= 1

        return vowel_count == 0
