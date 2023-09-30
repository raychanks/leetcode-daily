class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_len = 0
        for char in s:
            if char.isdigit():
                decoded_len *= int(char)
            else:
                decoded_len += 1

        for char in reversed(s):
            k %= decoded_len

            if k == 0 and char.isalpha():
                return char

            if char.isdigit():
                decoded_len //= int(char)
            else:
                decoded_len -= 1

        return ""
