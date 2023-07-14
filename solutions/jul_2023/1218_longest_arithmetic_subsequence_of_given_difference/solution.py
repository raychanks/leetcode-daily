from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        indices = {}
        dp = [1] * n
        longest = 1

        for i in range(n - 1, -1, -1):
            next_num = arr[i] + difference

            if next_num in indices:
                idx = indices[next_num]
                dp[i] = dp[idx] + 1
                longest = max(longest, dp[i])

            indices[arr[i]] = i

        return longest
