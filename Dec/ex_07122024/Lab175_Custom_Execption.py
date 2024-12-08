from bisect import insort_right


class LowBalanceExceptionCustom(Exception):
    def __init__(self,message):
        self.message=message
        super().__init__(message)

balance=200
withdraw=int(input("enter the amount you want to withdraw"))
if withdraw> balance:
    raise LowBalanceExceptionCustom("balance is low")
else:
    print("Remain balance:"+(balance-withdraw))