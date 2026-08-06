class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            prod = 1
            num = i
            while num > 0:
                prod *= num % 10
                num = num // 10

            if prod % t == 0:
                return i
