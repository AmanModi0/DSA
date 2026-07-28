from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        a = ""
        mid = ""
        count = Counter(s)
        for i in sorted(count.keys()):
            if count[i] % 2 == 1:
                mid = i
            a += i * (count[i] // 2)
        return a + mid + a[::-1]
