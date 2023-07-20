from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            should_add = True

            while stack:
                if stack[-1] < 0 or asteroid > 0:
                    stack.append(asteroid)
                    should_add = False
                    break

                if stack[-1] == -asteroid:
                    stack.pop()
                    should_add = False
                    break

                if stack[-1] > -asteroid:
                    should_add = False
                    break

                stack.pop()

            if should_add:
                stack.append(asteroid)

        return stack
