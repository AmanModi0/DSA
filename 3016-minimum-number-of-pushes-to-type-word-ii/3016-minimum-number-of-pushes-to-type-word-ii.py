from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word).most_common()
        pushes = 0
        cnt = 1
        for i in range(len(count)):
            if cnt <= 8:
                pushes += count[i][1]

            elif cnt > 8 and cnt <= 16:
                pushes += count[i][1] * 2

            elif cnt > 16 and cnt <= 24:
                pushes += count[i][1] * 3

            else:
                pushes += count[i][1] * 4

            cnt += 1
        return pushes
