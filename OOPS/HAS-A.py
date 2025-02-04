class Engine:
    a=10
    def __init__(self):
        self.b=10;
    def m1(self):
        print(self.a)
class Car:
    def __init__(self):
        self.engine=Engine()
    def m2(self):
        print(self.engine.a)
        print(self.engine.b)
        self.engine.m1()   

c=Car();
c.m2()         
                
