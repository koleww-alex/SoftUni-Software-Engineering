class Account:

    def __init__(self, owner: str, amount: int = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount: int):
        if self.balance + transaction_amount < 0:
            raise ValueError('sorry cannot go in debt!')

        self._transactions.append(transaction_amount)
        return f'New balance: {self.balance}'

    def add_transaction(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')

        return self.handle_transaction(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.amount}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __le__(self, other):
        return self.balance <= other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __add__(self, other):
        merged_account = Account(f'{self.owner}&{other.owner}', self.amount + other.amount)
        merged_account._transactions = self._transactions + other._transactions
        return merged_account
