class Solution:
    def digitSum(self, n):
        sum = 0
        while n > 0:
            sum += n % 10
            n //= 10
        return sum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter()
        for i in range(lowLimit, highLimit + 1):
            a = self.digitSum(i)
            c[a] += 1

        return c.most_common(1)[0][1]
