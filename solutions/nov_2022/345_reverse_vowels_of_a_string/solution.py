class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        arr = list(s)
        vowels = {"a", "e", "i", "o", "u"}

        while left < right:
            if arr[left].lower() not in vowels:
                left += 1
                continue
            if arr[right].lower() not in vowels:
                right -= 1
                continue

            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

        return "".join(arr)
