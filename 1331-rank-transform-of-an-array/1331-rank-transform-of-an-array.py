class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        l1 = list(set(arr))
        l1.sort()

        rank = {}

        for i in range(len(l1)):
            rank[l1[i]] = i + 1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr
