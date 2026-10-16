class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        count = 0
        seen = set()
        for i in nums:
            if i not in seen:
                if i == k / 2:
                    count += c[i] // 2
                    c[i] -= c[i] // 2
                elif c[k - i] > 0:
                    m = min(c[i], c[k - i])
                    count += m
                    c[i] -= m
                    c[k - i] -= m
            seen.add(i)
            seen.add(k - i)

        return count