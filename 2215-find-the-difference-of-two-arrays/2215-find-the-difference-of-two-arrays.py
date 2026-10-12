class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]