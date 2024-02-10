from functools import cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            count += 1

            for span in range(1, len(s) - 1):
                left, right = i - span, i + span

                if left < 0 or right >= len(s):
                    break

                if s[left] == s[right]:
                    count += 1
                else:
                    break

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                continue

            count += 1

            for span in range(1, len(s) - 1):
                left, right = i - span, i + span + 1

                if left < 0 or right >= len(s):
                    break

                if s[left] == s[right]:
                    count += 1
                else:
                    break

        return count
