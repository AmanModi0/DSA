class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        ans = []
        for key in d:
            if d.get(key) == 1:
                ans.append(key)
        return ans
