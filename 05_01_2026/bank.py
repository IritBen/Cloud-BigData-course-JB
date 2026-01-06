"""This is class bank"""

class Bank:

    def __init__(self, name, location, branch, clients=None):
        self.name = name
        self.location = location
        self.branch = branch
        self.number_of_clients = 0
        self.clients = {"clients_name": [], "clients_balance": [], "clients_id": []}

    def register_client(self, client_name, client_id, client_balance):
        self.clients['clients_name'].append(client_name)
        self.clients['clients_id'].append(client_id)
        self.clients['clients_balance'].append(client_balance)
        self.number_of_clients += 1

    def deposit_client(self, amount, client_name, client_id):
        self.clients["clients_balance"][client_id] += amount

    def withdrawal_client(self, amount, client_name, client_id):
        if self.clients["clients_balance"][client_id] - amount >= 0:
            self.clients["clients_balance"][client_id] -= amount
        else:
            print(f" client {client_name} don't have enough money: {amount}")

        print("client current balance: ", self.clients["clients_balance"][client_id])

    def does_client_exist(self, name, client_id, client_balance):
        clients_names = self.clients["clients_name"]
        name_exist = name in clients_names
        id_exists = client_id in self.clients['clients_id']
        balance_true = (client_balance == self.clients["clients_balance"][client_id])
        result = name_exist and id_exists and balance_true
        return result
        

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