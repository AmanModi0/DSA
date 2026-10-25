class Solution:
    def days(self, date):
        d = date.split("-")
        year = 1900
        day = 0
        while year < int(d[0]):
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                day += 366
            else:
                day += 365
            year += 1
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        month = 1
        while month < int(d[1]):
            day += months[month - 1]
            month += 1
        day += int(d[2])
        return day

    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs(self.days(date2) - self.days(date1))
