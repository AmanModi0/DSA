class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = []
        indices = []
        for i in range(len(s)):
            if s[i].lower() in "aeiou":
                vowels.append(s[i])
                indices.append(i)
        vowels.sort()
        res = list(s)
        v_index = 0
        for i in indices:
            res[i] = vowels[v_index]
            v_index += 1
        return "".join(res)