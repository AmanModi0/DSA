class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count = 0
        for i in costs:
            coins -= i
            if coins >= 0:
                count += 1
        return count
