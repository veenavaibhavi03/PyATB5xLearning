class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirmation(self):
        if self.email=="vinay89@gmail.com" and self.password=="vinay2020":
            print("Login Success")

        else:
            print("Login Failed!")


#email=#infuture we will read from csv file or excel file
#password=#infuture we will read from csv file or excel file
vwo_loginpage=VWOLoginPage("vinay89@gmail.com","vinay2020")
vwo_loginpage.login_confirmation()