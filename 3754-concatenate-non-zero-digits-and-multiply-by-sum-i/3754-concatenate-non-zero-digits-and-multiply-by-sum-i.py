class Solution:
    def sumAndMultiply(self, n: int) -> int:

        if n == 0:
            return 0
        sum = 0
        x = ""
        for i in str(n):
            if i != "0":
                x += i
                sum += int(i)

        return int(x)*sum
