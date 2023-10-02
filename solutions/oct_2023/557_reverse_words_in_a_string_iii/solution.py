class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words_reversed = ["".join(reversed(word)) for word in words]
        return " ".join(words_reversed)
