class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digiSum = 0
            while nums[i] > 0:
                digiSum += nums[i] % 10
                nums[i] //= 10

            if digiSum == i:
                return i
        return -1
