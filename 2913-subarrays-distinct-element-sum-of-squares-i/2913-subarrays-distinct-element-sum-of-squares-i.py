class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum = 0
        for i in range(len(nums)):
            dist = set()
            for j in range(i, len(nums)):
                dist.add(nums[j])
                sum += len(dist) ** 2
        return sum