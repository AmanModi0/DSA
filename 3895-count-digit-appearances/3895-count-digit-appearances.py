from collections import Counter


class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        nums = [str(num) for num in nums]
        s = "".join(nums)
        c = Counter(s)
        return c[str(digit)]
