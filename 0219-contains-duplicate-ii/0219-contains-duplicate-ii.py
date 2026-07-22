from collections import Counter


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = Counter(nums)
        for i in range(0, len(nums)):
            diff = 0
            if c[nums[i]] > 1:
                for j in range(i + 1, len(nums)):
                    if nums[j] == nums[i]:
                        diff = abs(i - j)
                        if diff <= k:
                            return True
                c[nums[i]] -= 1
        return False
