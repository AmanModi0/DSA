class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        chr = 0
        i = 0
        while chr < len(s) and i < len(t):
            if t[i] == s[chr]:
                chr += 1
            i += 1
        return len(s) == chr