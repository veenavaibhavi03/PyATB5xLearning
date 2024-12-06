# their is an object class which is parent to the classess
class oldBrowser:
    def openbroswer(self):
        print("Opening the browser")

    def closeBrowser(self):
        print("closing the broswer")


class chrome(oldBrowser):
    def openbroswer(self):
        super().openbroswer()
        print("Chrome Browser is stating!!")

    def closeBrowser(self):
        print("Chrome Broweser is closed")

chrome_reference=chrome()
chrome_reference.openbroswer()
chrome_reference.closeBrowser()