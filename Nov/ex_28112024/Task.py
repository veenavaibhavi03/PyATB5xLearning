class PyATB:
    list_student = []

    def __init__(self, name, phone_number, role, mail_id, course_name):
        self.name=name
        self.phone_number=phone_number
        self.role=role
        self.mail=mail_id
        self.course_registered=course_name

    def print_student_information(self):
        print("name of the student:", self.name)
        print("phone_number:", self.phone_number)
        print("Role:", self.role)
        print("mail id:", self.mail + "@gmail.com")
        print("Course_Registered:", self.course_registered)


pyatb = PyATB("Rahul", 7896058989, "Manual Tester", "rahul", "Python")
pyatb.print_student_information()
print("\n")
pyatb = PyATB("vinay", 7650897534, "Automation Tester", "vinay06", "Java")
pyatb.print_student_information()
print("\n")
pyatb = PyATB("Jovana", 8654389012, "Intern Tester", "Jovana78", "SDET Master class")
pyatb.print_student_information()