def leapYear(year):
    if year % 400 == 0 and year % 100 == 0:  # for century years2016
        return True
    elif year % 4 == 0 and year % 100 != 0:  # not for century years
        return True
    else:
        return False

year = int(input("enter year"))
leapYear(year)

if leapYear(year):
    print("Leap year")
else:
    print("Not Leap year")