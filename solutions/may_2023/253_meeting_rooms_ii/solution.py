from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        events = []
        for start, end in intervals:
            events.append((start, 1))
            events.append((end, -1))
        events.sort()

        meeting_rooms = 0
        count = 0

        for _, diff in events:
            count += diff
            meeting_rooms = max(meeting_rooms, count)

        return meeting_rooms
