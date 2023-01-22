from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def is_palindrome(p):
            left, right = 0, len(p) - 1

            while left < right:
                if p[left] != p[right]:
                    return False

                left += 1
                right -= 1

            return True

        def backtack(idx):
            if idx == len(s):
                for p in part:
                    if not is_palindrome(p):
                        return

                result.append(tuple(part))
                return

            if part:
                last = part[-1]
                part[-1] = last + s[idx]
                backtack(idx + 1)
                part[-1] = last

            part.append(s[idx])
            backtack(idx + 1)
            part.pop()

        backtack(0)

        return result
