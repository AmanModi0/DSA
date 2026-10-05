class Solution:
    def findComplement(self, num: int) -> int:
        a = bin(num)[2:]
        ans = ""
        for i in range(len(a)):
            if a[i] == "1":
                ans += "0"
            else:
                ans += "1"
        return int(ans, 2)
