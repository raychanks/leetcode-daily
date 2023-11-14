class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        num_letters = 26
        n = len(s)
        first_occurance = [n] * num_letters
        last_occurance = [-1] * num_letters

        for i, char in enumerate(s):
            j = ord(char) - ord("a")
            first_occurance[j] = min(first_occurance[j], i)
            last_occurance[j] = max(last_occurance[j], i)

        palindromes = set()

        for i in range(1, n - 1):
            for j in range(num_letters):
                if len(palindromes) == num_letters**2:
                    return len(palindromes)

                if first_occurance[j] == n or last_occurance[j] == -1:
                    continue

                if first_occurance[j] < i and last_occurance[j] > i:
                    char = chr(ord("a") + j)
                    palindromes.add(char + s[i] + char)

        return len(palindromes)
