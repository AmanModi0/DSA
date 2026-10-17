class Solution:
    def maxFreqSum(self, s: str) -> int:
        c = Counter()
        v = Counter()
        vow = "aeiou"
        for i in s:
            if i in vow:
                v[i] += 1
            else:
                c[i] += 1
        vowels = 0
        conso = 0
        if c:
            conso = c.most_common()[0][1]
        if v:
            vowels = v.most_common()[0][1]
        return conso + vowels