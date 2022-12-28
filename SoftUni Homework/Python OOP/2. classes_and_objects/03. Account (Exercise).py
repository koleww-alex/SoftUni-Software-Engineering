class Account:

    def __init__(self, id_number: int, name: str, balance=0):
        self.id = id_number
        self.name = name
        self.balance = balance

    def credit(self, amount: int):
        self.balance += amount
        return self.balance

    def debit(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance

        return 'Amount exceeded balance'

    def info(self):
        return f'User {self.name} with account {self.id} has {self.balance} balance'

