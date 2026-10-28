class Solution:
    def smallestNumber(self, n: int) -> int:
        a = len(bin(n)[2:])
        return int("1" * a, 2)
