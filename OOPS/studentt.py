class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return ("Name is : {} and age is : {}".format(self.name,self.age))    
    
s1=Student("Abhi",78)
print(s1)    
        