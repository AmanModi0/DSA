class Solution:
    def calPoints(self, ops: List[str]) -> int:
        a = []
        for i in range(len(ops)):
            if ops[i] == "C":
                a.pop()
            elif ops[i] == "D":
                a.append(a[-1] * 2)
            elif ops[i] == "+":
                a.append(a[-2] + a[-1])
            else:
                a.append(int(ops[i]))
        return sum(a)
