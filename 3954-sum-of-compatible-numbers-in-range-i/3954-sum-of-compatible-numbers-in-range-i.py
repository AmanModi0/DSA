class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        sum = 0
        for i in range(max(1, n - k), n + k + 1):
            if abs(n - i) <= k and n & i == 0:
                sum += i
        return sum
