class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        left = 0
        right = len(piles)
        piles.sort()
        maxCoins = 0
        while left < right:
            maxCoins += piles[right-2]
            right -= 2
            left += 1

        return maxCoins