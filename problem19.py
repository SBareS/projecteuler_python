"""
Counting Sundays
You are given the following information, but you may prefer to do some
research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a
        century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
"""

def day_of_week(year, month, day):
    # See https://en.wikipedia.org/wiki/Zeller%27s_congruence
    # 0 is Sunday, 1 is Monday, etc. (thus we have to subtract 1 from 
    # the formula on Wikipedia, since that has Saturday as day 0)
    if month < 3:
        # Count January and February as months 13 and 14 of the 
        # previous year
        month += 12
        year -= 1
    J, K = divmod(year, 100)
    return (day + (13*(month + 1))//5 + K + K//4 + J//4 - 2*J - 1)%7

sunday_firsts = [(year, month, 1)
    for year in range(1901, 2001)
    for month in range(1, 13)
    if day_of_week(year, month, 1) == 0]

print(len(sunday_firsts))
correct_answer = "171"