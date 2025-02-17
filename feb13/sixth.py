class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

account = BankAccount(43182700, 1000)
print(account.balance)
account.deposit(4500)
print(account.balance)