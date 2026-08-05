class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        l = []
        nums.extend(nums)
        for i in range(len(nums) // 2):
            flag = False
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    l.append(nums[j])
                    flag = True
                    break
            if flag == False:
                l.append(-1)
        return l
