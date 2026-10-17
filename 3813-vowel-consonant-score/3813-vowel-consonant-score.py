class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        cons = "bcdfghjklmnpqrstvwxyz"
        vow = "aeiou"
        c = 0
        v = 0
        for i in s:
            if i in vow:
                v += 1
            if i in cons:
                c += 1
        if c > 0:
            return v // c
        return 0