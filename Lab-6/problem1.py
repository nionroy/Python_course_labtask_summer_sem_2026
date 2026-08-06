class BankAccount:
    # Constructor
    def __init__(self, account_number, customer_name, date_of_opening, balance):
        self.account_number = account_number
        self.customer_name = customer_name
        self.date_of_opening = date_of_opening
        self.balance = balance

    # Deposit money
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    # Withdraw money
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance!")

    # Check current balance
    def check_balance(self):
        print("Current Balance:", self.balance)


# Create an object
account1 = BankAccount(
    "123456789",
    "John",
    "06-08-2026",
    5000
)

# Show account details
print("Account Number:", account1.account_number)
print("Customer Name:", account1.customer_name)
print("Date of Opening:", account1.date_of_opening)
print("Balance:", account1.balance)

print()

# Deposit money
account1.deposit(2000)

# Withdraw money
account1.withdraw(1000)

# Check balance
account1.check_balance()