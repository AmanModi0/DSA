class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            for s in str(i):
                ans.append(int(s))
        return ans
