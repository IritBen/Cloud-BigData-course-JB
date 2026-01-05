"""This is customer classm it contains details about the customer, such as name, balance, id, etc."""

class Customer:

    def __init__(self, customer_name, customer_id, balance):
        self.customer_name = customer_name 
        self.customer_id = customer_id
        self.balance = balance

if __name__ == "__main__":
    Irit = Customer("Irit Ben", 0, 100)
    print(Irit.customer_name)
    print(Irit.customer_id)
    print(Irit.balance)


        
