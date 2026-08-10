class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = ""
        m = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] not in a:
                a += s[r]
                r += 1
                m = max(len(a), m)

            elif s[r] in a:
                while s[r] in a:
                    l += 1
                    a = s[l:r]

        return m
