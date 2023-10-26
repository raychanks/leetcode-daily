from collections import defaultdict
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        arr.sort()
        num_set = set(arr)
        factors = defaultdict(list)

        for i in range(len(arr)):
            num = arr[i]

            for j in range(i):
                div, mod = divmod(num, arr[j])

                if mod == 0 and div in num_set:
                    factors[num].append((div, arr[j]))

        ways_by_num = defaultdict(int)

        for i in range(len(arr)):
            ways = 1

            for a, b in factors[arr[i]]:
                ways += ways_by_num[a] * ways_by_num[b]
                ways %= MOD

            ways_by_num[arr[i]] = ways

        return sum(ways_by_num.values()) % MOD
