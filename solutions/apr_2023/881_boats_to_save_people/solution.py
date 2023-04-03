from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        picked = [False] * len(people)
        left, right = 0, len(people) - 1
        count = 0

        while left < right:
            light, heavy = people[left], people[right]

            if light + heavy <= limit:
                picked[left] = True
                picked[right] = True
                count += 1
                left += 1

            right -= 1

        for i, p in enumerate(picked):
            if people[i] > limit:
                break

            if not p:
                count += 1

        return count
