class Solution:
    def totalFruit(self, nums: list[int]) -> int:
        l = 0
        count = 0
        d = {}
        for r in range(len(nums)):
            d[nums[r]] = d.get(nums[r], 0) + 1
            while len(d) > 2:
                d[nums[l]] -= 1
                if d[nums[l]] == 0:
                    del d[nums[l]]
                l += 1
            count = max(count, r - l + 1)
        return count
