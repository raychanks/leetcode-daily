class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        def arithmetic_sum(initial, end):
            return (initial + end) * (end - initial + 1) // 2

        def get_sum(val):
            el_left = index
            el_right = n - index - 1
            num_first = max(val - el_left, 1) - 1
            num_last = max(val - el_right, 1) - 1

            s = (
                n
                + arithmetic_sum(num_first, val - 1)
                + arithmetic_sum(num_last, val - 1)
                - val
                + 1
            )

            return s

        result = 1

        left, right = 1, maxSum
        while left <= right:
            val = (left + right) // 2
            s = get_sum(val)

            if s <= maxSum:
                result = max(result, val)
                left = val + 1
            else:
                right = val - 1

        return result
