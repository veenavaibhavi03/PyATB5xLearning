class  Check:
    def __init__(self,a,b,c):
        """
                Parameters
                ----------
                a : list
                    It takes a list as an input
                b : set
                    It takes set as an input
                c : String
                    The input has to be a string
                """
        self.a=a
        self.b=b
        self.c=c
        print("I am called")

        if isinstance(self.a,list):
            self.printList()
        if c!= "" and type(c)==str:
            self.printString()
        if type(b) == set:
            self.printSet()

    def printString(self):
     print(self.c)


    def printList(self):
        for i in self.a:
            print(i)
        #print("The input is list")

    def printSet(self):
        print(self.b)


a=["a","b","c"]
b={1,2,3}
c="alpha"

check=Check(a,b,c)