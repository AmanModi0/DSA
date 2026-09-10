class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans = []
        prefixSum = 0
        suffixSum = sum(nums)
        for i in range(len(nums)):
            if i == 0:
                prefixSum = 0
            else:
                prefixSum += nums[i - 1]
            suffixSum -= nums[i]
            ans.append(abs(prefixSum - suffixSum))

        return ans
