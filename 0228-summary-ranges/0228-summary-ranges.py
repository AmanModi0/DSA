class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        s = []
        i = 0
        while i < n:
            a = i
            if a < n - 1 and nums[a + 1] == nums[a] + 1:
                while a < n - 1 and nums[a + 1] == nums[a] + 1:
                    a += 1

                s.append(str(nums[i]) + "->" + str(nums[a]))

            else:
                s.append(str(nums[i]))
            i = a + 1
        return s
