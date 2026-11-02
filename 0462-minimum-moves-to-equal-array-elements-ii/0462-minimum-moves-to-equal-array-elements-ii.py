class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        c = 0
        nums.sort()
        m = len(nums) // 2
        for i in nums:
            c += abs(nums[m] - i)
        return c