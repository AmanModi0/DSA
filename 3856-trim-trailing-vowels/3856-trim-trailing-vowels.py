class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        l = list(s)
        while l and l[-1] in "aeiou":
            l.pop()
        return "".join(l)