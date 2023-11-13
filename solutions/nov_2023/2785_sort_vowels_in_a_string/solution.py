class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        vowel_indices = []
        vowel_chars = []

        for i, char in enumerate(s):
            if char in vowels:
                vowel_indices.append(i)
                vowel_chars.append(char)

        vowel_chars.sort(key=ord)
        s2 = list(s)

        for i, char in zip(vowel_indices, vowel_chars):
            s2[i] = char

        return "".join(s2)
