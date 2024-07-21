#!/usr/bin/env python3

import sys
#PETER DEVOS

def day_of_week(date: str) -> str:
#Based on the algorithm by Tomohiko Sakamoto

    day, month, year = (int(x) for x in date.split('/'))
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}

    if month < 3:
        year -= 1

    num = (year + year//4 - year//100 + year//400 + offset[month] + day) % 7
    return days[num]


def leap_year(year: int) -> bool:

    #return true if the year is a leap year
    #A formula that checks for leap years if the year is divisible by 4, and not 100, unless divisible by 400
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            Return True
    else:
        return False


def mon_max(month:int, year:int) -> int:
    "returns the maximum day for a given month. Includes leap year check"
    if month == 2:
        return 29 if leap_year(year) else 28
    if month in {4, 6, 8, 11}:
        return 30
    return 31


def after(date: str) -> str: 
  '''
  after() -> date for next day in DD/MM/YYYY string format
  Return the date for the next day of the given date in DD/MM/YYYY format.
  This function has been tested to work for year after 1582
  '''
    #Turns the date given into strings for day, month, and year
    day, mon, year = (int(x) for x in date.split('/'))
    day += 1 # next day
    #Defines every 4 years is a leap year
    lyear = year % 4
    if lyear == 0:
        leap_flag = True
    else:
        leap_flag = False # this is not a leap year
    
    #If year is divisible by 100, check for 400 years
    lyear = year % 100
    if lyear == 0:
        leap_flag = False # this is not a leap year
    
    #If divisible by 400, is a leap year
    lyear = year % 400
    if lyear == 0:
    leap_flag = True # this is a leap year

   #Defines the days in each month
    mon_dict= {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    #Checks for days in february if leap flag caught a False
    if mon == 2 and leap_flag:
        mon_max = 29
    else:
        mon_max = mon_dict[mon]
    if day > mon_max:
        mon += 1
        if mon > 12:
            year += 1
            mon = 1
        day = 1 # if tmp_day > this month's max, reset to 1 
    return f"{day:02}/{mon:02}/{year}"


def before(date: str) -> str:
  "Returns previous day's date as DD/MM/YYYY"



def usage():
  "Print a usage message to the user"
  print("Usage: " + str(sys.argv[0]) + " DD/MM/YYYY NN")
  sys.exit()


def valid_date(date: str) -> bool:
  "check validity of date"




def day_iter(start_date: str, num: int) -> str:
  "iterates from start date by num to return end date in DD/MM/YYYY"




if __name__ == "__main__":
  # check length of arguments
  # check first arg is a valid date
  # check that second arg is a valid number (+/-)
  # call day_iter function to get end date, save to x
  # print(f'The end date is {day_of_week(x)}, {x}.')
  pass
