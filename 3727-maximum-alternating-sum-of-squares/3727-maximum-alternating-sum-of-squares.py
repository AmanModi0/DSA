class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort()
        total = 0
        n = len(nums)
        return sum(nums[n // 2 :]) - sum(nums[: n // 2])