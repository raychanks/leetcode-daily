class Solution:
    def reverseWords(self, s: str) -> str:
        rev_word = ""
        rev_str = ""

        for char in s:
            if char == " ":
                rev_str = f"{rev_str} {rev_word}"
                rev_word = ""
            else:
                rev_word = char + rev_word

        return f"{rev_str} {rev_word}".strip()
