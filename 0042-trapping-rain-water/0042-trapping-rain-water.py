class Solution:
    def trap(self, height: List[int]) -> int:
        lmax = 0
        rmax = 0
        left = 0
        right = len(height) - 1
        water = 0

        while left <= right:
            lmax = max(height[left], lmax)
            rmax = max(height[right], rmax)

            if lmax <= rmax:
                water += lmax - height[left]
                left += 1
            elif rmax < lmax:
                water += rmax - height[right]
                right -= 1

        return water
