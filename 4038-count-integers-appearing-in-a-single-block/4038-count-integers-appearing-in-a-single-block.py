class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        c = Counter(nums)
        l = 0
        r = 0
        count = 0
        while r < len(nums):
            while r < len(nums) and nums[r] == nums[l]:
                r += 1
            if c[nums[l]] == r - l:
                count += 1
            l = r
        return count
