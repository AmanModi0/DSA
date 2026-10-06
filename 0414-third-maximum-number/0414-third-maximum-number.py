class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        ans = sorted(set(nums))
        if len(ans) >= 3:
            return ans[-3]
        return ans[-1]
