from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur_num = nums[0]
        count = 1

        for num in nums[1:]:
            if num == cur_num:
                count += 1
            else:
                count -= 1
                if count < 0:
                    cur_num = num
                    count = 1

        return cur_num
