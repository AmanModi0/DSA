class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for key in d:
            if d.get(key) == 1:
                return key
