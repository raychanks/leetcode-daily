class Solution:
    def totalMoney(self, n: int) -> int:
        def arithmetic_sum(initial, diff, terms):
            last = initial + diff * (terms - 1)
            return (initial + last) * terms // 2

        rounds, last_day = divmod(n, 7)
        total = 0

        for i in range(1, 8):
            if i <= last_day:
                total += arithmetic_sum(i, 1, rounds + 1)
            else:
                total += arithmetic_sum(i, 1, rounds)

        return total
