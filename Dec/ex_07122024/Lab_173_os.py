class xyz:

    def f1(self):
        try:
            a=["1",2,3,4,5]
            print(a[7])
        except IndexError as e:
            print("Index error")
        else:
            print(a)
        finally:
            print("The program is executed")

XYZ=xyz()
XYZ.f1()