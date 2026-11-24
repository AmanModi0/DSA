class Solution:
    def maxLength(self, nums: List[int]) -> int:
        l = 0
        mlen = 2
        r = 1
        prod = nums[0]
        while r < len(nums):
            if math.gcd(int(prod), nums[r]) == 1:
                prod *= nums[r]
                mlen = max(mlen, r - l + 1)
                r += 1
                continue
            prod /= nums[l]
            l += 1
        return mlen