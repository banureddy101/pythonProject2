# class Employee:
#     def __init__(self,fname,lname,pay):
#         self.first_name=fname
#         self.last_name=lname
#         self.salary=pay
#
#     def email(self):
#         return f"{self.first_name}.{self.last_name}@company.com"
#
#     def pay_hike(self,percent_hike):
#         hike_amount=self.salary*percent_hike
#         self.salary=self.salary + hike_amount
#         return self.salary
#
# emp1=Employee('steve', 'jobs', 1000)
# emp2=Employee('bill', 'gates', 5000)
#
# print(emp1.__dict__)
# print(emp2.__dict__)
# print(emp1.pay_hike(0.1))
# print(emp2.pay_hike(0.5))
#
# add=Employee.email(emp1)
# add1=Employee.email(emp2)
# print(add)
# print(add1)
#
#
#
# class calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def add(self):
#         return self.a + self.b
#
#     def sub(self):
#         return self.a - self.b
#
#     def mul(self):
#         return self.a * self.b
#
#     def div(self):
#         return self.a / self.b
#
# c1=calculator(10,20)
# c2=calculator(20,40)
# c3=calculator(50,100)
# c4=calculator(10,5)
# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)
# print(c4.__dict__)
#
# print(c1.add())
# print(c2.sub())
# print(c3.mul())
# print(c4.div())

#
#
# class Bankaccount:
#     interest_rate=0.4 ###class variable
#     def __init__(self,name,balance=0):
#         #instance variable (each customer will get a fresh copy of name,
#         self.name=name
#         self.balance=balance
#         self.transactions=[]
#         self.transactions.append(f"****************intial amount deposite {balance}*****************")
#
#     def deposit(self,amount):
#         self.balance = self.balance+amount
#         self.transactions.append(f'amount deposited{amount}')
#
#
#
#     def withdraw(self,amount):
#         if amount > self.balance:
#             raise ValueError("insufficient funds")
#         self.balance = self.balance - amount
#         self.transactions.append(f'amount withdraw {amount}')
#         return f'please collect the amount {amount}'
#
#     def transfer(self,to_account,amount):
#         if self.balance<amount:
#             raise ValueError("insufficient funds")
#         to_account.deposit(amount)
#         self.balance-=amount
#
#     def statement(self):
#         for transactions in self.transactions:
#             print(transactions)
#             print("*"*20)
#             print(f'available balance is {self.balance}')

    #
    # def roi(self):
    #     interest_amount = self.balance * Bankaccount.interest_rate
    #     self.balance+=interest_amount
    #     self.transactions.append(f"**************intrest amount credit*******{interest_amount}")


# #counting the number of instances created to the class#
# class demo:
#     #shared across all the instances
#     count=0
#     def__init__(self,a,b):
#         self.a=a
#         self.b=b
#         demo.count=demo.count+1
#
# c1=Bankaccount('banu',1000)
# c2=Bankaccount('pratap',3000)
# c3=Bankaccount('bansi')

# print(c1.__dict__)
# print(c2.__dict__)
# print(c3.__dict__)


# print(c1.withdraw(2000))
# print(c1.__dict__)

# print(c1.transfer(c2,100))
# print(c1.balance)
# print(c2.balance)

# print(c1.transfer(c2,100))
# print(c1.__dict__)
# print(c2.balance)

# print(c1.statement())
# print(c2.statement())
# print(c3.statement())

#
# print(c1.roi())
# print(c1.balance)



