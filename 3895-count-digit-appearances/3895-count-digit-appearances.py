class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        return str(nums).count(str(digit))
