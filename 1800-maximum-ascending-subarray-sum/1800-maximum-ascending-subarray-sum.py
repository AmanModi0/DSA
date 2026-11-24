class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        summ = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                summ += nums[i]
                maxSum = max(maxSum, summ)
            else:
                summ = nums[i]
        return maxSum