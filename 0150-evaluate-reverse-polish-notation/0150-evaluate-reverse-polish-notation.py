class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                stack[-2] = str(int(eval(stack[-2] + i + stack[-1])))
                stack.pop()
                continue
            stack.append(i)
        return int(stack[-1])