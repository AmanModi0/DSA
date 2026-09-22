class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        i = 0
        intervals.sort()
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i + 1][0]:
                if intervals[i][1] >= intervals[i + 1][1]:
                    del intervals[i+1]
                else:
                    intervals[i][1] = intervals[i + 1][1]
                    del intervals[i + 1]
            else:
                i += 1
        return intervals
