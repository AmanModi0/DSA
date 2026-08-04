from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:

        c = Counter(s)
        l = c.most_common()
        a = ""
        for i in l:
            a += i[0] * c[i[0]]
        return a
