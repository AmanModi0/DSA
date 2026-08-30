class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        arr = nums.copy()
        arr.sort()
        maxEl = nums.index(arr[-1])
        minEl = nums.index(arr[0])
        front = min(minEl, maxEl)
        rear = max(minEl, maxEl)

        return min(front + 1 + len(nums) - rear, rear + 1, len(nums) - front)
