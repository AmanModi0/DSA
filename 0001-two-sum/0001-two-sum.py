from collections import Counter


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c = Counter(nums)
        for i in nums:
            a = target - i
            if a == i and c[i] > 1:
                b = nums.index(i)
                nums.pop(b)
                return [b, nums.index(a) + 1]
            elif a != i and c[a] > 0:
                return [nums.index(i), nums.index(a)]
