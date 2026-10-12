"""Act3. Create a class named BankAccount with the following characteristics:
- A class attribute named bank = "Central Bank".
- An instance method named show_balance() that prints the client's balance.
- A class method named show_bank() that prints the bank's name.
- A static method named convert_currency(value) that receives an amount in dollars and converts it to pesos (use a fixed exchange rate of your choice).
Create one object of the BankAccount class and call each method to demonstrate its use."""

class BankAccount: # We create a class called BankAccount.
    # Class attribute: belongs to ALL accounts, not just one.
    bank = "Central Bank"

    def __init__(self, client, balance): # The constructor: runs when we create a new BankAccount.
        # Self refers to this particular account.
        self.client = client  # Here we store the client's name for this account.
        self.balance = balance # Here we store the balance for this account.

    def show_balance(self): # Instance method: shows the balance of ONE specific account.
        # Self inside the parentheses receives the current instance so that its data can be used.
        print(f"Customer: {self.client} - balance: ${self.balance} USD")
        # We use f-strings (f"...") to interpolate text with variables.
        # Whatever is inside { } is replaced with the actual value of each attribute.
        # self.client is this account's client, self.balance is this account's balance.

    @classmethod
    def show_bank(cls): # Class method: shows information shared by ALL accounts.
        # cls refers to the class itself, not to a single object.
        print(f"Bank: {cls.bank}")
        # cls.bank accesses the class attribute "bank" that is common to all accounts.

    @staticmethod
    def convert_currency(value): # Static method: does not depend on self or cls.
        # It only receives a value and performs a calculation.
        # Fixed exchange rate: 1 USD = 18.41 MXN
        # Dollar exchange rate 10/10/2026
        pesos = value * 18.41 # It performs the calculation by multiplying the amount in dollars by the fixed exchange rate.
        print(f"${value} USD = ${pesos} MXN") # Displays the result in a readable format, indicating how many pesos the entered dollars are equivalent to.
        return pesos # returns the converted value, allowing you to store it in a variable or use it in subsequent calculations.

# We create one object (account) with specific data.
cuenta1 = BankAccount("Juan", 500) # We create an object called cuenta1 with client name and balance.
# "Juan" is stored in self.client.
# 500 is stored in self.balance.

# We ask the account to show its balance.
cuenta1.show_balance() # We call Juan's show_balance method, which uses its own data to print the balance.

# We ask the class to show the bank name.
BankAccount.show_bank() # We call the class method show_bank, which prints the bank name.

# We use the static method to convert currency.
BankAccount.convert_currency(100) # We call convert_currency with 100 USD, which converts it to pesos.