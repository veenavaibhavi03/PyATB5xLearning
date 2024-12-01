# private variables can be only accessesed in class methods
#
class Bank:
    def __init__(self,account_number,balance):
        self.__account_number=account_number #private variable
        self.Balance=balance #public variable
        self.__internal_private_method()


    def check_balance(self):
        print(self.Balance)


    def deposit(self,amount):
        self.Balance=self.Balance+amount

    def show_accountnumber(self,auth_id):
        if auth_id==True:
            print(self.__account_number)
        else:
            print("Not allowed")

    def __internal_private_method(self):
        print("Private method can only be accessed by class")

bank1=Bank(987654321,2000)
bank1.deposit(2000)
bank1.check_balance()
print(bank1.Balance)
bank1.show_accountnumber(True)
#print(bank1.__account_number)