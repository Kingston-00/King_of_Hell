# Base class BankAccount
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

# Derived class SavingsAccount (inherits from BankAccount)
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)  # Initialize base class
        self.interest_rate = interest_rate

    def calculate_interest(self):
        # Calculate interest on the balance
        return (self.balance * self.interest_rate) / 100

# Get user input
account_holder = input("Enter account holder's name: ")
balance = float(input("Enter the account balance: "))
interest_rate = float(input("Enter the interest rate: "))

# Create a SavingsAccount object with user inputs
account = SavingsAccount(account_holder, balance, interest_rate)

# Calculate and print interest
interest = account.calculate_interest()
print(f"\nAccount Holder: {account.account_holder}")
print(f"Balance: ${account.balance}")
print(f"Interest: ${interest}")
