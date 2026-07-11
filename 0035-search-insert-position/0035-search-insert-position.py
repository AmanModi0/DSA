class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):

            if nums[i] == target:
                return i
            elif nums[i] < target:
                if i == len(nums) - 1:
                    return i + 1
                else:
                    continue
            else:
                return i
