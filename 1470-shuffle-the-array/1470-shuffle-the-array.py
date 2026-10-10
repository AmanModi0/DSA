class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[0:n][i])
            ans.append(nums[n:][i])
        return ans