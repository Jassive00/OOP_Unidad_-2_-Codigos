"""Act 2. Create class Accountant with a method generate_report() that prints "generate_report()" that prints "Generating financial report".
    Create a class Technical with a method repair_machine() that prints "Repair machine".
    Create a class Boss that inherits from both classes and test both methods."""
class Accountant: # We create a class called Accountant.
    def generate_report(self): # Instance method: used to generate a report.
        print("Generating financial report") # Displays a message indicating that the financial report is being generated.
"""Here is the Accountant class. Its only purpose is to have a method that 
prints a message related to its job: generating reports."""
        
class Technician: # We create a class called Technician.
    def repair_machine(self): # Instance method: used to display the message below
        print("Repairing machine") # Displays a message indicating that the machine is being repaired.
"""This is the Technician class. Like the previous one, it has a method 
that represents its main task: repairing machines."""

class boss(Accountant, Technician): # We create a Boss class that inherits from Accountant and Technician.
    pass # We don't add anything new, but through inheritance, it already has the methods of both classes.
"""Here is the Boss class. It inherits from two classes at the same time 
(this is called multiple inheritance). Even though we don't write anything inside it 
(pass means “there is no code here”), the boss can automatically use the methods of 
Accountant and Technician."""

boss1 = boss() # We create an object named boss1 of the Boss class.  Although it does not have its own methods, it inherits those of its two parent classes.
boss1.generate_report() # The boss uses the Accountant method.
boss1.repair_machine() # The boss uses the Technician method.
"""Here we show that the boss can do both:
Generate a report (like an accountant).
Repair a machine (like a technician)."""