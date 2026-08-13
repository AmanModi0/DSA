class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = int(str(int(str(num)[::-1]))[::-1])
        return a == num
