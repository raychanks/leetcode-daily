from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)

        if total < x:
            return -1
        if total == x:
            return len(nums)

        cur_sum = 0
        prefix_sum = [0]
        for num in nums:
            cur_sum += num
            prefix_sum.append(cur_sum)

        min_operations = len(nums)

        for i in range(len(nums)):
            prefix = prefix_sum[i]

            left, right = i, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                suffix = total - prefix_sum[mid]

                if prefix + suffix <= x:
                    right = mid - 1
                else:
                    left = mid + 1

            suffix = total - prefix_sum[left]
            if prefix + suffix == x:
                min_operations = min(min_operations, i + len(nums) - left)

        return min_operations if min_operations < len(nums) else -1
