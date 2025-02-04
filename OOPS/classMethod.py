class Student:
    __a=10;
    def dsp(self):
        print(self.__a)
    @classmethod
    def m1(cls):
        print(cls._Student__a)
        
s=Student()
Student.m1() 
s.dsp()       
