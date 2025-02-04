class P:
    def m1(self):
        print("hello P")

class C(P):
    def m1(self):
        print("Hello C")
        super().m1() 

c=C()
c.m1()                   