class excelReader:
    @staticmethod
    def read_from_excel():
        print("reading from excel")
    @staticmethod
    def read_data_from_mysql():
        print("reading data from mysql")


class TC1:

    def testcase1(self):
        excelReader.read_from_excel()
        excelReader.read_data_from_mysql()

Tc1=TC1()
Tc1.testcase1()
