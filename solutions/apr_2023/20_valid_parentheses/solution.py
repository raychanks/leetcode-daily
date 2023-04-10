class Solution:
    def isValid(self, s: str) -> bool:
        pair_map = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        stack = []

        for char in s:
            if not stack or char in {"(", "[", "{"}:
                stack.append(char)
                continue

            if pair_map[char] != stack[-1]:
                return False

            stack.pop()

        return not stack
