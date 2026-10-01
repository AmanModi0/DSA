class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        check = [False] * (len(nums) + 1)
        for i in nums:
            if check[i]:
                return i
            check[i] = True
