"""This is customer classm it contains details about the customer, such as name, balance, id, etc."""

class Customer:

    def __init__(self, name, age, balance = 0):
        self.name = name 
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print(f"Can't deposit {amount}")
            return
        self.balance += amount
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"The amount {amount} is greater than your balance which is {self.balance}")
            return
        self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        if new_age < self.age:
            print("age not valid")
            return
        self.age = new_age

    def set_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    Irit = Customer("Irit Ben", 36, 100)
    print(Irit.get_age())
    print(Irit.get_balance())
    print(Irit.get_name())
    Irit.deposit(500)
    print(Irit.get_balance())
    Irit.deposit(-10)
    print(Irit.get_balance())
    Irit.withdraw(700)
    print(Irit.balance)
    Irit.set_age(30)
    print(Irit.get_age())
    print(Irit.age)
    Irit.set_name('Irit Benbenisti')
    print(Irit.get_name())
        
