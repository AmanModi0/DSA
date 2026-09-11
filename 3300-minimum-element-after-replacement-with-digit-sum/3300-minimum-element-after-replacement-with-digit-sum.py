class Solution:
    def minElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            a = 0
            while nums[i] > 0:
                a += nums[i] % 10
                nums[i] = nums[i] // 10
            nums[i] = a

        return min(nums)
