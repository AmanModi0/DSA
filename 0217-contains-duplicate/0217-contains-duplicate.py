class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        flag = False
        for i in nums:
            d[i] = d.get(i, 0) + 1

        for key in d:
            if d.get(key) > 1:
                flag = True
        return flag
