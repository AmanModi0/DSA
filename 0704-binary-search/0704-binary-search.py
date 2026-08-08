class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1 and nums[0] == target:
            return 0
        low = 0
        high = n - 1
        mid = (low + high) // 2
        while low <= high:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                low = mid + 1
                mid = (low + high) // 2
            else:
                high = mid - 1
                mid = (low + high) // 2

        return -1
