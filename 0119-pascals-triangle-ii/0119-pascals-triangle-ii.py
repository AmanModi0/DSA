class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        l = [[1]]
        for i in range(1, rowIndex + 1):
            dp = [0] * (i + 1)
            dp[0] = l[i - 1][0]
            dp[-1] = l[i - 1][-1]
            for j in range(1, i):
                if i == j:
                    continue

                dp[j] = l[i - 1][j - 1] + l[i - 1][j]

            l.append(dp)

        return l[rowIndex]
