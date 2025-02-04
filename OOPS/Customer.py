class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def deposit(self,money):
        self.money=money   
        self.__balance=self.__balance+money
        return self.__balance
    def withdraw(self,money):
        if money>self.__balance:
            return "Insufficient balance"
        else:
            self.__balance=self.__balance-money
            return self.__balance
        
s=Customer("Krishan",5000)   
print(s.deposit(1000))  
print(s.withdraw(1000))