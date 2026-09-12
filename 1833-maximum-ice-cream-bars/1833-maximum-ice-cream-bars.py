class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        price = 0
        count = 0
        for i in costs:
            price += i
            if price <= coins:
                count += 1
        return count