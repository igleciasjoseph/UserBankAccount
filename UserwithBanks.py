class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name}'s balance is {self.account.acc_balance}")
        return self

class BankAccount:
    def __init__(self, interest=0.01, balance=0):
        self.int_rate = interest
        self.acc_balance = balance
    
    def deposit(self, amount):
        self.acc_balance += amount
        return self

    def withdraw(self, amount):
        if 5 < self.acc_balance > 0:
            self.acc_balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.acc_balance -= 5
        return self

    def display_account_infor(self):
        print(f"Balance for: {self.acc_balance}")
        return self

    def yield_interest(self):
        self.acc_balance += self.acc_balance * self.int_rate
        print(f"New Balance with Interest: {self.acc_balance()}")
        return self

Joe = User("Joe", 500)
Joe.make_deposit(500).make_withdrawal(100).display_user_balance()