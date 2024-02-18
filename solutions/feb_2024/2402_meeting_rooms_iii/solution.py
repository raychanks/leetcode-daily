import heapq
from typing import List


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])
        current_time = 0
        meetings_held = [0] * n

        available = list(range(n))
        heapq.heapify(available)

        # (release_at, room_number)
        in_use = []

        for start, end in meetings:
            current_time = start

            while in_use and in_use[0][0] <= current_time:
                _, released_room = heapq.heappop(in_use)
                heapq.heappush(available, released_room)

            if not available:
                current_time = in_use[0][0]
                _, released_room = heapq.heappop(in_use)
                heapq.heappush(available, released_room)

            room = heapq.heappop(available)
            meetings_held[room] += 1
            heapq.heappush(in_use, (current_time + (end - start), room))

        max_meeting_room = -1
        max_meeting_held = -1
        for i, held in enumerate(meetings_held):
            if held > max_meeting_held:
                max_meeting_held = held
                max_meeting_room = i

        return max_meeting_room
