class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            return -int("".join(sorted(str(num)[1:])[::-1]))
        if num == 0:
            return 0
        a = list(str(num))
        c = Counter(a)
        ans = ""
        if "0" in a:
            m = 9
            for i in a:
                if int(i) != 0:
                    m = min(m, int(i))
            c[str(m)] -= 1
            ans += str(m)
        for i in sorted(c.most_common()):
            ans += i[0] * i[1]
        return int(ans)
