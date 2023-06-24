from collections import defaultdict
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def get_dp(halves):
            states = {(0, 0)}
            dp = defaultdict(int)

            for num in halves:
                tmp_states = set()

                for left, right in states:
                    add_to_left = (left + num, right)
                    add_to_right = (left, right + num)
                    skip = (left, right)

                    tmp_states.add(add_to_left)
                    tmp_states.add(add_to_right)
                    tmp_states.add(skip)

                states = states.union(tmp_states)

            for left, right in states:
                diff = left - right
                dp[diff] = max(dp[diff], left)

            return dp

        left_dp = get_dp(rods[: len(rods) // 2])
        right_dp = get_dp(rods[len(rods) // 2 :])

        max_height = 0

        for diff in left_dp:
            if -diff in right_dp:
                max_height = max(max_height, left_dp[diff] + right_dp[-diff])

        return max_height
