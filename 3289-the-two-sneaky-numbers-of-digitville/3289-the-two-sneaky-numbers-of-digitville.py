class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        s = set()
        ans = []
        for i in nums:
            if i in s:
                ans.append(i)
            else:
                s.add(i)
        return ans