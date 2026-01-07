"""This is class bank that imports Customer class"""

from customer import Customer

class Bank:

    def __init__(self, name, location, branch, balance, customers=[]):
        self.name = name
        self.location = location
        self.branch = branch
        self.balance = balance
        self.number_of_customers = 0
        self.customers = customers

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return
        print(f"You can't deposit {amount} ils")

    def withraw(self, amount):  
        if self.balance >= amount:
            self.balance -= amount
            return
        print(f"You can't withdraw {amount} ils. Your balance is {self.balance}")

    def get_balance(self):
        return self.balance

    def register_customer(self, customer):
        self.customers.append(customer)
        print('Customer {customer.name} whick is {customer.age} years old was registered to {self.branch} with balance of {customer.balance}')

# 
    # def does_client_exist(self, name, client_id, client_balance):
        # clients_names = self.clients["clients_name"]
        # name_exist = name in clients_names
        # id_exists = client_id in self.clients['clients_id']
        # balance_true = (client_balance == self.clients["clients_balance"][client_id])
        # result = name_exist and id_exists and balance_true
        # return result
        

if __name__ == '__main__':
    jb = Bank("John Bryce", "Israel", "Tel Aviv")
    print(jb.name)
    print(jb.location)
    print(jb.branch)
    jb.register_client("Ariel", 0, client_balance = 100)
    jb.register_client("Maria", 1, client_balance = 1000)
    print(jb.clients)
    jb.deposit_client(100, "Ariel", 0)
    print(jb.clients)
    jb.withdrawal_client(2000, "Ariel", 0)
    print(jb.clients)
    result = jb.does_client_exist("Ariel", 0, 200)
    print(f"does client exist: {result}") 