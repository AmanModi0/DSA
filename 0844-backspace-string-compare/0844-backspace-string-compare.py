class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []
        for i in s:
            if i == "#":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        a = stack.copy()
        stack.clear()
        for i in t:
            if i == "#":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(i)
        return a == stack
