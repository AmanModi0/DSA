class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(set(word)) == 1:
            return True
        c = Counter(word)
        print(len(set(word)))
        a = sorted(list(c.values()))
        if len(set(a)) > 2 or (len(set(a)) == 1 and a[0] > 1):
            return False
        if a[0] == 1 and len(set(a)) == 1:
            return True
        if a[-1] > a[-2]:
            a[-1] -= 1
        if a[0] < a[1]:
            print(a)
            a[0] -= 1
        return len(set(a)) == 1 or a[0] == 0