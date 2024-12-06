class calc:
    def sum(self,*args):
        for a in args:
            print(a)


calc_ref=calc()
calc_ref.sum(1,2,3,4)
calc_ref.sum(1,2,3)