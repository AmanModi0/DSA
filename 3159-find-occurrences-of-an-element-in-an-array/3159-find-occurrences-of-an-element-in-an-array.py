class Solution:
    def occurrencesOfElement(
        self, nums: List[int], queries: List[int], x: int
    ) -> List[int]:
        idx = []
        ans = []
        for i in range(len(nums)):
            if nums[i] == x:
                idx.append(i)
        idx.sort()
        for j in range(len(queries)):
            if queries[j] <= len(idx):
                ans.append(idx[queries[j] - 1])
            else:
                ans.append(-1)
        return ans
