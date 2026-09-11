class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        a = max(nums)
        sum = 0
        for i in range(k):
            sum += a + i
        return sum
