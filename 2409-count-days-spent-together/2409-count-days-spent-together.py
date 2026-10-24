class Solution:
    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        cnt = 0
        for i in range(12):
            for j in range(1, months[i] + 1):
                date = str(i + 1).zfill(2) + "-" + str(j).zfill(2)
                if arriveAlice <= date <= leaveAlice and arriveBob <= date <= leaveBob:
                    cnt += 1
                print(date)
        return cnt
