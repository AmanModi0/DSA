class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c_open = 0
        c_close = 0
        ans = ""
        for i in s:
            if i == "(":
                c_open += 1
                if c_open > 1:
                    ans += "("
            else:
                c_close += 1
                if c_close < c_open:
                    ans += ")"

            if c_open == c_close:
                c_open = 0
                c_close = 0
        return ans
