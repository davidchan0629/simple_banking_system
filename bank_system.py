import pandas as pd

class Customer:
    def __init__(self, name, init_balance):
        self.name = name
        self.balance = init_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if (amount > 0) and (self.balance >= amount):
            self.balance -= amount
            return True
        return False
    

class bank_system:
    def __init__(self):
        self.customers = {}
    
    def create_account(self):
        name = input("Enter your name: ")
        if name in self.customers:
            print("Account already exists.") # Assume no duplicate names can be registered
            return
        init_balance = float(input("Enter initial deposit amount: "))
        customer = Customer(name, init_balance)
        self.customers[name] = customer
        print(f"Account created for {name} with starting balance {customer.balance}")
    
    def deposit(self, name, amount):
        if name in self.customers:
            if self.customers[name].deposit(amount):
                print(f"Deposited {amount} to {name}'s account.")
            else:
                print("Invalid deposit amount.")
        else:
            print("Account not found.")
    
    def withdraw(self, name, amount):
        if name in self.customers:
            if self.customers[name].withdraw(amount):
                print(f"Withdrew {amount} from {name}'s account.")
            else:
                print("Invalid withdrawal amount of insufficient funds in account.")
        else:
            print("Account not found.")
    
    def show_customers(self):
        for name, customer in self.customers.items():
            print(f"Name: {name}, Balance: {customer.balance}")
    
    def transfer(self, from_name, to_name, amount):
        if (from_name in self.customers) and (to_name in self.customers):
            if self.customers[from_name].withdraw(amount):
                self.customers[to_name].deposit(amount)
                print(f"Transferred {amount} from {from_name} to {to_name}.")
            else:
                print("Invalid transfer amount or insufficient funds.")
        else:
            print("One or both accounts not found.")
    
    def save_to_csv(self, filename):
        data = []
        for customer in self.customers.values():
            data.append({'Name': customer.name, 'Balance': customer.balance})
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("System state saved to CSV file.")
    
    def load_from_csv(self, filename):
        try:
            df = pd.read_csv(filename)
            for index, row in df.iterrows():
                name = row['Name']
                balance = row['Balance']
                customer = Customer(name, balance)
                self.customers[name] = customer
            print("System state loaded from CSV file.")
        except FileNotFoundError:
            print("CSV file not found. Cannot load system state.")
    

