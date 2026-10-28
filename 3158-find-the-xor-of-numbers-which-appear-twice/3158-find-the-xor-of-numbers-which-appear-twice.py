class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        a = Counter(nums)
        ans = 0
        for i in a:
            if a[i] == 2:
                ans ^= i
        return ans