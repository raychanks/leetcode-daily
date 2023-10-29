class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        num_tests = minutesToTest // minutesToDie

        for i in range(1001):
            if (num_tests + 1) ** i >= buckets:
                return i

        return -1
