class area:

    def __init__(self,base,height):
           self.base=base
           self.height=height
    def disply(self):
            print("I am area mehthod")

class rectangle(area):
    def disply(self):
        result = self.base*self.height
        print("Area is rectrangle: ",result)
r=rectangle(10,20)
r.disply()

class trangle(area):
    def disply(self):
        result=.5*self.base*self.height
        print("Area of trangle:",result)
t=trangle(20,30)
t.disply()
