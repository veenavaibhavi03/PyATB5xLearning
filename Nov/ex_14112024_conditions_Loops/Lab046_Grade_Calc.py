#grading
#logic building formula
#1-> user inputs-> score or marks->int
#2-> o/p -> str-> A or B...

score =int(input("Enter your score\n"))

if score>=90 and score<=100:
    print("Grade:A")
elif score >= 80 and score <= 89:
    print("Grade:B")
elif score >= 70 and score <= 79:
    print("Grade:c")
elif score>=60 and score<=69:
    print("Grade:D")
elif score>100 or score<=-1:
    print("No Grade")
else:
    print("Grade:F")

