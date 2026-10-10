class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c1 = Counter(s)
        c2 = Counter(t)
        for i in t:
            if c1[i] != c2[i]:
                return i
