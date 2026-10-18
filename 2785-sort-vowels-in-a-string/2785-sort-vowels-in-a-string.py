class Solution:
    def sortVowels(self, s: str) -> str:
        vow = []
        for i in s:
            if i.lower() in "aeiou":
                vow.append(i)
        vow.sort()
        chr = 0
        ans = ""
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                ans += vow[chr]
                chr += 1
            else:
                ans += s[i]
        return ans