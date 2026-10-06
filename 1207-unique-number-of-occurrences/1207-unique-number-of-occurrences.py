class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        c = Counter(arr)
        l = [i[1] for i in c.most_common()]
        return len(l) == len(set(l))