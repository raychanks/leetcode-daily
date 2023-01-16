# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
# 	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
# 	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
# 	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
# 	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
# 	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: "ArrayReader") -> int:
        left, right = 0, reader.length()

        while left < right:
            is_even = (right - left) % 2 == 0
            mid = (left + right) // 2

            if is_even:
                compare_result = reader.compareSub(left, mid - 1, mid, right - 1)

                if compare_result == 0:
                    raise RuntimeError

                if compare_result == 1:
                    right = mid
                elif compare_result == -1:
                    left = mid
            else:
                compare_result = reader.compareSub(left, mid, mid, right - 1)

                if compare_result == 0:
                    return mid

                if compare_result == 1:
                    right = mid
                else:
                    left = mid

        return left
