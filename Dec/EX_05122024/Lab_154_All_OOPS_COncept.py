from abc import ABC,abstractmethod

class BankAccount(ABC):

    def __init__(self,Acno,balance,password):
        self.__ac__=Acno
        self.__balance__=balance
        self.__pwd=password


    @staticmethod
    def welcome(nameofcus):
        print("We are fecting the details",nameofcus)

    @abstractmethod
    def check_balance(self,username):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def __passwordCreation__(self):
        pass

class customer(BankAccount):
    def check_balance(self,usernames):
        BankAccount.welcome(nameofcus=usernames)
        print("the customer has balance:" +self.__ac__)

    def deposit(self, amount):
        print("the current balance is ",self.__balance__+amount)

    def __passwordCreation__(self):
        pass


cus=customer("1234567",2356,"xxx")
cus.check_balance("Marina")
cus.deposit(2345)




