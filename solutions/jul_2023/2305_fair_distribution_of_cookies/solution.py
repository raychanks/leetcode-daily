from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        distributed = [0] * k
        min_unfairness = 10**9

        def dfs(i):
            nonlocal min_unfairness
            max_distributed = max(distributed)

            if max_distributed >= min_unfairness:
                return

            if i == len(cookies):
                min_unfairness = min(min_unfairness, max_distributed)
                return

            for j in range(k):
                distributed[j] += cookies[i]
                dfs(i + 1)
                distributed[j] -= cookies[i]

        dfs(0)

        return min_unfairness
