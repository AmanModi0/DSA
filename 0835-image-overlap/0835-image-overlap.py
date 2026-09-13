class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        if len(img2) == 1:
            if img1[0][0] == 1:
                return img2[0][0]
            else:
                return 0
        ans = []
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                if img1[i][j] == 1:
                    for m in range(len(img2)):
                        for n in range(len(img2[0])):
                            if img2[m][n] == 1:
                                ans.append((m - i, n - j))
        if len(ans) == 0:
            return 0
        c = Counter(ans)
        return c.most_common(1)[0][1]
