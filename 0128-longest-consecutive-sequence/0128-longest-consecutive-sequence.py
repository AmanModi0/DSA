class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a = sorted(set(nums))
        if len(a) == 1:
            return 1
        count = 1
        mx = 0
        for i in range(1, len(a)):
            if a[i] == a[i - 1] + 1:
                count += 1
            else:
                count = 1
            mx = max(count, mx)
        return mx
