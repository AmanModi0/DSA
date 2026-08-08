class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        sell = 0
        l = []
        for i in prices:
            sell = max(i, sell)
            if i < buy:
                l.append(sell - buy)
                buy = i
                sell = 0
            l.append(sell - buy)

        return max(l)
