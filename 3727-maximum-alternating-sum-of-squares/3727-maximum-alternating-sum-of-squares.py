class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [x * x for x in nums]
        nums.sort()
        total = 0
        n = len(nums)
        if n % 2 == 0:
            return sum(nums[n // 2 :]) - sum(nums[: n // 2])
        else:
            return sum(nums[n // 2 :]) - sum(nums[: n // 2])
