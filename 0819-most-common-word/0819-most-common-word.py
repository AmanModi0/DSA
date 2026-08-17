from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        l = ["!", "?", "'", ",", ";", "."]
        for i in l:
            paragraph = paragraph.replace(i, " ")
        c = Counter(paragraph.lower().split())
        print(c)
        for i in banned:
            c[i] = 0

        return c.most_common(1)[0][0]
