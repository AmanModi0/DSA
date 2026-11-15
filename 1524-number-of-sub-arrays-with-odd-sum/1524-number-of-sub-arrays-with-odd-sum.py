class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        count = 0
        odd_count = 0
        for i in arr:
            count += i
            odd_count += count % 2
        odd_count += (len(arr) - odd_count) * odd_count
        return odd_count % (10**9 + 7)
