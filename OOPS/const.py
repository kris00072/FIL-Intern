class Student:
    def __init__(self,*args):
        if(len(args)==2):
            self.name="sss"
            self.age=40
        if(len(args)==3):
            self.name="my"
            self.age=100
            self.classs="namee"    
    
    def dsp(self):
        print(self.name,self.age)
    def dsp1(self):
        print(self.name,self.age,self.classs)

s=Student(40,20,10);  
s.dsp1()      