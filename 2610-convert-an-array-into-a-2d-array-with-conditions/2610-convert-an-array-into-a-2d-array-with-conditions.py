class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        if len(set(nums)) == len(nums):
            return [nums]
        c = Counter(nums)
        res = []
        while c:
            l = []
            d = []
            for i in c:
                if c[i] > 0:
                    l.append(i)
                    c[i] -= 1
                    if c[i] == 0:
                        d.append(i)
            res.append(l)
            for i in d:
                del c[i]
        return res