class Solution:
    def maxDepth(self, s: str) -> int:
        a = 0
        b = 0
        for i in s:
            if i == "(":
                a += 1
                b = max(b, a)
            if i == ")":
                a -= 1
        return b
