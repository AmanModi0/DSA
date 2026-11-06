class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in nums:
            rem = i % 3
            ops += min(rem, 3 - rem)
        return ops