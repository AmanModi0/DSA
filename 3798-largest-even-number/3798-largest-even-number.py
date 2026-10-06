class Solution:
    def largestEven(self, s: str) -> str:
        if int(s) % 2 == 0:
            return s
        l = list(s)
        while l and l[-1] != "2":
            l.pop()
        return "".join(l)
