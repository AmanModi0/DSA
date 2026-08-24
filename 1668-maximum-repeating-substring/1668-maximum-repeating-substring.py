class Solution:
    def maxRepeating(self, s: str, word: str) -> int:
        count = 0
        i = 0
        mx = 0
        while i <= (len(s) - len(word)):
            a = s[i : i + len(word)]
            if a != word:
                count = 0
                i += 1
            else:
                count += 1
                i += len(word)

            mx = max(mx, count)
        i = len(s)
        count = 0
        while i > 0:
            a = s[i - len(word) : i]
            if a != word:
                count = 0
                i -= 1
            else:
                count += 1
                i -= len(word)
            print(a)
            mx = max(mx, count)

        return mx
