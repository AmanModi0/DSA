class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        res = []
        m = 0
        while m < len(l):
            if r[m] - l[m] + 1 > 2:
                temp = sorted(nums[l[m] : r[m] + 1])
                print(len(temp))
                flag = True
                dif = temp[1] - temp[0]
                for i in range(2, len(temp)):
                    if temp[i] - temp[i - 1] != dif:
                        res.append(False)
                        flag = False
                        break
                if not flag:
                    m += 1
                    continue
            res.append(True)
            m += 1
        return res