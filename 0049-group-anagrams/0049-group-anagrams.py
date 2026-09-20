class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for i in strs:
            a = "".join(sorted(i))
            if a in d:
                d[a].append(i)
            else:
                d[a] = d.get(a, [i])
        return sorted(list(d.values()))
