class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = [s[0]]
        for i in range(1, len(s)):
            if stack and s[i] == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack)
