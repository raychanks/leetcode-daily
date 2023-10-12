class MountainArray:
    """
    This is MountainArray's API interface.
    You should not implement it, or speculate about its implementation
    """

    def __init__(self, arr):
        self.arr = arr
        self.call_count = 0

    def get(self, index: int) -> int:
        self.call_count += 1
        return self.arr[index]

    def length(self) -> int:
        return len(self.arr)


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: "MountainArray") -> int:
        n = mountain_arr.length()
        peak_index = self.get_peak_index(mountain_arr)

        left, right = 0, peak_index - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) >= target:
                right = mid - 1
            else:
                left = mid + 1

        if left < n and mountain_arr.get(left) == target:
            return left

        left, right = peak_index + 1, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) <= target:
                right = mid - 1
            else:
                left = mid + 1

        if left < n and mountain_arr.get(left) == target:
            return left

        return -1

    def get_peak_index(self, mountain_arr):
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if mid < n - 1 and mountain_arr.get(mid) > mountain_arr.get(mid + 1):
                right = mid - 1
            else:
                left = mid + 1

        return left
