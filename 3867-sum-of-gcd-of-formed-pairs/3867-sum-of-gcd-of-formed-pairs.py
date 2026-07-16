class Solution:
    def GCD(self, x, y):

        if x == 1 or y == 1:
            return 1
        a = max(x, y)
        b = min(x, y)

        while True:
            if x % y == 0:
                return y
            else:
                temp = x % y
                x = y
                y = temp

    def gcdSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0

        mx = [0] * len(nums)
        mx[0] = nums[0]

        for i in range(1, len(nums)):
            mx[i] = max(mx[i - 1], nums[i])

        prefixGcd = [0] * len(nums)
        for i in range(len(nums)):
            prefixGcd[i] = self.GCD(mx[i], nums[i])

        prefixGcd.sort()
        sum = 0
        for i in range(len(prefixGcd) // 2):
            sum += self.GCD(prefixGcd[0], prefixGcd[-1])
            prefixGcd.pop(-1)
            prefixGcd.pop(0)

        return sum
