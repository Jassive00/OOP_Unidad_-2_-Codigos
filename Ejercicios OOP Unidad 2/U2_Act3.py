# Polymorphism: A method can behave in different ways depending on the object that uses it.

# Class for full-time employees
class FulltimeEmployee: # We create a class called FulltimeEmployee.
    def __init__(self, name, salary): # The constructor receives name and salary.
        self.name = name # We store the employee's name.
        self.salary = salary # We store the employee's fixed salary.
    
    def payment(self): # Method that calculates the payment of this employee.
        return f"{self.name} receives a fixed payment of {self.salary}."# Returns a message indicating that the payment is always the same.

# Class for hourly employees
class HourlyEmployee: # We create a class called HourlyEmployee.
    def __init__(self, name, hours_worked, hourly_rate): # The constructor receives name, hours worked, and hourly rate.
        self.name = name # We store the employee's name.
        self.hours_worked = hours_worked # We store the hours worked.
        self.hourly_rate = hourly_rate   # We store the hourly rate. 
    
    def payment(self): # Method that calculates the payment of this employee.
        total = self.hours_worked * self.hourly_rate # Multiply hours by rate.
        return f"{self.name} receives an hourly payment of {total}." # Returns a message indicating how much the employee earned based on the hours worked.
"""This class represents a full-time employee. Their pay does not change: 
    they always receive the same fixed salary.
    The payment() method calculates the payment by multiplying hours by the rate and returns a message with the total."""

# Function that uses polymorphism
def calculate_payment(worker): # This function receives an object called worker.
    print(worker.payment()) # Calls the payment() method of the object, regardless of which class it belongs to.
    # Here polymorphism occurs: the same call produces different results depending on the type of employee.

# Testing with different objects
emp1 = FulltimeEmployee("Rocio", 5000) # We create a full-time employee named Rocio with a fixed salary of 5000.
emp2 = HourlyEmployee("Luis", 40, 100) # We create an hourly employee named Luis who worked 40 hours at 100 each.

calculate_payment(emp1)  # Calls the payment method of FulltimeEmployee  Rocio receives fixed payment.
calculate_payment(emp2)  # Calls the payment method of HourlyEmployee  Luis receives hourly payment.
