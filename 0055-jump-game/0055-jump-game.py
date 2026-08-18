class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            if i > dp[i - 1]:
                return False
            dp[i] = max(dp[i - 1], i + nums[i])
            if dp[i] >= n - 1:
                return True

        return True
