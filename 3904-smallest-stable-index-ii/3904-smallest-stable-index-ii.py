class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        mini = [0] * n
        mini[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            mini[i] = min(nums[i], mini[i + 1])

        maxi = nums[0]
        for i in range(n):
            maxi = max(maxi, nums[i])
            score = maxi - mini[i]
            if score <= k:
                return i
        return -1
