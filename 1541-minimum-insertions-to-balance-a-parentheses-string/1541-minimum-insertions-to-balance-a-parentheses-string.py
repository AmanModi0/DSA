class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        close = 0
        for i in s:
            if i == "(":
                close += 2
                if close % 2 == 1:
                    ans += 1
                    close -= 1
            else:
                close -= 1
                if close < 0:
                    ans += 1
                    close = 1
        return ans + close