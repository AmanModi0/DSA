class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max(prev1, nums[i] + prev2)
            prev2 = prev1
            prev1 = nums[i]

        return nums[-1]
