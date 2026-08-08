class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n // 5 > 0:
            zeros += n // 5
            n = n // 5
        return zeros
