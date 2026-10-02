class Solution:
    def sortEvenOdd(self, nums: list[int]) -> list[int]:
        e = []
        o = []
        ans = []
        for i in range(len(nums)):
            if i % 2 == 0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e.sort()
        o.sort(reverse=True)
        for i in range(len(nums) // 2):
            ans.append(e[i])
            ans.append(o[i])
        if len(nums) % 2 != 0:
            ans.append(e[-1])
        return ans
