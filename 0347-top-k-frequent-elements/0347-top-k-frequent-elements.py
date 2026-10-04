class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        c = Counter(nums)
        ans = []
        for i in c.most_common(k):
            ans.append(i[0])
        return ans
