from collections import deque


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        for char in s:
            if not stack or stack[-1] != char:
                stack.append(char)
            else:
                stack.pop()
        return "".join(stack)
