class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)
        left = 0
        d = {}
        a = []
        for i in range(k - 1, len(nums)):
            window = nums[left : left + k]
            for i in window:
                d[i] = d.get(i, 0) + 1
            left += 1
        print(d)
        if 1 in d.values():
            for key, value in d.items():
                if value == 1:
                    a.append(key)
            return max(a)
        else:
            return -1
