class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an initial balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraw money from the account if funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        """Print the current account balance."""
        print(f"Current balance: {self.balance}")

# Usage Example
account = BankAccount(100)  # Create an account with an initial balance of 100
account.deposit(50)         # Deposited 50
account.withdraw(30)        # Withdrew 30
account.check_balance()     # Current balance

# Output:
# Deposited 50. New balance: 150
# Withdrew 30. New balance: 120
# Current balance: 120
