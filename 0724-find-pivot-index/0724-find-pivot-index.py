class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lsum = 0
        rsum = 0
        for i in range(1, len(nums)):
            rsum += nums[i]
        if lsum == rsum:
            return 0
        else:
            for i in range(1, len(nums)):
                lsum += nums[i - 1]
                rsum -= nums[i]
                if lsum == rsum:
                    return i

            return -1
