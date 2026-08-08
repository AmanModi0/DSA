class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1 or n == 3:
            return True
        a = 1
        while a < n:
            a *= 3
            if a == n:
                return True
        return False
