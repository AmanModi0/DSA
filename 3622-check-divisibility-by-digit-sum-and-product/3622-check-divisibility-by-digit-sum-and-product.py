class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        prod = 1
        for i in str(n):
            s += int(i)
            prod *= int(i)
            print(i)
        return n % (s + prod) == 0
