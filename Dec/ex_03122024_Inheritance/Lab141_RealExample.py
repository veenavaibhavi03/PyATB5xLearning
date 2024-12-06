class BaseTesCase:
    def openbroswer(self):
        print("Opening the browser")

    def read_from_excel_file(self):
        print("Using Excel")

    def closeBrowser(self):
        print("closing the broswer")


class TestCase1(BaseTesCase):
     def test_1(self):
         self.openbroswer()
         print("Testcase 1 is executed")
         self.read_from_excel_file()
         self.closeBrowser()


class TestCase2(BaseTesCase):
    def test_2(self):
        self.openbroswer()
        print("Tescase 2 is executed")
        self.read_from_excel_file()
        self.closeBrowser()


testcase1=TestCase1()
testcase1.test_1()

testcase2=TestCase2()
testcase2.test_2()