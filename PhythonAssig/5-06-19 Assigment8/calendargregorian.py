#INSTRUCTIONS:
#1) input gregorian date, output human calendar date.
#2) output current date in human calendar format, and have it updated by system time.

import calendargregorian
import calendar
import math

def leapYear(year):

    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                print("{0} is a leap year".format(year))
            else:
                print("{0} is not a leap year".format(year))
        else:
            print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
        # Divisible by 4 and,
        # either not divisible by 100 or divisible by 400.
   


def gregTojd(year, month, day):
    
    a = int((month - 14) / 12.0)
    jd =int((1461 * (year + 4800 + a)) / 4.0)
    jd +=int((367 * (month - 2 - 12 * a)) / 12.0)
    x =int((year + 4900 + a) / 100.0)
    jd -=int((3 * x) / 4.0)
    jd += day - 2432075.5  # was 32075; add 2400000.5

    jd -= 0.5  # 0 hours; above JD is for midday, switch to midnight.

    print ("reusult: %d , %d, %d",(x, a , jd))

def main ():
    year = int(input (" year to convert from Greg---> Julian Calendar: "))
    month = int(input (" month to convert from Greg---> Julian Calendar: "))
    day = int(input (" day to convert from Greg---> Julian Calendar: "))
    
    leapYear (year)
    gregTojd (year, month, day)
    input('')
    quit()

main()