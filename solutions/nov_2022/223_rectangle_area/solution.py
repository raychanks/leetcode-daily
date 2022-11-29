class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        def get_overlapping_length(segment1, segment2):
            left_segment = segment1 if segment1[0] <= segment2[0] else segment2
            right_segment = segment2 if segment1[0] <= segment2[0] else segment1

            if right_segment[0] >= left_segment[1]:
                return 0

            if right_segment[1] <= left_segment[1]:
                return right_segment[1] - right_segment[0]

            return left_segment[1] - right_segment[0]

        total_area = (ay2 - ay1) * (ax2 - ax1) + (by2 - by1) * (bx2 - bx1)
        overlapping_area = get_overlapping_length(
            (ax1, ax2), (bx1, bx2)
        ) * get_overlapping_length((ay1, ay2), (by1, by2))

        return total_area - overlapping_area
