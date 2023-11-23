from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        answer = [False] * len(l)

        for i, (left, right) in enumerate(zip(l, r)):
            if right - left < 1:
                continue

            seen = {nums[left]}
            local_min, local_max = nums[left], nums[left]

            for j in range(left + 1, right + 1):
                seen.add(nums[j])
                local_min = min(local_min, nums[j])
                local_max = max(local_max, nums[j])

            diff = (local_max - local_min) / (right - left)
            valid = True

            for k in range(right - left):
                if local_min + diff * (k + 1) not in seen:
                    valid = False
                    break

            answer[i] = valid

        return answer
