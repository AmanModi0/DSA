class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, 0, -1):
            n -= i
            if n < 0:
                return i % 2 != 0
        return i % 2 == 0