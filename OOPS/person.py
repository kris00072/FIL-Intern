class Person:
    def __init__(self, name, age,id):
        self.name = name
        self.age = age
        self.id = id
    def getInfo(self):
        print(self.name)
        print(self.age)
        print(self.id)

class Employee(Person):
    def __init__(self, name, age,id,salary):
        super().__init__(name,age,id)
        self.salary=salary
        super().getInfo();

e=Employee("KRishan","20","a98",2000)