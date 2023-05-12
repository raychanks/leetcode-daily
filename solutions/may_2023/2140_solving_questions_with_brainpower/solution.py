from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * (len(questions) + 1)

        for i in range(len(questions)):
            idx = len(questions) - 1 - i
            points, brainpower = questions[idx]

            if idx + brainpower + 1 < len(questions):
                points += dp[idx + brainpower + 1]

            dp[idx] = max(points, dp[idx + 1])

        return dp[0]
