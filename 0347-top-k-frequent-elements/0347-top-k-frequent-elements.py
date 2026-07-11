class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        count = {}
        s = []
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1

        for i in range(k):

            mostFreq = max(count, key=count.get)

            s.append(mostFreq)
            count[max(count, key=count.get)] = 0

        return s
