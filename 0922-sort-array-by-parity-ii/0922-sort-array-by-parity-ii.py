class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = even.pop()
            else:
                nums[i] = odd.pop()
        return nums
