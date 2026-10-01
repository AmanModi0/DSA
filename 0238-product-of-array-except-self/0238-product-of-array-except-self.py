class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefixArr = [1]
        suffixArr = [1]
        prefix = 1
        suffix = 1
        for i in range(len(nums) - 1):
            prefix *= nums[i]
            prefixArr.append(prefix)
        for i in range(1, len(nums)):
            suffix *= nums[-i]
            suffixArr.append(suffix)
        suffixArr.reverse()
        for i in range(len(nums)):
            ans.append(prefixArr[i] * suffixArr[i])
        return ans
