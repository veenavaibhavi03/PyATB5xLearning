from browserPackage.OpenBroswer import start_browser
from browserPackage.CloseBroswer import close_browser


class browsr:

    def browse(self):
        start_browser()
        close_browser()

B=browsr()
B.browse()