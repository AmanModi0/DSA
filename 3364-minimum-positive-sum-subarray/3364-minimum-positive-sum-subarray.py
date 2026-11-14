class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        m = float("inf")
        for i in range(l, r + 1):
            s = 0
            left = 0
            right = 0
            while right < i:
                s += nums[right]
                right += 1
            if s > 0:
                m = min(m, s)
            while right < len(nums):
                s += nums[right]
                s -= nums[left]
                left += 1
                right += 1
                if s > 0:
                    m = min(m, s)
        if m == float("inf"):
            return -1
        return m
