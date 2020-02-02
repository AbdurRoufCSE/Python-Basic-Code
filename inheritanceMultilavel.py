class A:
    def disply1(self):
         print("I am in A class")
class B(A):
    def disply2(self):
        print("I am in B class")
class C(B):
    def disply3(self):
        print("I am in C class")

c=C()
c.disply1()
c.disply2()
c.disply3()
