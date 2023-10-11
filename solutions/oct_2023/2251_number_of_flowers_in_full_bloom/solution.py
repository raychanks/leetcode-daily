from typing import List


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        events = []
        for start, end in flowers:
            events.append((start, 1))
            events.append((end + 1, -1))
        events.sort()

        blooms = []
        count = 0
        for time, change in events:
            count += change
            blooms.append((time, count))

        answer = []
        for time in people:
            left, right = 0, len(blooms) - 1
            while left <= right:
                mid = (left + right) // 2
                if blooms[mid][0] > time:
                    right = mid - 1
                else:
                    left = mid + 1

            answer.append(blooms[left - 1][1])

        return answer
