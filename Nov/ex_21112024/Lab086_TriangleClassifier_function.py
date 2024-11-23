
def classify_triangle(len1, len2, len3):
    if len1 > 0 and len2 > 0 and len3 > 0:
        if len1 + len2 > len3:
            if len1 == len2 == len3:
                return "Equilateral"
            elif len1 == len2 or len2 == len3 or len3 == len1:
                return "Isosceles"
            else:
                return "Scalene"
        else:
            print("not a triangle")
    else:
        print("Not a valid triangle")


len1 = int(input("enter length1"))  # 40
len2 = int(input("enter length2"))  # 20
len3 = int(input("enter length3"))  # 40
triangle_type=classify_triangle(len1,len2,len3)
print(triangle_type)