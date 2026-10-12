"""Act 1. Create a class Employee with attributes name, and salary, and method show_info() that prints the name and salary.
    Then, create a class Manager that inherits from Employee and adds an attribute department.
    Override show_info() to also display the department."""
class employee: # A class called Employee is created.
    def __init__(self, name, salary): # The constructor: It runs when we create a new employee. name and salary: These are the parameters the constructor needs to create an employee.
        # Self refers to this particular employee.
        # name and salary are the parameters the constructor needs to create an employee.
        # A parameter is like a litter box that receives data when you call a function or create an object.
        self.name = name # The employee's name is saved.
        self.salary = salary # The employee's salary is saved.

    def show_info(self): # Instance method: This is used to display the employee's information.
        print(f"Name: {self.name}, Salary: {self.salary}") # This line is like saying, “Print a message that includes the name and salary, but use the data stored in this object.”
        # We use f-strings to interpolate text with variables.
        # The content inside { } is replaced with the actual value of each attribute.

class manager(employee): # We create a class called Manager that inherits from Employee.
    def __init__(self, name, salary, department): # This is the Manager constructor; it inherits all attributes from the Employee class, with only the department attribute added.
        super().__init__(name, salary,) # # We use super() to call the Employee constructor and reuse name and salary.
        self.department = department # This is where we keep the manager's department.
        """This code block creates a child class (Manager) that inherits from the parent class (Employee), reuses 
        what it already had (name and salary), and adds something of its own (department)."""

    def show_info(self): # Here, we override the show_info() method for the child class.
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}") # Now, in addition to the name and salary, we also show the department.

# We create an object of the Employee class (parent class).
empleado1 = employee("Manuel", 1500) # We created an employee named Manuel with a salary of 1,500.
empleado1.show_info() # Manuel displays his information: name and salary.

# We create an object of the Manager class (subclass)
manager1 = manager("Laura", 60000, "Networking") # We create a manager named Laura with a salary of 60000 and assigned to the Networking department.
manager1.show_info() # Laura displays her information: name, salary, and department.