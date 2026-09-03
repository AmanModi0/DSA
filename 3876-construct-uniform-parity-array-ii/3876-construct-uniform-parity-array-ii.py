class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        s = min(nums1)
        if s % 2 == 0:
            for i in nums1:
                if i % 2 == 0:
                    continue
                else:
                    if (i - s) < 1 or (i - s) % 2 != 0:
                        return False
            return True
        else:
            for i in nums1:
                if i % 2 != 0:
                    continue
                else:
                    if (i - s) < 1 or (i - s) % 2 == 0:
                        return False
            return True
