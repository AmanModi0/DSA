class Solution:
    def isGood(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) != nums[-1] + 1:
            return False
        c = Counter(nums)
        for i in nums:
            if i != nums[-1]:
                if c[i] > 1:
                    return False
                else:
                    continue
            if c[i] == 2:
                return True
        return False
