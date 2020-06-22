# -*- coding: UTF-8 -*-
import datetime
import random
import calendar
import openpyxl


first = lambda x: x[0]

def all_days(): 
    days = []
    weekdays = ("星期一", "星期二", "星期三", "星期四", "星期五")
    d = datetime.datetime.today()
    month = d.month
    year = d.year
    b = calendar.Calendar()
    for i in b.itermonthdates(year, month - 1):
     if i.month == month - 1 and i.day >= 21 and i.weekday() not in (5 ,6):
         min = random.randint(30, 59)
         days.append((i, weekdays[i.weekday()], f"20:{min}"))
    for i in b.itermonthdates(year, month):
     if i.month == month and i.day <= 21 and i.weekday() not in (5 ,6):
         min = random.randint(30, 59)
         days.append((i, weekdays[i.weekday()], f"20:{min}", ""))
    real_days = random.sample(days, 10)
    real_days.sort(key=first)
    for i in real_days:
        print(i[0])
    for i in real_days:
        print(i[2])

all_days()