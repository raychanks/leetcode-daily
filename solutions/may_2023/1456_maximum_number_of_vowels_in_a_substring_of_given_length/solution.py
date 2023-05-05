class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        left, right = 0, k
        max_count = 0

        for i in range(k):
            char = s[i]
            if char in vowels:
                max_count += 1

        count = max_count

        while right < len(s):
            incoming = s[right]
            outgoing = s[left]

            if incoming in vowels:
                count += 1
            if outgoing in vowels:
                count -= 1

            max_count = max(max_count, count)
            left += 1
            right += 1

        return max_count
