class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        for i in bin(start ^ goal)[2:]:
            if i == "1":
                count += 1
        return count