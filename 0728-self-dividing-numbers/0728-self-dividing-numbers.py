class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right + 1):
            flag = True
            if "0" not in str(i):
                a = int(i)
                while a > 0:
                    k = a % 10
                    if i % k != 0:
                        flag = False
                        break
                    a = a // 10
                if flag == True:
                    l.append(i)
        return l
