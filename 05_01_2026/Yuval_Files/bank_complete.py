# This is an example of Bank class it demonstrates the syntax of a class and how to create objects as well as the logic behind their methods and creation
import customer_complete # must be in the same directory 



class Bank:
    def __init__(self, name, place, balance=0, customers=None):
        self.name = name
        self.place = place
        self.balance = balance
        self.customers = customers if customers is not None else [] # This isn't pretty

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def get_balance(self):
        return self.balance

    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} registered at {self.name}, with initial balance {customer.balance}.")

    def get_customer_info(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                return customer
        return None

    def get_all_customers(self):
        return self.customers

    def get_total_balance(self):
        return sum(customer.balance for customer in self.customers) # you haven't learn this yet don't be scared

    def customer_deposit(self, customer_name, amount):
        # check if customer name is valid
        if customer_name not in [customer.name for customer in self.get_all_customers()]:
            print(f"Customer {customer_name} not found.")
            return
        # check amount is greater than 0
        if amount <= 0:
            print(f"Invalid deposit amount: {amount}.")
            return
        
        customer = self.get_customer_info(customer_name)
        if customer:
            customer.balance += amount
            print(f"Deposited {amount} into {customer_name}'s account.")

    def customer_withdraw(self, customer_name, amount):
        # check if customer name is valid
        if customer_name not in [customer.name for customer in self.get_all_customers()]:
            print(f"Customer {customer_name} not found.")
            return
        # check amount is greater than 0
        if amount <= 0:
            print(f"Invalid withdraw amount: {amount}.")
            return

        customer = self.get_customer_info(customer_name)
        if customer:
            if amount > customer.balance:
                print(f"Insufficient funds in {customer_name}'s account.")
            else:
                customer.balance -= amount
                print(f"Withdrew {amount} from {customer_name}'s account.")
        else:
            print(f"Customer {customer_name} not found.")

if __name__ == "__main__":
    bank = Bank("My Bank", "New York", 1000)
    bank.deposit(500)
    bank.withdraw(200)
    print(f"Current balance is {bank.get_balance()}.")
    alice = Customer("Alice", 30, 1000)
    bob = Customer("Bob", 25, 500)
    bank.register_customer(alice)
    print(alice.balance)
    bank.register_customer(bob)

    bank.customer_deposit("Alice", 200)
    bank.customer_withdraw("Bob", 100)

    print(f"Current balance is {bank.get_balance()}.")
    print(f"Total balance across all customers is {bank.get_total_balance()}.")
