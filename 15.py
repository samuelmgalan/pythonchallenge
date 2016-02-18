#!/usr/bin/env python3

# http://www.pythonchallenge.com/pc/return/uzi.html
import datetime
import calendar

years = [x for x in range(1582, 1997)]
for i in range(len(years)):
  if datetime.datetime(years[i], 1, 1).weekday() == 3 and calendar.isleap(years[i]): # leap years since the begining of the Gregorian Calendar
    print(str(years[i])) # 1756

# todo: buy flowers for tomorrow <- 27/01/1986 Mozart's birthday