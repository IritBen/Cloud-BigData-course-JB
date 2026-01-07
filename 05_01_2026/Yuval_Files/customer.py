"""This is the customer class, it contains details about the customer, 
such as it's name, balance, id?, pet_name"""

class Customer:

    def __init__(self, name, balance, id, pet_name): # Constructor
        self.name = name
        self.balance = balance
        self.id = id
        self.pet_name = pet_name
        self.number_of_customers = 0

class A:

    def __init__(self):
        pass

    def print_a(self):
        print("a")

class A_B:

    def __init__(self, a):
        self.a = a
    
    def print_a_b(self):
        self.a.print_a(), print("B")



if __name__ == "__main__":
    james = Customer("James", 18, 0, "Shmolik")
    # print(james.name, james.balance, james.id, james.pet_name)
    shlomit = Customer("Shlomit", 10, 1, "")
    # print(james.number_of_customers, shlomit.number_of_customers)
    a = A()
    a_b = A_B(a)
    a_b.print_a_b()