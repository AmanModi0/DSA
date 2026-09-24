class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        l = 0
        r = 0
        g.sort()
        s.sort()
        while l < len(s) and r < len(g):
            if s[l] >= g[r]:
                r += 1
                l += 1
            else:
                l += 1
        return r
