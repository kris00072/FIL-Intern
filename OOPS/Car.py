class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def display(self):
        print(f"Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")



class Employee(Car):
    def __init__(self,name,eid,cname,model,color):
        super().__init__(cname, model, color)
        self.name=name
        self.eid=eid
        
        super().display()

c=Employee("Krishan","AID567","Porsche","911","red")        

             
        