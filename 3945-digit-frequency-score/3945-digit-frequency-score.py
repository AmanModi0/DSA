from collections import Counter


class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        c = Counter(str(n))
        score = 0
        for key, val in c.items():
            score += int(key) * val

        return score
