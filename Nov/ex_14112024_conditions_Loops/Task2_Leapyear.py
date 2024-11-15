year=int(input("enter year"))
if year%400==0 and year%100==0: #for century years2016
    print("Leap year")
elif year%4==0 and year%100!=0: #not for century years
    print("Leap year")
else:
    print("Not a leap year")