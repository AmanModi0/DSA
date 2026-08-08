class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1:
            return 1
        low = 0
        high = x // 2
        mid = (low + high) // 2
        while low <= high:
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
                mid = (low + high) // 2
            else:
                high = mid - 1
                mid = (low + high) // 2
        return mid
