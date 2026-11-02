class Solution(object):
    def minMoves2(self, nums):
        nums.sort()
        m = nums[len(nums) // 2]
        return sum(abs(i - m) for i in nums)