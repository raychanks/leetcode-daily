from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        def solve(idx, prev_value):
            if idx == len(arr1):
                return 0

            cur_value = arr1[idx]
            # pick = len(arr1) + 1
            a, b = -1, -1

            if cur_value > prev_value:
                a = solve(idx + 1, cur_value)

                for num in arr2:
                    if num > prev_value:
                        b = 1 + solve(idx + 1, num)
                        break
            else:
                for num in arr2:
                    if num > prev_value:
                        b = 1 + solve(idx + 1, num)
                        break

            if a == -1 and b == -1:
                return -1
            if a == -1:
                return b
            if b == -1:
                return a
            return min(a, b)

        return solve(0, 0)

        # def solve(idx, prev_value, pick_count):
        #     if idx == len(arr1):
        #         return pick_count

        #     cur_value = arr1[idx]
        #     pick = len(arr1) + 1

        #     if cur_value > prev_value:
        #         pick = min(pick, solve(idx + 1, cur_value, pick_count))

        #         for num in arr2:
        #             if num > prev_value:
        #                 pick = min(pick, solve(idx + 1, num, pick_count + 1))
        #                 break
        #     else:
        #         for num in arr2:
        #             if num > prev_value:
        #                 pick = min(pick, solve(idx + 1, num, pick_count + 1))
        #                 break

        #     # if cur_value > prev_value, pick or not pick, greedy
        #     # else: must pick
        #     # if cannot pick, return -1
        #     return pick

        # result = solve(0, 0, 0)

        # return result if result != len(arr1) + 1 else -1


print(Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 3, 2, 4]))
print(Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[4, 3, 1]))
print(Solution().makeArrayIncreasing(arr1=[1, 5, 3, 6, 7], arr2=[1, 6, 3, 3]))
