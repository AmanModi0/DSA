class Solution:
    def reverseDegree(self, s: str) -> int:
        sum = 0
        for i in range(len(s)):
            sum += (i + 1) * (abs(ord(s[i]) - 123))
        return sum
