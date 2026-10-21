class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        n = start ^ goal
        while n > 1:
            count += n % 2
            n //= 2
        if n == 1:
            count += 1
        return count