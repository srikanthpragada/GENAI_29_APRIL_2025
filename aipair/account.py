# Create Account class  with accno, customer, balance and required methods

class Account:
    def __init__(self, accno, customer, balance=0):
        """Initialize the account with account number, customer name, and initial balance."""
        self.accno = accno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Withdrawal amount exceeds balance or is invalid.")

    def get_balance(self):
        """Return the current balance of the account."""
        return self.balance
    
