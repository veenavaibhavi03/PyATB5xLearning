from dotenv import load_dotenv
import os
class VWOLoginPage:

    def __init__(self,email_arg,password_arg):
        self.email=email_arg
        self.password=password_arg

    def login_confirmation(self):
        if self.email=="Vinay2024@gmail.com" and self.password=="Vinay38998":
            print("Login Success")

        else:
            print("Login Failed!")


load_dotenv()
email=os.getenv("EMAIL")
password=os.getenv("PASSCODE")
vwo_login_page=VWOLoginPage(email,password)
vwo_login_page.login_confirmation()
print(email,password)


"""vwo_loginpage=VWOLoginPage("vinay89@gmail.com","vinay2020")
vwo_loginpage.login_confirmation()"""