class Solution:
    def maxDistinct(self, s: str) -> int:
        c = Counter(s)
        return len(c)