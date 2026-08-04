from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        words.sort()
        c = Counter(words)
        l = c.most_common(k)
        a = []
        for i in l:
            a.append(i[0])
        return a
