from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i, j = 0, 0

        while i < len(pushed):
            if not stack:
                stack.append(pushed[i])
                i += 1
                continue

            if stack[-1] != popped[j]:
                stack.append(pushed[i])
                i += 1
            else:
                stack.pop()
                j += 1

        while j < len(popped):
            if stack[-1] != popped[j]:
                return False

            stack.pop()
            j += 1

        return True
