class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches_played = 0

        while n > 1:
            matches_played += n // 2

            if n % 2 == 0:
                n //= 2
            else:
                n = n // 2 + 1

        return matches_played
