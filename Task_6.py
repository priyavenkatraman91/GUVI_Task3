class BankAccount:
    def __init__(self, Account_num, balance=0):
        self.account_num = Account_num
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}, Balance: {self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")
        else:
            print("Insufficient balance")



class SavingsAccount(BankAccount):
    def __init__(self, Account_num, balance=0, interest_rate = 0.0):
        super().__init__(Account_num, balance)
        self.interest_rate = interest_rate
    def calculateInterest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest: {interest}, Balance: {self.balance}")

class CurrentAccount(BankAccount):
    def __init__(self, Account_num, balance=0, minimum_balance = 0):
        super().__init__(Account_num, balance)
        self.minimum_balance = minimum_balance
    def withdraw(self, amount):
        if self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            print(f"Withdrew {amount}, Balance: {self.balance}")
        else:
            print("Cannot withdraw. Minimum balance requirement not met")

savings = SavingsAccount("SBI12345", 1000, 0.05)
savings.deposit(500)
savings.calculateInterest()

current = CurrentAccount("BOI45667", 2000, 1000)
current.withdraw(800)
current.withdraw(500)