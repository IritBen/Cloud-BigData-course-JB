# customer class that fits the bank_complete.py structure
class Customer:
    def __init__(self, name, age, balance=0):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Invalid deposit amount: {amount}.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print(f"Invalid withdraw amount: {amount}.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance is {self.balance}.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        if new_age <= self.age:
            print(f"Invalid age: {new_age}.")
            return
        self.age = new_age
    
    def set_name(self, new_name):
        self.name = new_name

######################################

Irit = Customer('Irit Ben', 36, 1000)
Irit.set_age(30)
print(Irit.age)
print(Irit.get_balance())
print(Irit.balance)