class Solution:
    def minInsertions(self, s: str) -> int:
        dp = {}

        def solve(left, right):
            if left >= right:
                return 0

            state = (left, right)

            if state in dp:
                return dp[state]

            count = len(s)

            if s[left] == s[right]:
                count = min(count, solve(left + 1, right - 1))
            else:
                count = min(
                    count,
                    1 + solve(left + 1, right),
                    1 + solve(left, right - 1),
                )

            dp[state] = count

            return dp[state]

        return solve(0, len(s) - 1)
