class Solution:
    def partitionString(self, s: str) -> int:
        i = 0
        count = 1
        seen = [False] * 26

        while i < len(s):
            char_idx = ord(s[i]) - ord("a")

            if seen[char_idx]:
                seen = [False] * 26
                count += 1
                continue

            seen[char_idx] = True
            i += 1

        return count
