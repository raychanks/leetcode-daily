class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        left, right = 0, len(palindrome) - 1
        palindrome_arr = list(palindrome)

        while left < right:
            if palindrome_arr[left] != "a":
                palindrome_arr[left] = "a"
                return "".join(palindrome_arr)

            left += 1
            right -= 1

        palindrome_arr[-1] = "a" if palindrome[-1] != "a" else "b"

        return "".join(palindrome_arr)
