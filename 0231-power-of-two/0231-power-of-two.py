class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1 or n == 2:
            return True
        a = 1
        while a < n:
            a *= 2
            if a == n:
                return True
        return False
