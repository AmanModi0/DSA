class Solution:
    def minMoves(self, a: list[int]) -> int:
        m = min(a)
        return sum(x - m for x in a)