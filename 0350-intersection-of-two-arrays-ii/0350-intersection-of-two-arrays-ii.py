from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        a = []
        for i in nums2:
            if c[i] > 0:
                a.append(i)
                c[i] -= 1
        return a
