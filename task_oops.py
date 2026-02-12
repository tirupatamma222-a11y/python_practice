
# create a student class with display_details method and print two objects


class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def display_details(self):
        print(f"name:{self.name} and marks:{self.marks}")

s1=student("renu",80)
s2=student("charith",90)

s1.display_details()
s2.display_details()






# create a calculator class with add,subtract, multiply and divide methods

class calculator:

    def add(self,a,b):
        return a+b
    def sub(self,a,b):
       return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        return a/b

c1=calculator()

c1.add(12,2)
c1.sub(12,2)
c1.mul(12,2)
c1.div(12,2)






# create a bank account system

class bank_account:

    def __init__(self,acc_holder,balance):
        self.acc_holder=acc_holder
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print(f"{self.acc_holder} balance is {self.balance}") 
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")    
        else:
            self.balance-=amount
            print(f"{self.acc_holder} balance is {self.balance}")

    def check_bal(self):
       print(f"{self.acc_holder} balance is {self.balance}")
    
a1=bank_account("renu",1000)
a2=bank_account("charith",5000)

a1.withdraw(500)
a2.withdraw(100)





# employee class

class employee:
    def __init__(self,name,salary):
        self.salary=salary
        self.name=name
    def give_raise(self,percent):
        increase=self.salary*(percent/100)
        self.salary+=increase
        print(f"{self.name} new salary is {self.salary}")
e1=employee("tiru",20000)
e1.give_raise(75)



















