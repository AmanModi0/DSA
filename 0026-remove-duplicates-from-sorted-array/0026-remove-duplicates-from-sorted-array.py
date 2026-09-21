class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a = sorted(list(set(nums)))
        nums[:] = a
        return len(nums)