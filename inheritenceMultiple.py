class A:
    def disply(self):
         print("I am in A class")
class B:
    def disply(self):
        print("I am in B class")
class C(A,B):
    pass
c=C()
c.disply()
