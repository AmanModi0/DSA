class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = {}
        left = 0
        right = 0
        long = 0
        while right < len(s):
            d[s[right]] = d.get(s[right], 0) + 1
            if d[s[right]] > 2:
                while d[s[right]] > 2:
                    d[s[left]] -= 1
                    left += 1
            long = max(right - left + 1, long)
            right += 1

        return long
