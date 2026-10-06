class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        a = [i.strip() for i in a]
        return " ".join(a[::-1])
