class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        l = 0
        d = {}
        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1
            while d.get(s[r]) > 1:
                d[s[l]] -= 1
                l += 1
            m = max(m, r - l + 1)
        return m
