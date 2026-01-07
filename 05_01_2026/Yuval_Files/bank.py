"""This is class bank"""

class Bank:

    def __init__(self, name, location, branch, clients=None): # Constructor
        self.name = name
        self.location = location
        self.branch = branch
        self.number_of_clients = 0
        self.clients = {"clients_names": [], "clients_balance": [], "clients_id": []}

        
    def register_client(self, client_name, client_id, client_balance):
        self.clients['clients_names'].append(client_name)
        self.clients['clients_id'].append(client_id)
        self.clients['clients_balance'].append(client_balance)
        # self.number_of_clients = self.number_of_clients + 1
        self.number_of_clients += 1 # same as previous line

    def deposit_client(self, amount, client_name, client_id):
        self.clients["clients_balance"][client_id] += amount
        # self.clients["clients_balance"][client_name] += amount

    def withdraw_client(self, amount, client_name, client_id):
        # Check if balance is enough to withdraw that amount
        if self.clients['clients_balance'][client_id] >= amount:
            self.clients['clients_balance'][client_id] -= amount

        else:
            print(f"Client {client_name} balance isn't high enough for this amount {amount}")
        # self.clients[client_id]['client_balance'] # Not going to work in this implementation
        # print current balance after withdraw
        print("client current balance:", self.clients['clients_balance'][client_id])

    def does_client_exist(self, name, client_id, client_balance):
        # check if clinet exist
        clients_names = self.clients["clients_names"]
        name_exist = name in clients_names
        id_exist = client_id in self.clients['clients_id']
        balance_true = (client_balance == self.clients["clients_balance"][client_id])
        result = name_exist and id_exist and balance_true
        return result


if __name__ == "__main__":
    jb = Bank("jhon Bryce", "Israel", "Tel Aviv")
    print(jb.name)
    print(jb.location)
    print(jb.branch)
    jb.register_client("Ariel", 0, client_balance=100)
    jb.register_client("Mriel", 1, client_balance=1000)
    print(jb.clients)
    jb.deposit_client(100, "Ariel", 0)
    print(jb.clients)
    jb.withdraw_client(100, "Ariel", 0)
    print(jb.clients)
    jb.withdraw_client(2000, "Mriel", 1)
    print(jb.clients)
    result = jb.does_client_exist("Ariel", 0, 100)
    print(f"Does client exist: {result}")



    