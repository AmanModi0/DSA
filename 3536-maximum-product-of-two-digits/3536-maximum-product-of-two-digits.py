class Solution:
    def maxProduct(self, n: int) -> int:
        l = sorted(map(int, str(n)), reverse=True)
        return l[0] * l[1]
