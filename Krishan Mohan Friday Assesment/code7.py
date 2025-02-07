

class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
class Department(Employee):
    def __init__(self,deptname,departid,name,id,dept):
        super().__init__(name,id,dept)
        self.deptname=deptname
        self.departid=departid

    def display(self):
        ename=self.name
        print("Name:",self.name)
        print("Id Of The Employee Is",self.id)
        print(f"Department Name Of The {ename} Is",self.departid)


    
employeeDetails=Department("ETS","ETS7XXX","Krishan","AID-XXX","DATA DELIEVERY")
employeeDetails.display()