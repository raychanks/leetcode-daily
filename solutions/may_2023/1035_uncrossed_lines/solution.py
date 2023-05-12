from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = {}

        def solve(i, j):
            state = (i, j)

            if state in dp:
                return dp[state]

            if i == len(nums1) or j == len(nums2):
                return 0

            if nums1[i] == nums2[j]:
                dp[state] = max(
                    1 + solve(i + 1, j + 1),
                    solve(i + 1, j),
                    solve(i, j + 1),
                )
            else:
                dp[state] = max(solve(i + 1, j), solve(i, j + 1))

            return dp[state]

        solve(0, 0)

        return dp[(0, 0)]
