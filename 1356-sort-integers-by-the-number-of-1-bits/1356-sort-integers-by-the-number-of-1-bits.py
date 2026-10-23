class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        res = []
        ones = {}
        arr.sort()
        c1 = Counter(arr)
        for i in arr:
            c = Counter(bin(i)[2:])
            ones[i] = c["1"]
        a = dict(sorted(ones.items(), key=lambda item: item[1]))
        for i in a.keys():
            for j in range(0, c1[i]):
                res.append(i)
        return res