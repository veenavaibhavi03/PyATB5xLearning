#Web Automation
#

class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirmation(self):
        if self.email=="vinay89@gmail.com" and self.password=="vinay2020":
            print("Login Success")

        else:
            print("Login Failed!")


email=input("Enter a vaild mailid \n")
password=input("Enter a valid Password \n")
vwo_loginpage=VWOLoginPage(email,password)
vwo_loginpage.login_confirmation()