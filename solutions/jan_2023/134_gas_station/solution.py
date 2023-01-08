from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        diffs = [g - cost[i] for i, g in enumerate(gas)]
        ptr = 0
        cur_gas = 0
        n = len(diffs)

        for i in range(2 * n):
            if i - ptr == n:
                return ptr % n

            idx = i % n

            if cur_gas < 0:
                cur_gas = diffs[idx]
                ptr = i
            else:
                cur_gas += diffs[idx]

        return ptr % n
