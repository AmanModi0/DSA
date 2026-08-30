from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        mx = -1
        for key, val in c.items():
            if key == val:
                mx = max(mx, val)

        return mx
