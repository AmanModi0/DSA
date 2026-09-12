class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        c = Counter(nums)
        for i in c.keys():
            if c[i] == 2:
                ans.append(i)
        return ans
