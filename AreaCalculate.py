class area:
    base=""
    height=""
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def disply(self):
        result=.5*self.base*self.height
        print("Area is:",result)


t1=area(10,20)
t1.disply()

t2=area(20,30)
t2.disply()