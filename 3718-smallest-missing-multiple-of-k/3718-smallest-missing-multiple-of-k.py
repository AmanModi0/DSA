class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        mul = k
        while True:
            if mul in nums:
                mul += k
            else:
                return mul
