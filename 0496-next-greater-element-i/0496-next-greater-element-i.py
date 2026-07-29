class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            flag = False
            a = nums2.index(i)
            for j in range(a, len(nums2)):
                if nums2[j] > i:
                    l.append(nums2[j])
                    flag = True
                    break
            if flag == False:
                l.append(-1)

        return l
