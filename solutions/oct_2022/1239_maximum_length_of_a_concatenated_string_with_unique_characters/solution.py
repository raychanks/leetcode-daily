from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        seen = [False] * 26

        def backtrack(idx):
            if idx >= len(arr):
                return len([s for s in seen if s])

            is_unique = True
            for char in arr[idx]:
                i = ord(char) - ord("a")
                if seen[i]:
                    is_unique = False
                    break

            len1, len2 = backtrack(idx + 1), 0
            if is_unique and len(set(arr[idx])) == len(arr[idx]):
                for char in arr[idx]:
                    i = ord(char) - ord("a")
                    seen[i] = True

                len2 = backtrack(idx + 1)

                for char in arr[idx]:
                    i = ord(char) - ord("a")
                    seen[i] = False

            return max(len1, len2)

        return backtrack(0)
