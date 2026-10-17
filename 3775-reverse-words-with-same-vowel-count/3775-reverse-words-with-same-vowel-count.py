class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        vow = 0
        for i in l[0]:
            if i in "aeiou":
                vow += 1
        for i in range(1, len(l)):
            count = 0
            for j in l[i]:
                if j in "aeiou":
                    count += 1
            if count == vow:
                l[i] = l[i][::-1]
        return " ".join(l)