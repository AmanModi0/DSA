class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        c = 0
        for i in arr1:
            flag = False
            for j in arr2:
                if abs(i - j) > d:
                    continue
                else:
                    flag = True
                    break
            if not flag:
                c += 1
        return c