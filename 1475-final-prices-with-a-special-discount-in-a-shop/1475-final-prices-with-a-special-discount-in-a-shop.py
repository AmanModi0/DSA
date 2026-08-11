class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []
        for i in range(len(prices)):

            if i == len(prices) - 1:
                ans.append(prices[-1])

            for j in range(i + 1, len(prices)):

                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    break
                elif j == len(prices) - 1:
                    ans.append(prices[i])

        return ans
