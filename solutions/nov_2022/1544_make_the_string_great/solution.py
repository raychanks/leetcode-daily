from collections import deque


class Solution:
    def makeGood(self, s: str) -> str:
        stack = deque()

        for char in s:
            if not stack:
                stack.append(char)
                continue

            last = stack[-1]
            if char.lower() == last.lower() and char != last:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
