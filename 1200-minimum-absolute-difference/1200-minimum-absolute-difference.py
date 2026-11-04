class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        ans = []
        arr.sort()
        mn = float(inf)
        for i in range(1, len(arr)):
            mn = min(mn, abs(arr[i] - arr[i - 1]))
        for i in range(1, len(arr)):
            if abs(arr[i] - arr[i - 1]) == mn:
                ans.append([arr[i - 1], arr[i]])
        return ans