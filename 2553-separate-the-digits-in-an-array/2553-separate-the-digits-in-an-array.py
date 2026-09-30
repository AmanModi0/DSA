class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        ans = []
        for i in nums:
            ans.extend(list(map(int, list(str(i)))))
        return ans
