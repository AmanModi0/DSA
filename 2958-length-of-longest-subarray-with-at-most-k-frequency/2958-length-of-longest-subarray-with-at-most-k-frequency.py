class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        dict = {}
        l = 0
        long = 0
        for r in range(len(nums)):
            dict[nums[r]] = dict.get(nums[r], 0) + 1

            if dict.get(nums[r]) <= k:
                long = max(long, r - l + 1)
                continue

            while dict.get(nums[r]) > k:
                dict[nums[l]] -= 1
                l += 1

        return long
