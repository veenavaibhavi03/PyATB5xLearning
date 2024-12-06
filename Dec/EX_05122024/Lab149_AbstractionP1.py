# hide the un necessary details  will be hidden
from abc import ABC,abstractmethod

class Father(ABC):

    def __init__(self,name):
        self.name=name

    @abstractmethod
    def loan(self):
        pass


class Son(Father):
    def loan(self):
        print(f"Loan is cleared by {self.name}")

s=Son("Jovana")
s.loan()
