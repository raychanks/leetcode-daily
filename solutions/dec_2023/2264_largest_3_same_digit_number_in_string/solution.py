class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = "-1"
        left = 0

        for right in range(1, len(num)):
            if num[left] != num[right]:
                if right - left > 2 and int(num[left] * 3) > int(largest):
                    largest = num[left] * 3
                left = right

        if len(num) - left > 2 and int(num[left] * 3) > int(largest):
            largest = num[left] * 3

        return largest if largest != "-1" else ""
