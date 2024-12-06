#static methods can be called using the classname
class o:
    @staticmethod
    def sum(a,b):
        print(a+b)

    def add(self,a,b):
        print(a+b)


o_ref=o()
o_ref.add(1,2)

print(o.sum(1,2))
