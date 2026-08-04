class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        upper = nums[-1]
        lower = nums[0]
        missingElem = []
        for i in range(1, len(nums)):
            while nums[i] != lower + 1:
                lower += 1
                missingElem.append(lower)
            lower += 1

        return missingElem
