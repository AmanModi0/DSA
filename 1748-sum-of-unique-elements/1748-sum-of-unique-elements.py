class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        c = Counter(nums)
        sum = 0
        for i in c.keys():
            if c[i] == 1:
                sum += i
        return sum
