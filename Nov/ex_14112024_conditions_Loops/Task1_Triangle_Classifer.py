#triangle classifier
# logic building formula
# input len 1, len2,len3-> int
# 0/p-> equiletral , isosceles, scalene
len1=int(input("enter length1")) #40
len2=int(input("enter length2")) # 20
len3=int(input("enter length3"))#40

# rough logic : len1==len2 and len2==len3 -> equilateral triangle
#len1==len2 or len2!=len3 or len3==len1
if (len1==len2) and len2==len3 and len3==len1:
    print("Equilateral triangle ")
elif (len1!=len2 or len2!=len3 or len3!=len1 ) and (len1==len2 or len2==len3 or len3==len1):
    print("Isosceles triangle")
else:
    print("scalene triangle")

#edge cases-string, float numbers