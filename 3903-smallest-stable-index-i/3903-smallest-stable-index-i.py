class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ans = []
        for i in range(n):
            score = max(nums[: i + 1]) - min(nums[i:n])
            ans.append(score)
            if ans[i] <= k:
                return i
        return -1
