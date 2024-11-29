class PyATB:
    list_student=[]

    def __init__(self, list_student=None):
        self.list_student=list_student

    def print_student_information(self):
        print("Name of the person:", self.list_student[0])
        print("phone_number:", self.list_student[1])
        print("mail_id:", self.list_student[2]+"@gmail.com")
        print("occupation:", self.list_student[3])
        print("course Registered:", self.list_student[4])

pyatb=PyATB(["Rahul",9605898972,"rahul","Maual tester","Python"])
pyatb.print_student_information()
print("\n")
pyatb1=PyATB(["vinay",8899605898,"vinay12","Automation Tester","Java"])
pyatb1.print_student_information()
print("\n")
pyatb2=PyATB(["Jovana",7896580889,"jovana23","Manual Tester","SDET Master_Class"])
pyatb2.print_student_information()