class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        power_of_2 = []
        num = 1
        while num <= 10**9:  # constraint: 1 <= n <= 10 ** 9
            power_of_2.append(num)
            num *= 2

        freq_combinations = set()
        for num in power_of_2:
            freq = self.get_freq(num)
            freq_combinations.add(freq)

        return self.get_freq(n) in freq_combinations

    def get_freq(self, num: int) -> str:
        digit_freq = [0] * 10
        for digit in str(num):
            digit_freq[int(digit)] += 1
        return ",".join([str(freq) for freq in digit_freq])
