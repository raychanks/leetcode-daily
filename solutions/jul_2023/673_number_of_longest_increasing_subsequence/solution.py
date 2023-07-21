from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp: list[tuple[int, int]] = [(1, 1)] * len(nums)
        max_len = 1

        for i, num in enumerate(nums):
            cur_len = 1
            total_count = 1

            for j in range(0, i):
                if nums[j] >= num:
                    continue

                run_len, count = dp[j]

                if run_len + 1 > cur_len:
                    total_count = count
                    cur_len = run_len + 1
                elif run_len + 1 == cur_len:
                    total_count += count

            dp[i] = (cur_len, total_count)
            max_len = max(max_len, cur_len)

        result = 0
        for l, c in dp:
            if l == max_len:
                result += c

        return result
