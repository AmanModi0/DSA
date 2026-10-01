class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i)
            elif stack and (
                (i == ")" and stack[-1] == "(")
                or (i == "]" and stack[-1] == "[")
                or (i == "}" and stack[-1] == "{")
            ):
                stack.pop()
            else:
                return False
        if stack and stack[-1] in "({[":
            return False
        return True
