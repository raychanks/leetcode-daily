from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        ##########
        # dp
        ##########
        # n = len(nums)
        # dp = [n] * n
        # dp[-1] = 0

        # for i in range(n - 2, -1, -1):
        #     step = nums[i]
        #     min_step = n
        #     for j in range(i + 1, min(n, i + step + 1)):
        #         min_step = min(min_step, dp[j])
        #     dp[i] = min_step + 1

        # return dp[0] if dp[0] < n else -1

        ##########
        # greedy
        ##########
        n = len(nums)
        idx = 0
        count = 0

        if n == 1:
            return 0

        for _ in range(n):
            step = nums[idx]

            if idx == n - 1:
                return count
            if idx + step >= n - 1:
                return count + 1

            count += 1
            max_reach = 0
            max_reach_idx = idx

            for j in range(idx + 1, min(n, idx + step + 1)):
                if j + nums[j] > max_reach:
                    max_reach = j + nums[j]
                    max_reach_idx = j

            idx = max_reach_idx

        return -1
